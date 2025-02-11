from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd

director_dict = {'director_name':[], 'oscars':[], 'height_cm':[]}

url = 'https://www.imdb.com/search/title/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument("--lang=en")
options.add_experimental_option('detach', True)
options.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})
driver = webdriver.Chrome(options = options)
actions = ActionChains(driver)
driver.implicitly_wait(3)
driver.get(url)

drama_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid ="test-chip-id-Drama"]')
actions.move_to_element(drama_button).perform()
drama_button.click()
sleep(1)
awardsMenu = driver.find_element(By.CSS_SELECTOR, 'label[data-testid ="accordion-item-awardsAccordion"]')
actions.move_to_element(awardsMenu).perform()
awardsMenu.click()
sleep(1)
best_director_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="test-chip-id-best-director-winning"]')
actions.move_to_element(best_director_button).perform()
best_director_button.click()

see_results_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid ="adv-search-get-results"]')
actions.move_to_element(see_results_button).perform()
see_results_button.click()

while True:
    sleep(2)
    more_buttons = driver.find_elements(By.CSS_SELECTOR, 'span.ipc-see-more')
    if len(more_buttons) != 0:
        more_button = more_buttons[0]
        actions.move_to_element(more_button).perform()
        more_button.click()
        sleep(1)
    else:
        break
director_links = []

for info_button in driver.find_elements(By.CSS_SELECTOR, 'svg.ipc-icon--info'):
    actions.move_to_element(info_button).perform()
    info_button.click()
    sleep(0.5)
    director_link = driver.find_element(By.CSS_SELECTOR, 'a.clUCBN').get_attribute('href')
    if director_link not in director_links:
        director_links.append(director_link)
        print(director_link)
    close_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Close Prompt"]')
    actions.move_to_element(close_button).perform()
    close_button.click()
    sleep(0.5)

print(len(director_links))
for link in director_links:
    driver.get(link)
    try:
        name = driver.find_element(By.CSS_SELECTOR, 'h1[data-testid="hero__pageTitle"] span[data-testid="hero__primary-text"]').text
    except:
        name = 'N/A'

    oscars = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="See more awards and nominations"]').text

    try:
        height = driver.find_element(By.XPATH, '//span[text()="Height"]/following-sibling::div[1]/ul/li/span').text
    except:
        height = 'N/A'

    director_dict['director_name'].append(name)
    director_dict['oscars'].append(oscars)
    director_dict['height_cm'].append(height)

dft = pd.DataFrame(director_dict)
dft.to_excel('directors.xlsx')
