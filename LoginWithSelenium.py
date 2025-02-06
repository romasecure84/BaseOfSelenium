from selenium import webdriver
from selenium.webdriver.common.by import By


def login(the_driver):
    login_button = the_driver.find_element(By.XPATH, '//a[text()="Login"]')
    login_button.click()

    username_shield = the_driver.find_element(By.ID, 'username')
    username_shield.send_keys('userName')

    password_shield = the_driver.find_element(By.ID, 'password')
    password_shield.send_keys('password')

    login_button_submit = the_driver.find_element(By.XPATH, '//input[@type="submit"]')
    login_button_submit.click()

url = 'https://quotes.toscrape.com/js/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = options)
driver.get(url)

login(driver)