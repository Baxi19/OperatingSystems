from multiprocessing import Process, Manager
from selenium import webdriver
import time
from socket_client import Socket_Client
import pickle
import json
import requests

# Clean the games list
def deleteAllGames():
    url = 'https://operating-systems.herokuapp.com/delete'
    res = requests.get(url)
    print("NODE_1>Delete all games in server: " + res.text)
    return True

# PS5
def insertAllGames(games):
    url = 'https://operating-systems.herokuapp.com/games'
    header = {"content-type": "application/json"}
    data = json.dumps({'array': games})
    res = requests.post(url, data=data, headers=header, verify=False)
    print("NODE_1>Games inserted in server  => "+res.text)


# Task to get first info
def task(i, l):
    print("NODE_1>Hilo {0} - Inicio su trabajo".format(i))
    array = []
    url = 'https://store.playstation.com/es-cr/category/d71e8e6d-0940-4e03-bd02-404fc7d31a31/'+str(i)
    id_game = 0
    if(i == 2):
        id_game = 25 
    elif(i == 3):
        id_game = 49
    elif(i == 4):
        id_game = 73
    else:
        id_game = i
        

    # Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')

    driver = webdriver.Chrome(
        executable_path="../chromedriver", options=options)
    driver.get(url)

    time.sleep(3)

    games = driver.find_elements_by_xpath(
        '/html/body/div[3]/main/section/div/div/ul/li')

    for item in games:
        # url
        game_url = item.find_element_by_xpath(
            './/div[@class="ems-sdk-product-tile"]/a/div/div/span[2]/img').get_attribute('src')
        modify_url = game_url.split(sep="?")

        # name
        game_name = item.find_element_by_xpath(
            './/section[@class="ems-sdk-product-tile__details"]/span').text

        # price
        game_price = item.find_element_by_xpath(
            './/section[@class="ems-sdk-product-tile__details"]/div/span[@class="price"]').text

        newGame = {
            "id": str(id_game),
            "name": game_name,
            "price": game_price,
            "store": "PlayStation",
            "url": modify_url[0],
            "time": "",
            "meta": ""
        }
        #l.append(newGame)
        array.append(newGame)
        id_game += 1

    driver.close()    
    data = pickle.dumps(array)

    # Send by sockets
    client = Socket_Client("localhost", 10000, data)
    client.send()
    data_node1 = client.result()
    
    client2 = Socket_Client("localhost", 11000, data)
    client2.send()
    data_node2 =client2.result()

    # Join all response data from node secundaries
    for node1 in data_node1:
        for node2 in data_node2:
            if node1['id'] == node2['id']:
                node2['price'] = node1['price']
                node2['store'] = node1['store']
    
    l.extend(data_node2)
    print("NODE_1>Hilo {0} - Fin de su trabajo".format(i))


def main(quantity):
    with Manager() as manager:
        l = manager.list()

        # Pool
        piscina = []
        for i in range(1, (quantity+1)):
            print("NODE_1>PADRE: creando Hilo {0}".format(i))
            piscina.append(Process(target=task, args=(i, l)))

        # Start
        print("NODE_1>PADRE: arrancando hilos")
        for proceso in piscina:
            proceso.start()

        print("NODE_1>PADRE: esperando a que los procesos hagan su trabajo")
        while piscina:
            for proceso in piscina:
                if not proceso.is_alive():
                    proceso.join()
                    piscina.remove(proceso)
                    del(proceso)

        print("NODE_1>Fin del trabajo de los hilos")
        insertAllGames(list(l))
        
if __name__ == "__main__":
    deleteAllGames()
    quantity = 4  # Note: quantity = (quantity * 24)
    main(quantity)
    print("NODE_1>Fin")
