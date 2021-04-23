import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from socket_client import Socket_Client
import json
import pickle

# Insertion at server from 24 to 24 games
def insertAllGames(games):
    url = 'http://localhost:8888/loadGames'
    header = {"content-type": "application/json"}
    data = json.dumps({'array': games})
    res = requests.post(url, data=data, headers=header, verify=False)
    print(res.text)

# Clean the games list
def deleteAllGames():
    url = 'http://localhost:8888/deleteAllGames'
    res = requests.get(url)
    print("Delete all games in server: " + res.text)


# Get PS5 games by page
def parse(page):
    ps5_list = []
    url = 'https://store.playstation.com/es-cr/category/d71e8e6d-0940-4e03-bd02-404fc7d31a31/' + str(page)

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

# prepare data to secondary nodes
def reduce_data(games):
    res = ""
    size = len(games)
    for game in games:
        res += game['name']+'\\~'+game['price']
        if games.index(game) != (size-1):
            res += '\\^'
    return res


# Get range of games
def get_ps5_games(quantity):
    deleteAllGames()
    for page in range(1, (quantity + 1)):
        print("NODE_1>Working on Page: " + str(page))
        block_games = parse(page)
        insertAllGames(block_games)

        # Data ready to start to working with Node 1 & 2
        result = reduce_data(block_games)
        data = pickle.dumps(result)

        # Send by sockets
        if page % 2 == 0:
            client2 = Socket_Client("localhost", 11000, data)
            client2.send()
        else:
            client = Socket_Client("localhost", 10000, data)
            client.send()

    print("NODE_1>All data Sended!")


if __name__ == "__main__":
    quantity = 4 # Note: quantity = (quantity * 24)
    get_ps5_games(quantity)

    print("NODE_1>Finished process")
