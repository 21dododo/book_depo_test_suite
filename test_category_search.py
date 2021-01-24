import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from locators import *


@pytest.fixture
def homepage():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.bookdepository.com/")
    yield driver
    driver.close()


def test_top_categories(homepage):
    driver = homepage
    actions = ActionChains(driver)
    shop_by_cat = driver.find_element_by_partial_link_text("Shop by category")
    art_and_photo = driver.find_element(*CategoryLocators.ART_AND_PHOTO)
    actions.move_to_element(shop_by_cat).move_to_element(art_and_photo).click().perform()
    assert "art & photography" in driver.title.lower()


def test_more_categories(homepage):
    driver = homepage
    actions = ActionChains(driver)
    shop_by_cat = driver.find_element_by_partial_link_text("Shop by category")
    audio_books = driver.find_element(*CategoryLocators.AUDIO_BOOKS)
    actions.move_to_element(shop_by_cat).move_to_element(audio_books).click().perform()
    assert "audio books" in driver.title.lower()


def test_top_authors(homepage):
    driver = homepage
    actions = ActionChains(driver)
    shop_by_cat = driver.find_element_by_partial_link_text("Shop by category")
    jk_rowling = driver.find_element(*CategoryLocators.JK_ROWLING)
    actions.move_to_element(shop_by_cat).move_to_element(jk_rowling).click().perform()
    assert "j k rowling" in driver.title.lower()


def test_bestselling_series(homepage):
    driver = homepage
    actions = ActionChains(driver)
    shop_by_cat = driver.find_element_by_partial_link_text("Shop by category")
    harry_potter = driver.find_element(*CategoryLocators.HARRY_POTTER)
    actions.move_to_element(shop_by_cat).move_to_element(harry_potter).click().perform()
    assert "harry potter" in driver.title.lower()


def test_popular_features(homepage):
    driver = homepage
    actions = ActionChains(driver)
    shop_by_cat = driver.find_element_by_partial_link_text("Shop by category")
    home_learn = driver.find_element(*CategoryLocators.HOME_LEARNING)
    actions.move_to_element(shop_by_cat).move_to_element(home_learn).click().perform()
    assert "home learning" in driver.title.lower()


