import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *


@pytest.fixture
def homepage():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.bookdepository.com/")
    return driver

#@pytest.mark.skip
@pytest.mark.parametrize("book_name", [("City Of Glass"),("The Wave")])
def test_search_existing_book(homepage, book_name):
    driver = homepage
    search_tab = driver.find_element(*MainPageLocators.SEARCH_TAB)
    search_btn = driver.find_element(*MainPageLocators.SEARCH_BUTTON)
    search_tab.clear()
    search_tab.send_keys(book_name)
    search_btn.click()
    books = driver.find_elements_by_class_name("book-item")
    found_title = False
    for book in books:
        book = book.find_element_by_class_name("title")
        if book_name.lower() in str(book.text).lower():
            found_title = True
            break
    assert found_title
    driver.close()

#@pytest.mark.skip
def test_press_empty(homepage):
    driver = homepage
    search_btn = driver.find_element(*MainPageLocators.SEARCH_BUTTON)
    search_btn.click()
    element_text = str(driver.find_element_by_class_name("content").find_element_by_tag_name("h1").text)
    assert "advanced search" in element_text.lower()
    driver.close()

#@pytest.mark.skip
def test_search_non_existing_book(homepage):
    driver = homepage
    search_tab = driver.find_element(*MainPageLocators.SEARCH_TAB)
    search_btn = driver.find_element(*MainPageLocators.SEARCH_BUTTON)
    search_tab.clear()
    search_tab.send_keys("MMMM1234")
    search_btn.click()
    element_text = str(driver.find_element_by_class_name("content").find_element_by_tag_name("h1").text)
    assert "advanced search" in element_text.lower()
    driver.close()




