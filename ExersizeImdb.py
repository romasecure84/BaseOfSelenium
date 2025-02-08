from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd

def scroll_to_bottom():
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(1)
movie_dict = {'movie_name':[], 'year':[], 'duration':[], 'stars':[], 'votes':[], 'Meta score':[],'description':[]}

url = 'https://www.imdb.com/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument("--lang=en")
options.add_experimental_option('detach', True)
options.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})
driver = webdriver.Chrome(options = options)
actions = ActionChains(driver)
driver.implicitly_wait(1)
driver.get(url)

search_button = driver.find_element(By.ID,'suggestion-search-button')
search_button.click()
sleep(1)
movies_tv = driver.find_element(By.CSS_SELECTOR, 'a[data-testid ="advanced-search-chip-tt"]')
movies_tv.click()
sleep(1)
movie = driver.find_element(By.CSS_SELECTOR, 'button[data-testid ="test-chip-id-movie"]')
movie.click()
sleep(1)
comedy = driver.find_element(By.CSS_SELECTOR, 'button[data-testid ="test-chip-id-Comedy"]')
actions.move_to_element(comedy).perform()
comedy.click()
sleep(1)
awardsMenu = driver.find_element(By.CSS_SELECTOR, 'label[data-testid ="accordion-item-awardsAccordion"]')
actions.move_to_element(awardsMenu).perform()
awardsMenu.click()
sleep(1)
oscarNominated = driver.find_element(By.CSS_SELECTOR, 'button[data-testid ="test-chip-id-oscar-nominated"]')
actions.move_to_element(oscarNominated).perform()
oscarNominated.click()
sleep(1)
resultsButton = driver.find_element(By.CSS_SELECTOR, 'button[data-testid ="adv-search-get-results"]')
resultsButton.click()

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

movies = driver.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')

for movie in movies:
    raw_name = movie.find_element(By.CSS_SELECTOR, 'h3.ipc-title__text').text
    name = ' '.join(raw_name.split(' ')[1:])
    movie_dict['movie_name'].append(name)

    year_duration = movie.find_elements(By.CSS_SELECTOR, 'span.dli-title-metadata-item')
    year = year_duration[0].text
    movie_dict['year'].append(year)
    duration = year_duration[1].text
    movie_dict['duration'].append(duration)

    stars = movie.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--rating').text
    movie_dict['stars'].append(stars)

    votes = movie.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--voteCount').text.strip()[1:-1]
    movie_dict['votes'].append(votes)

    try:
        meta_score = movie.find_element(By.CSS_SELECTOR, 'span.metacritic-score-box').text
        movie_dict['Meta score'].append(meta_score)
    except:
        movie_dict['Meta score'].append('N/A')

    description = movie.find_element(By.CSS_SELECTOR, 'div.ipc-html-content-inner-div').text
    movie_dict['description'].append(description)

    df = pd.DataFrame(movie_dict)
    df.to_excel('movies.xlsx')