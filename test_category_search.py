import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

DRIVER_PATH = r"C:\drivers\selenium\chromedriver.exe"

@pytest.fixture
def homepage():
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get("https://www.bookdepository.com/")
    return driver

#@pytest.mark.skip
def test_top_categories(homepage):
    driver = homepage
    actions = ActionChains(driver)
    shop_by_cat = driver.find_element_by_partial_link_text("Shop by category")
    art_and_photo = driver.find_element_by_partial_link_text("Art & Photography")
    actions.move_to_element(shop_by_cat).move_to_element(art_and_photo).click().perform()
    assert "art & photography" in driver.title.lower()
    driver.close()

#@pytest.mark.skip
def test_more_categories(homepage):
    driver = homepage
    actions = ActionChains(driver)
    shop_by_cat = driver.find_element_by_partial_link_text("Shop by category")
    audio_books = driver.find_element_by_xpath('//a[@href="/category/3389/Audio-Books"]')
    actions.move_to_element(shop_by_cat).move_to_element(audio_books).click().perform()
    assert "audio books" in driver.title.lower()
    driver.close()

#@pytest.mark.skip
def test_top_authors(homepage):
    driver = homepage
    actions = ActionChains(driver)
    shop_by_cat = driver.find_element_by_partial_link_text("Shop by category")
    jk_rowling = driver.find_element_by_xpath('//a[@href="/author/J-K-Rowling"]')
    actions.move_to_element(shop_by_cat).move_to_element(jk_rowling).click().perform()
    assert "j k rowling" in driver.title.lower()
    driver.close()

#@pytest.mark.skip
def test_bestselling_series(homepage):
    driver = homepage
    actions = ActionChains(driver)
    shop_by_cat = driver.find_element_by_partial_link_text("Shop by category")
    harry_potter = driver.find_element_by_xpath('//a[@href="/harry-potter"]')
    actions.move_to_element(shop_by_cat).move_to_element(harry_potter).click().perform()
    assert "harry potter" in driver.title.lower()
    driver.close()

#@pytest.mark.skip
def test_popular_features(homepage):
    driver = homepage
    actions = ActionChains(driver)
    shop_by_cat = driver.find_element_by_partial_link_text("Shop by category")
    home_learn = driver.find_element_by_xpath('//a[@href="/home-learning"]')
    actions.move_to_element(shop_by_cat).move_to_element(home_learn).click().perform()
    assert "home learning" in driver.title.lower()
    driver.close()

