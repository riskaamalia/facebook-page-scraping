from selenium.webdriver.common.keys import Keys
from util import loggerConfig
logger = loggerConfig.setConfig()


def login (driver) :
    # username and password in facebook
    usr="susisusanti1234"
    pwd="SusiSusanti1234"

    # log in to facebook first
    driver.get("http://www.facebook.com")

    # element for log in
    assert "Facebook" in driver.title
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)

    # try to log in
    try:
        elem = driver.find_element_by_css_selector(".input.textInput")
        elem.send_keys("Posted using Python's Selenium WebDriver bindings!")
        elem = driver.find_element_by_css_selector("input[value=\"Publicar\"]")
        elem.click()
    except (Exception) :
        logger.info('Exception, I do not know')