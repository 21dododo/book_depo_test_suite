import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


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
    driver.execute_script("arguments[0].click();", title)
    yield driver
    driver.close()


@pytest.mark.parametrize("book_name", ExampleBooks.BOOKS)
def test_overeview_features(bookpage, book_name):
    driver = bookpage
    correct_title = book_name.lower() in driver.title.lower()
    assert correct_title
    description_table_displayed = driver.find_element(*BookPageLocators.DESCRIPTION_TABLE).is_displayed()
    assert description_table_displayed
    price_displayed = driver.find_element(*BookPageLocators.PRICE).is_displayed()
    assert  price_displayed


