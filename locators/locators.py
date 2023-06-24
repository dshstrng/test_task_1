from selenium.webdriver.common.by import By

# к каждой странице свой класс с локаторами

class LoginPageLocators():
    INPUT_USERNAME = (By.CSS_SELECTOR, "#username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".radius i")
    TEXT_MESSAGE = (By.CSS_SELECTOR, "#flash")

class KeyPressesLocators():
    INPUT_FRAME = (By.CSS_SELECTOR, "input#target")
    TEXT_RESULT = (By.CSS_SELECTOR, "#result")

class DropdownListLocators():
    LIST_DROPDOWN = (By.ID, "dropdown")
    OPTIONS = (By.TAG_NAME, "option")
    
class DownloadLocators():
    LINK_DOWNLOAD = (By.LINK_TEXT, "some-file.txt")
    