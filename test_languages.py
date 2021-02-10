import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def test_spanish(spanish_page):
    driver = spanish_page
    assert driver.find_element_by_partial_link_text("Los más vendidos").is_displayed()


def test_return_english(spanish_page):
    driver = spanish_page
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    language_btn = driver.find_element(*SpanishPage.LANGUAGE_BUTTON)
    actions.move_to_element(language_btn).perform()
    wait.until(EC.element_to_be_clickable(SpanishPage.ENGLISH_BUTTON))
    driver.find_element_by_partial_link_text('English').click()
    assert driver.find_element_by_partial_link_text("Bestsellers").is_displayed()





