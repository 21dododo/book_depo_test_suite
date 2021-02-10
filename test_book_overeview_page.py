import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *





@pytest.mark.parametrize("book_name", ExampleBooks.BOOKS)
def test_overeview_features(bookpage, book_name):
    driver = bookpage
    correct_title = book_name.lower() in driver.title.lower()
    assert correct_title
    description_table_displayed = driver.find_element(*BookPageLocators.DESCRIPTION_TABLE).is_displayed()
    assert description_table_displayed
    price_displayed = driver.find_element(*BookPageLocators.PRICE).is_displayed()
    assert  price_displayed


