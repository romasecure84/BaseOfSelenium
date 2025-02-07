from selenium import webdriver
from selenium.webdriver.common.by import By
from LoginWithSelenium import login


def scrape_page(the_driver):
    quotes = driver.find_elements(By.CLASS_NAME, 'quote')
    for element in quotes:

        quote = element.find_element(By.CLASS_NAME, 'text')
        print(quote.text)

        author = element.find_element(By.CLASS_NAME, 'author')
        print(author.text)

        tag_container = element.find_element(By.CLASS_NAME, 'tags')
        a_tags = tag_container.find_elements(By.CSS_SELECTOR, 'a')
        tags = ''
        for i, a_tag in enumerate(a_tags):
            if i == len(a_tags) - 1:
                tag = a_tag.text
            else:
                tag = a_tag.text + ", "
            tags += tag
        print(tags)
        print('\n')

url = 'https://quotes.toscrape.com/js/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = options)
driver.get(url)

login(driver)

scrape_page(driver)
