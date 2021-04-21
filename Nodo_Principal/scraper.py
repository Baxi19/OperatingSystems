import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def parse(page):
    url = 'https://store.playstation.com/es-cr/category/d71e8e6d-0940-4e03-bd02-404fc7d31a31/' + str(page)
    
    # Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')

    driver = webdriver.Chrome(executable_path="../chromedriver", options=options)
    driver.get(url)
    games = driver.find_elements_by_xpath('/html/body/div[3]/main/section/div/div/ul/li')

    time.sleep(3)
    cont = 1
    for item in games:
        print("\n==========================================================================================================")
        print(cont)
        cont += 1

        # url
        game_url = item.find_element_by_xpath('.//div[@class="ems-sdk-product-tile"]/a/div/div/span[2]/img').get_attribute('src')
        modify_url = game_url.split(sep="?")

        # name
        game_name = item.find_element_by_xpath('.//section[@class="ems-sdk-product-tile__details"]/span').text

        # price
        game_price = item.find_element_by_xpath('.//section[@class="ems-sdk-product-tile__details"]/div/span[@class="price"]').text

        print(modify_url[0])
        print(game_name)
        print(game_price)

    driver.close()


def get_ps5_games():
    # for page in range(1, 13):
    #    time.sleep(3)
    #    parse(page)
    parse(1)


if __name__ == "__main__":
    get_ps5_games()
