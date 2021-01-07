import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def spanish_page():
    driver = webdriver.Chrome("chromedriver.exe")
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.bookdepository.com/")
    actions = ActionChains(driver)
    language_btn = driver.find_element_by_partial_link_text("English")
    actions.move_to_element(language_btn).perform()
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Spanish')))
    driver.find_element_by_partial_link_text('Spanish').click()
    return driver

#@pytest.mark.skip
def test_spanish(spanish_page):
    driver = spanish_page
    assert driver.find_element_by_partial_link_text("Los más vendidos").is_displayed()
    driver.close()

#@pytest.mark.skip
def test_return_english(spanish_page):
    driver = spanish_page
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    language_btn = driver.find_element_by_partial_link_text("Español")
    actions.move_to_element(language_btn).perform()
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'English')))
    driver.find_element_by_partial_link_text('English').click()
    assert driver.find_element_by_partial_link_text("Bestsellers").is_displayed()
    driver.close()




