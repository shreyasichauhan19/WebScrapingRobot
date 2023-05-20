from selenium import webdriver
import time

def open_wikipedia_pages(titles):
    # Instantiate the web driver
    driver = webdriver.Chrome()

    # Iterate over the list of scientist names
    for title in titles:
        # Create the Wikipedia URL
        url = 'https://en.wikipedia.org/wiki/' + title.replace(' ', '_')

        # Open the URL in a new tab
        driver.get(url)

        # wait time before opening the next page
        time.sleep(2)

    # Wait for the user to hit Enter before ending the script, without this the driver just shuts down automatically
    input("Press Enter to close the browser...")

    driver.quit()

# List of scientist names
SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

# Call the function with the list of names
open_wikipedia_pages(SCIENTISTS)
