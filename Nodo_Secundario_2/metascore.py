import requests
import bs4

def print_resource_data(resource):
    print ("Name: " + resource.name)
    print ("Metascore: " + str(resource.metascore))
    
def round_to(n, precision):
    correction = 0.5 if n >= 0 else -0.5
    return int( n/precision+correction ) * precision

def  meta(name):
    scraper = Scraper()
    query=Query(name)
    url=query.get_url()
    game = scraper.get(url)
    game.metascore=round_to(game.metascore/20,0.5)
    #print_resource_data(game)
    return game


# Contains info about the query to be made
class Query(object):
    # Standard constructor (w/ parameters)
    def __init__(self, terms):
        self.terms = terms
        self.base_url = "http://www.metacritic.com/search/game"
        self.url = self.base_url+ "/" + terms + "/results"
    # Returns the URL of the created query
    def get_url(self):
        scra=Scraper()
        urlf="http://www.metacritic.com"+scra.search(self.url)
        return urlf

# This class represents a generic resource found at Metacritic
class Resource(object):
    def __init__(self, name, metascore):
        self.name = name
        self.metascore = metascore     
class Response(object):
    def __init__(self, status, content):
        self.status = status
        self.content = content

    def valid(self):
        return (self.status == 200)

class Browser(object):
    def get(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        request = requests.get(url,headers=headers)
        
        response = Response(request.status_code, request.content)
        return response


class Scraper(object):
    def __init__(self):
        self.browser = Browser()
        self.response = ""
        self.soup = ""

    def get(self, url):
        self.response = self.browser.get(url)
        
        self.soup = bs4.BeautifulSoup(self.response.content,features="html.parser")
        
        return self.extract_data()
    def search(self, url):
        self.response = self.browser.get(url)
        
        self.soup = bs4.BeautifulSoup(self.response.content,features="html.parser")
        
        return self.extract_url()
    def extract_url(self):
        titles = self.soup.select(".product_title")
        try:
            for a in titles[0].find_all('a', href=True):
                url=a['href']
            
            return url
        except:
            print(error)
            return ("mal")
    def extract_data(self):
        name = self._extract_name()
        metascore = self._extract_metascore()
        resource = Resource(name, metascore)
        return resource

    def _extract_name(self):
        titles = self.soup.select(".product_title")
        
        try:
           
            title = titles[0].text
            info = title.split("\n")
            name = info[2].strip()
            return name
        except:
            print(error)
            return ("mal")

    
    def _extract_metascore(self):
        section = self.soup.select(".metascore_wrap")[0]
        
        score = section.select(".metascore_w")[0].text
        
        return int(score)
   

