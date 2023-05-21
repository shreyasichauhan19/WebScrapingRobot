from RPA.Browser.Selenium import Selenium
from bs4 import BeautifulSoup
import time
import requests

br = Selenium()


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage):
        br.open_available_browser(webpage)

    def print_first_paragraph(self, webpage):
        self.open_webpage(webpage)
        time.sleep(5)  # Allow the page to load
        response = requests.get(webpage)
        soup = BeautifulSoup(response.text, 'html.parser')
        first_paragraph = soup.select_one('div.mw-parser-output > p:not(.mw-empty-elt)').text
        print(first_paragraph)

    def print_bday_dday(self, webpage):
        self.open_webpage(webpage)
        time.sleep(5)  # Allow the page to load
        response = requests.get(webpage)
        soup = BeautifulSoup(response.text, 'html.parser')
        date_of_birth = soup.find('span', {'class': 'bday'}).text if soup.find('span', {'class': 'bday'}) else 'N/A'
        date_of_death ='N/A'
        infobox = soup.find('table', {'class': 'infobox biography vcard'})
        if infobox:
            th_elements = infobox.find_all('th')
            for th in th_elements:
                if "died" in th.text.lower():
                    date_of_death = th.find_next('td').text.strip().split('\n')[0].split('[')[0]
        print(f"Birth date: {date_of_birth}\n- Death date: {date_of_death}\n")
