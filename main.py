from selenium import webdriver

url = 'https://quotes.toscrape.com/js/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = options)
driver.get(url)