import pytest
from selenium import webdriver
from locators import *
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("book_name", ExampleBooks.BOOKS)
def test_existing_book_advanced(advanced_page, book_name):
    driver = advanced_page
    title = driver.find_element(*AdvancedSearchLocators.TITLE_TAB)
    title.clear()
    title.send_keys(book_name)
    search_btn = driver.find_element(*AdvancedSearchLocators.SEARCH_BUTTON)
    search_btn.click()
    books = driver.find_elements_by_class_name("book-item")
    found_title = False
    for book in books:
        book_title = book.find_element_by_class_name("title").text
        if book_name.lower() in (book_title).lower():
            found_title = True
            break
    assert found_title


def test_search_empty_fields(advanced_page):
    driver = advanced_page
    search_btn = driver.find_element(*AdvancedSearchLocators.SEARCH_BUTTON)
    search_btn.click()
    #checks that we did not move from the advanced search page when searching with all fields empty
    element_text = driver.find_element_by_class_name("content").find_element_by_tag_name("h1").text
    assert "advanced search" in element_text.lower()


def test_non_existing_book_advanced(advanced_page):
    driver = advanced_page
    title = driver.find_element(*AdvancedSearchLocators.TITLE_TAB)
    title.clear()
    title.send_keys("MMMM1234")
    search_btn = driver.find_element(*AdvancedSearchLocators.SEARCH_BUTTON)
    search_btn.click()
    # checks that we did not move from the advanced search page when searching a non existing book
    element_text = driver.find_element_by_class_name("content").find_element_by_tag_name("h1").text
    assert "advanced search" in element_text.lower()


def test_existing_book_wrong_author(advanced_page):
    driver = advanced_page
    title = driver.find_element(*AdvancedSearchLocators.TITLE_TAB)
    title.clear()
    title.send_keys("City Of Glass")
    author = driver.find_element(*AdvancedSearchLocators.AUTHOR_TAB)
    author.clear()
    author.send_keys("J K Rowling")
    search_btn = driver.find_element(*AdvancedSearchLocators.SEARCH_BUTTON)
    search_btn.click()
    element_text = driver.find_element_by_class_name("content").find_element_by_tag_name("h1").text
    assert "advanced search" in element_text.lower()


@pytest.mark.parametrize("book_with_author", ExampleBooks.BOOKS_WITH_AUTHORS)
def test_existing_book_correct_author(advanced_page, book_with_author):
    driver = advanced_page
    title = driver.find_element(*AdvancedSearchLocators.TITLE_TAB)
    title.clear()
    title.send_keys(book_with_author[0])
    author = driver.find_element(*AdvancedSearchLocators.AUTHOR_TAB)
    author.clear()
    author.send_keys(book_with_author[1])
    search_btn = driver.find_element(*AdvancedSearchLocators.SEARCH_BUTTON)
    search_btn.click()
    books = driver.find_elements_by_class_name("book-item")
    found_title = False
    for book in books:
        book_title = book.find_element_by_class_name("title").text
        if book_with_author[0].lower() in (book_title).lower():
            found_title = True
            break
    assert found_title


def test_existing_book_all_tabs_correct(advanced_page):
    driver = advanced_page
    title = driver.find_element(*AdvancedSearchLocators.TITLE_TAB)
    title.clear()
    title.send_keys("City of Glass")
    author = driver.find_element(*AdvancedSearchLocators.AUTHOR_TAB)
    author.clear()
    author.send_keys("Cassandra Clare")
    keyword = driver.find_element(*AdvancedSearchLocators.KEYWORD_TAB)
    keyword.send_keys("city of glass")
    publisher = driver.find_element(*AdvancedSearchLocators.PUBLISHER_TAB)
    publisher.clear()
    publisher.send_keys("Walker Books Ltd")
    #click english language
    driver.find_element(By.XPATH, '//*[@id="filterLang"]/option[2]').click()
    search_btn = driver.find_element(*AdvancedSearchLocators.SEARCH_BUTTON)
    search_btn.click()
    books = driver.find_elements_by_class_name("book-item")
    found_title = False
    for book in books:
        book_title = book.find_element_by_class_name("title").text
        if "city of glass" in (book_title).lower():
            found_title = True
            break
    assert found_title








