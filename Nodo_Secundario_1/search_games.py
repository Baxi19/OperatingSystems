from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json

# Search game in Amazon
def search(name, price):
    url = 'https://www.amazon.com/s?i=videogames-intl-ship&bbn=16225016011&rh=n%3A20972781011%2Cn%3A20972797011%2Cp_89%3APlaystation&dc&language=es&fst=as%3Aoff&pf_rd_i=16225016011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=e963b29d-d654-4995-bbb2-582c8cfbb5e4&pf_rd_r=0E6CBDMYSY2Z4QW1EYKE&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1619289230&rnid=20972781011&ref=sr_nr_n_3'

    # Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(
        executable_path="../chromedriver", options=options)
    driver.get(url)

    time.sleep(2)

    searchTextBox = driver.find_element_by_id('twotabsearchtextbox')
    searchTextBox.clear()
    searchTextBox.send_keys(name)

    searchBtn = driver.find_element_by_id('nav-search-submit-button')
    searchBtn.click()

    # Amazon changes the search category when it can't find the item
    searchCategory = driver.find_element_by_id('nav-search-label-id')

    if (searchCategory.text != "Juegos de PlayStation 5"):
        # The requested item was not found
        return False
    else:
        if (price == "Gratuito"):
            return False
        # Price
        price_find_element = driver.find_element_by_xpath('//*[@class="a-offscreen"]')
        price_find = price_find_element.get_attribute('innerText')
        # Price wasn't available
        if ("US$" in price_find == False):
            return False

        # Price in PS wasn't available
        if ("US$" in price == True):
            price = price.split("US$")[1]
        else: 
            pass

        price_find = price_find.split("US$\xa0")[1]
        return compare_price(price, price_find)

def compare_price(actual_price, price_find):
    if (actual_price <= price_find):
        return False
    else:
        return price_find