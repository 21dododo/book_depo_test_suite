import pytest
from selenium import webdriver

@pytest.fixture
def homepage():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.bookdepository.com/")
    return driver

#@pytest.mark.skip
def test_bestseller_button(homepage):
    driver = homepage
    driver.find_element_by_partial_link_text("Bestsellers").click()
    assert "bestsell" in driver.title.lower()
    driver.close()

#@pytest.mark.skip
def test_coming_soon_button(homepage):
    driver = homepage
    driver.find_element_by_partial_link_text("Coming Soon").click()
    assert "coming soon" in driver.title.lower()
    driver.close()

#@pytest.mark.skip
def test_new_releases_button(homepage):
    driver = homepage
    driver.find_element_by_partial_link_text("New Releases").click()
    assert "book releases" in driver.title.lower()
    driver.close()

#@pytest.mark.skip
def test_contact_us_button(homepage):
    driver = homepage
    driver.find_element_by_partial_link_text("Contact us").click()
    assert "contact us" in driver.title.lower()
    driver.close()

#@pytest.mark.skip
def test_help_button(homepage):
    driver = homepage
    driver.find_element_by_partial_link_text("Help").click()
    assert driver.current_url == "https://www.bookdepository.com/help"
    driver.close()

#@pytest.mark.skip
def test_advanced_search_button(homepage):
    driver = homepage
    driver.find_element_by_partial_link_text("Advanced Search").click()
    element_text =str (driver.find_element_by_class_name("content").find_element_by_tag_name("h1").text)
    assert "advanced search" in element_text.lower()
    driver.close()

#@pytest.mark.skip
def test_book_logo(homepage):
    driver = homepage
    driver.find_element_by_partial_link_text("Bestsellers").click()
    driver.find_element_by_class_name("brand-link").click()
    assert "Book Depository: Free delivery worldwide on over 20 million books" == driver.title
    driver.close()

#@pytest.mark.skip
def test_home_button(homepage):
    driver = homepage
    driver.find_element_by_partial_link_text("Bestsellers").click()
    driver.find_element_by_class_name("home-icon-link").click()
    assert "Book Depository: Free delivery worldwide on over 20 million books" == driver.title
    driver.close()






