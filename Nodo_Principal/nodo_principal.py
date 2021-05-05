import multiprocessing as mp
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from socket_client import Socket_Client
import json
import pickle

global list_games

# Insertion at server from 24 to 24 games
def insertAllGames(games):
    url = 'https://operating-systems.herokuapp.com/loadGames'
    header = {"content-type": "application/json"}
    data = json.dumps({'array': games})
    res = requests.post(url, data=data, headers=header, verify=False)
    print("NODE_1>Games inserted in server by :"+str(mp.current_process().name) + " => "+res.text)

# Update Amazon price
def updateAmazonGame(game):
    url = 'https://operating-systems.herokuapp.com/updateAmazonGame'
    header = {"content-type": "application/json"}
    data = json.dumps({"games": game})
    res = requests.put(url, data=data, headers=header)
    print("NODE_1>Game price updated in server: " + res.text)

# Update Time
def updateTimeGame(game):
    url = 'https://operating-systems.herokuapp.com/updateTimeGame'
    header = {"content-type": "application/json"}
    data = json.dumps({"games": game})
    res = requests.put(url, data=data, headers=header)
    print("NODE_1>Game time updated in server: " + res.text)

# Update Meta
def updateMetaGame(game):
    url = 'https://operating-systems.herokuapp.com/updateMetaDataGame'
    header = {"content-type": "application/json"}
    data = json.dumps({"games": game})
    res = requests.put(url, data=data, headers=header)
    print("NODE_1>Game meta updated in server: " + res.text)


# Clean the games list
def deleteAllGames():
    url = 'https://operating-systems.herokuapp.com/deleteAllGames'
    res = requests.get(url)
    print("NODE_1>Delete all games in server: " + res.text)
    return True


# Get PS5 games by page
def parse(page):
    ps5_list = []
    url = 'https://store.playstation.com/es-cr/category/d71e8e6d-0940-4e03-bd02-404fc7d31a31/'+str(page)

    # Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')

    driver = webdriver.Chrome(
        executable_path="../chromedriver", options=options)
    driver.get(url)

    time.sleep(3)

    games = driver.find_elements_by_xpath('/html/body/div[3]/main/section/div/div/ul/li')

    for item in games:
        # url
        game_url = item.find_element_by_xpath('.//div[@class="ems-sdk-product-tile"]/a/div/div/span[2]/img').get_attribute('src')
        modify_url = game_url.split(sep="?")

        # name
        game_name = item.find_element_by_xpath('.//section[@class="ems-sdk-product-tile__details"]/span').text

        # price
        game_price = item.find_element_by_xpath('.//section[@class="ems-sdk-product-tile__details"]/div/span[@class="price"]').text

        newGame = {
            "name": game_name,
            "price": game_price,
            "store": "PlayStation",
            "url": modify_url[0],
            "time": "",
            "meta": ""
        }

        ps5_list.append(newGame)

    driver.close()
    return ps5_list

# Execution threads, get the data, after that insert in server and give some task to secondary nodes
def prepare_data(page):
    print("NODE_1>Multiprocessing: Working on Page: " + str(page))
    print("NODE_1>Process: "+str(mp.current_process().name))
    block_games = parse(page)
    insertAllGames(block_games)

    # Data ready to start to working with Node 1 & 2
    result = reduce_data(block_games)
    data = pickle.dumps(result)

    # Send by sockets
    #client = Socket_Client("localhost", 10000, data)
    #client.send()
    
    client2 = Socket_Client("localhost", 11000, data)
    client2.send()

    

# Reduce data to secondary nodes
def reduce_data(games):
    res = ""
    size = len(games)
    for game in games:
        res += game['name']+'\\~'+game['price']
        if games.index(game) != (size-1):
            res += '\\^'
    return res


# Get range of games Multiprocessing
def get_ps5_games_multiprocessing(task):

    # TODO:
    # Multiprocessing
    pool = mp.Pool(mp.cpu_count())
    pool.map(prepare_data, task)
    print("NODE_1>Multiprocessing: All data Sended!")



# Main App
if __name__ == "__main__":
    deleteAllGames()
    list_games = []

    quantity = 4  # Note: quantity = (quantity * 24)
    task = []
    for i in range(1, (quantity + 1)):
        task.append(i)
    
    get_ps5_games_multiprocessing(task)
    time.sleep(300)
    print("NODE_1>Finished all process")

    """
    game1 = {
        "name": "Bugsnax",
        "price": 1
    }
    updateAmazonGame(game1)
    
    
    # Test: Time Update
    game2 = {
        "name": "Bugsnax",
        "time": 420
    }
    updateTimeGame(game2)
    
    
    # Test: MetaData Update
    game3 = {
        "name": "Bugsnax",
        "meta": 4
    }
    updateMetaGame(game3)
    """