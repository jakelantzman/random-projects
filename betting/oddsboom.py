from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def main():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    driver.get("https://www.oddsboom.com/basketball/nba/games/")
    time.sleep(2)
    nba = driver.find_elements_by_class_name("vig")
    nbaGames = driver.find_elements_by_class_name("games")
    gameLinks = nbaGames.
    print(nbaGames)
    gameLinks = []
    for i in nbaGames:
        gameLinks.append(i.get_attribute("href"))
    print(gameLinks)

if __name__ == "__main__":
    main()

