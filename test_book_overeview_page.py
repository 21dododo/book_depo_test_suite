import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = r"C:\drivers\selenium\chromedriver.exe"

@pytest.fixture
@pytest.mark.parametrize("book_name", [("City Of Glass"),("The Wave")])
def bookpage(book_name):
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get("https://www.bookdepository.com/")
    wait = WebDriverWait(driver, 10)
    search_tab = driver.find_element_by_name("searchTerm")
    search_btn = driver.find_element_by_class_name("header-search-btn")
    search_tab.clear()
    search_tab.send_keys(book_name)
    search_btn.click()
    wait.until(EC.title_contains("Results for"))
    title = driver.find_element_by_partial_link_text(book_name)
    driver.execute_script("arguments[0].click();", title)
    return driver



#@pytest.mark.skip
@pytest.mark.parametrize("book_name", [("City Of Glass"),("The Wave")])
def test_title_matches_book(bookpage, book_name):
    driver = bookpage
    assert book_name.lower() in driver.title.lower()
    driver.close()

#@pytest.mark.skip
@pytest.mark.parametrize("book_name", [("City Of Glass"),("The Wave")])
def test_details_table(bookpage, book_name):
    driver = bookpage
    assert driver.find_element_by_class_name("biblio-wrap").is_displayed()
    driver.close()


#@pytest.mark.skip
@pytest.mark.parametrize("book_name", [("City Of Glass"),("The Wave")])
def test_price_displayed(bookpage, book_name):
    driver = bookpage
    assert driver.find_element_by_class_name("sale-price").is_displayed()
    driver.close()