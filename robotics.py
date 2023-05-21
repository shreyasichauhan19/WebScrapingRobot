from RPA.Browser.Selenium import Selenium
from bs4 import BeautifulSoup
import time
import requests
import re
from datetime import datetime


br = Selenium()


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name} :D and I love science. I think scientists are cool and I love learning about them. I thought I would share some of that information with you, beep boop." )
        print("After you hit run, I will open a web browser, browse wikipedia for the scientist's info, scrap it, do some more magic and print thier informaion on your console.")
    
    def say_goodbye(self):
        print(f"Beep boop... beep boop {self.name} is signing off")

    def open_webpage(self, webpage):
        br.open_available_browser(webpage)

    def data_scraping(self, webpage):
        self.open_webpage(webpage)
        time.sleep(2)  # Allow the page to load
        response = requests.get(webpage)
        soup = BeautifulSoup(response.text, 'html.parser')
        first_paragraph = soup.select_one('div.mw-parser-output > p:not(.mw-empty-elt)').text
        date_of_birth = soup.find('span', {'class': 'bday'}).text if soup.find('span', {'class': 'bday'}) else 'N/A'
        date_of_death = 'N/A'
        infobox = soup.find('table', {'class': 'infobox biography vcard'})
        if infobox:
            th_elements = infobox.find_all('th')
            for th in th_elements:
                if "died" in th.text.lower():
                    date_of_death = th.find_next('td').text.strip().split('\n')[0].split('[')[0]
                    death_data_string = date_of_death
                    match = re.search(r'\((.*?)\)', death_data_string)
                    if match:
                        death_date = match.group(1)
                    bday = datetime.strptime(date_of_birth, '%Y-%m-%d')
                    dday = datetime.strptime(death_date, '%Y-%m-%d')
                    age_at_death = int((dday - bday).days / 365.25)  # Using 365.25 to account for leap years
                    
        print(first_paragraph)
        print(f"Date of Birth: {date_of_birth}")
        print(f"Date of Death: {death_date}")
        print(f"Age at Death: {age_at_death}")