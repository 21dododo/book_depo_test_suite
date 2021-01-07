import pytest
from selenium import webdriver

DRIVER_PATH = r"C:\drivers\selenium\chromedriver.exe"

@pytest.fixture
def advanced_page():
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get("https://www.bookdepository.com/search/advanced")
    return driver

#@pytest.mark.skip
@pytest.mark.parametrize("book_name", [("City Of Glass"), ("The Wave")])
def test_existing_book(advanced_page, book_name):
    driver = advanced_page
    title = driver.find_element_by_name("searchTitle")
    title.clear()
    title.send_keys(book_name)
    search_btn = driver.find_element_by_xpath('//button[text()="Search"]')
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
def test_search_empty_fields(advanced_page):
    driver = advanced_page
    search_btn = driver.find_element_by_xpath('//button[text()="Search"]')
    search_btn.click()
    element_text = str(driver.find_element_by_class_name("content").find_element_by_tag_name("h1").text)
    assert "advanced search" in element_text.lower()
    driver.close()

#@pytest.mark.skip
def test_non_existing_book(advanced_page):
    driver = advanced_page
    title = driver.find_element_by_name("searchTitle")
    title.clear()
    title.send_keys("MMMM1234")
    search_btn = driver.find_element_by_xpath('//button[text()="Search"]')
    search_btn.click()
    element_text = str(driver.find_element_by_class_name("content").find_element_by_tag_name("h1").text)
    assert "advanced search" in element_text.lower()
    driver.close()

#@pytest.mark.skip
def test_non_existing_book(advanced_page):
    driver = advanced_page
    title = driver.find_element_by_name("searchTitle")
    title.clear()
    title.send_keys("City Of Glass")
    author = driver.find_element_by_name("searchAuthor")
    author.clear()
    author.send_keys("J K Rowling")
    search_btn = driver.find_element_by_xpath('//button[text()="Search"]')
    search_btn.click()
    element_text = str(driver.find_element_by_class_name("content").find_element_by_tag_name("h1").text)
    assert "advanced search" in element_text.lower()
    driver.close()




