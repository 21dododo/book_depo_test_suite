import pytest
from selenium import webdriver
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

@pytest.fixture
def homepage():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.bookdepository.com/")
    yield driver
    driver.close()


@pytest.fixture
def advanced_page():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.bookdepository.com/search/advanced")
    yield driver
    driver.close()


@pytest.fixture
@pytest.mark.parametrize("book_name", ExampleBooks.BOOKS)
def bookpage(book_name):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.bookdepository.com/")
    wait = WebDriverWait(driver, 10)
    search_tab = driver.find_element(*MainPageLocators.SEARCH_TAB)
    search_btn = driver.find_element(*MainPageLocators.SEARCH_BUTTON)
    search_tab.clear()
    search_tab.send_keys(book_name)
    search_btn.click()
    wait.until(EC.title_contains("Results for"))
    title = driver.find_element_by_partial_link_text(book_name)
    # we used execute script to not be intercepted by another element
    driver.execute_script("arguments[0].click();", title)
    yield driver
    driver.close()

@pytest.fixture
def spanish_page():
    driver = webdriver.Chrome("chromedriver.exe")
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.bookdepository.com/")
    actions = ActionChains(driver)
    language_btn = driver.find_element(*MainPageLocators.LANGUAGE_BUTTON)
    actions.move_to_element(language_btn).perform()
    wait.until(EC.element_to_be_clickable(MainPageLocators.SPANISH_BUTTON))
    driver.find_element(*MainPageLocators.SPANISH_BUTTON).click()
    yield driver
    driver.close()
