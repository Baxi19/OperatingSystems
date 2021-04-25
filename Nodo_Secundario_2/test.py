import metascore

def print_resource_data(resource):
    print ("Name: " + resource.name)
    print ("Release date: " + resource.date)
    print ("Metascore: " + str(resource.metascore))
    print ("Userscore: " + str(resource.userscore))
    


def main():
    scraper = metascore.Scraper()
    alien = scraper.get("https://www.metacritic.com/game/xbox-one/stardew-valley")
    print_resource_data(alien)
   

if __name__ == "__main__":
    main()
