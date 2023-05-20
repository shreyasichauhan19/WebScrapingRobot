from selenium import webdriver
from bs4 import BeautifulSoup
import time

# List of scientist names
SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

def get_wikipedia_url(title):
    """Create and return the Wikipedia URL for the given title."""
    return 'https://en.wikipedia.org/wiki/' + title.replace(' ', '_')

def fetch_page_source(driver, url):
    """Fetch the page source using the driver and return a BeautifulSoup object."""
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    return BeautifulSoup(driver.page_source, 'lxml')

def extract_birth_date(soup):
    """Extract and return the birth date from the BeautifulSoup object."""
    return soup.find('span', {'class': 'bday'}).text if soup.find('span', {'class': 'bday'}) else 'N/A'

def main(titles):
    # Instantiate the web driver
    driver = webdriver.Chrome()

    # Iterate over the list of scientist names
    for title in titles:
        # Create the Wikipedia URL
        url = get_wikipedia_url(title)

        # Fetch the page content
        soup = fetch_page_source(driver, url)

        # Extract the birth date
        birth_date = extract_birth_date(soup)

        print(f"{title}:\n- Birth date: {birth_date}\n")

    # Wait for the user to hit Enter before ending the script, without this the driver just shuts down automatically
    input("Press Enter to close the browser...")
    driver.quit()

# Call the main function with the list of names
if __name__ == "__main__":
    main(SCIENTISTS)
