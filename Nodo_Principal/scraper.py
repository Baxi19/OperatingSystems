import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from socket_client import Socket_Client

def parse(page):
    url = 'https://store.playstation.com/es-cr/category/d71e8e6d-0940-4e03-bd02-404fc7d31a31/' + str(page)
    
    # Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')

    driver = webdriver.Chrome(executable_path="../chromedriver", options=options)
    driver.get(url)
    games = driver.find_elements_by_xpath('/html/body/div[3]/main/section/div/div/ul/li')

    time.sleep(3)
    ps5_list = []
    
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
            "price":game_price,
            "store":"PlayStation",
            "url": modify_url[0]
        }

        ps5_list.append(newGame)
        
    driver.close()
    return ps5_list


def get_ps5_games():
    #for page in range(1, 5):
    
    #    print(page)
    #    parse(page)
    
    gameList = parse(1)
    for game in gameList:
        print("\n==========================================================================================================")
        print(game['name'])
        print(game['price'])
        print(game['store'])
        print(game['url'])
            

    
    # Test
    client = Socket_Client("localhost",10000, b'Hello, Im Node 1')
    client.send()

    client2 = Socket_Client("localhost",11000, b'Hello, Im Node 1')
    client2.send()

if __name__ == "__main__":
    get_ps5_games()
