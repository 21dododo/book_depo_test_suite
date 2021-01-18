from selenium.webdriver.common.by import By

class MainPageLocators(object):
    BESTSELLERS_BUTTON = (By.PARTIAL_LINK_TEXT, "Bestsellers")
    COMING_SOON_BUTTON = (By.PARTIAL_LINK_TEXT, "Coming Soon")
    NEW_RELEASES_BUTTON = (By.PARTIAL_LINK_TEXT, "New Releases")
    CONTACT_US_BUTTON = (By.PARTIAL_LINK_TEXT, "Contact us")
    HELP_BUTTON = (By.PARTIAL_LINK_TEXT, "Help")
    ADVANCED_SEARCH_BUTTON = (By.PARTIAL_LINK_TEXT, "Advanced Search")
    BOOK_LOGO = (By.CLASS_NAME, "brand-link")
    HOME_BUTTON = (By.CLASS_NAME, "home-icon-link")
    SEARCH_TAB =(By.NAME, "searchTerm")
    SEARCH_BUTTON = (By.CLASS_NAME, "header-search-btn")
    LANGUAGE_BUTTON = (By.PARTIAL_LINK_TEXT, "English")
    SPANISH_BUTTON = (By.PARTIAL_LINK_TEXT, "Spanish")

class CategoryLocators(object):
    ART_AND_PHOTO = (By.XPATH, '//a[@href="/category/2/Art-Photography"]')
    AUDIO_BOOKS = (By.XPATH, '//a[@href="/category/3389/Audio-Books"]')
    JK_ROWLING = (By.XPATH, '//a[@href="/author/J-K-Rowling"]')
    HARRY_POTTER = (By.XPATH, '//a[@href="/harry-potter"]')
    HOME_LEARNING = (By.XPATH, '//a[@href="/home-learning"]')

class AdvancedSearchLocators(object):
    TITLE_TAB = (By.NAME, "searchTitle")
    SEARCH_BUTTON = (By.XPATH, '//button[text()="Search"]')

class BookPageLocators(object):
    DESCRIPTION_TABLE = (By.CLASS_NAME, "biblio-wrap")
    PRICE = (By.CLASS_NAME, "sale-price")

class SpanishPage(object):
    LANGUAGE_BUTTON = (By.PARTIAL_LINK_TEXT, "Español")
    ENGLISH_BUTTON = (By.PARTIAL_LINK_TEXT, "English")
