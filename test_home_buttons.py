import pytest
from selenium import webdriver
from locators import *
from selenium.webdriver.common.by import By



def test_bestseller_button(homepage):
    driver = homepage
    driver.find_element(*MainPageLocators.BESTSELLERS_BUTTON).click()
    assert "bestsell" in driver.title.lower()


def test_coming_soon_button(homepage):
    driver = homepage
    driver.find_element(*MainPageLocators.COMING_SOON_BUTTON).click()
    assert "coming soon" in driver.title.lower()


def test_new_releases_button(homepage):
    driver = homepage
    driver.find_element(*MainPageLocators.NEW_RELEASES_BUTTON).click()
    assert "book releases" in driver.title.lower()


def test_contact_us_button(homepage):
    driver = homepage
    driver.find_element(*MainPageLocators.CONTACT_US_BUTTON).click()
    assert "contact us" in driver.title.lower()


def test_help_button(homepage):
    driver = homepage
    driver.find_element(*MainPageLocators.HELP_BUTTON).click()
    assert driver.current_url == "https://www.bookdepository.com/help"


def test_advanced_search_button(homepage):
    driver = homepage
    driver.find_element(*MainPageLocators.ADVANCED_SEARCH_BUTTON).click()
    element_text = driver.find_element_by_class_name("content").find_element_by_tag_name("h1").text
    assert "advanced search" in element_text.lower()


def test_book_logo(homepage):
    driver = homepage
    driver.find_element(*MainPageLocators.BESTSELLERS_BUTTON).click()
    driver.find_element(*MainPageLocators.BOOK_LOGO).click()
    assert "Book Depository: Free delivery worldwide on over 20 million books" == driver.title


def test_home_button(homepage):
    driver = homepage
    driver.find_element(*MainPageLocators.BESTSELLERS_BUTTON).click()
    driver.find_element(*MainPageLocators.HOME_BUTTON).click()
    assert "Book Depository: Free delivery worldwide on over 20 million books" == driver.title







