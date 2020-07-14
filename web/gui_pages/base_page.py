""" BasePage Classes """
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage(object):
    """ The basic page parent class """
    url = ''
    timeout = 10
    instance_launch_time = 600
    def __init__(self, driver, url_prefix=None, url_suffix=None):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        if url_prefix is not None:
            self.url = url_prefix + self.url
            self.url_prefix = url_prefix

        if url_suffix is not None:
            self.url = self.url + url_suffix
            self.url_suffix = url_suffix

    def fill_form(self, form_xpath, value):
        """ Find the element by css selector and send key to the element"""
        self.fill_form_by_index(form_xpath, 0, value)

    def fill_form_by_index(self, form_xpath, index, value):
        """ Find the element by css selector and send key to the element"""
        try:
            element = self.driver.find_elements(By.XPATH, form_xpath)[index]
            element.clear()
            element.send_keys(value)
        except NoSuchElementException:
            self.quit_driver()

    def navigate(self):
        """ Go the the page """
        self.driver.get(self.url)

    def click_element(self, form_xpath):
        """ Find the element by xpath, scroll to it and click it """
        try:
            element = self.driver.find_element_by_xpath(form_xpath)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element.click()
        except NoSuchElementException:
            self.logger.error("No such xpath.")
            self.logger.error("Target xpath = " + form_xpath)
            self.quit_driver()

    def wait_element_located(self, wait_time_limit, form_xpath):
        """ Wait for the element located """
        try:
            WebDriverWait(self.driver, wait_time_limit).until(
                EC.presence_of_element_located((By.XPATH, form_xpath))
            )
        except TimeoutException:
            self.logger.error("Wait element located timeout(10s).")
            self.logger.error("Target xpath = " + form_xpath)
            self.quit_driver()

    def wait_element_visible(self, wait_time_limit, form_xpath):
        """ Wait for the element visible in browser """
        try:
            WebDriverWait(self.driver, wait_time_limit).until(
                EC.visibility_of_element_located((By.XPATH, form_xpath))
            )
        except TimeoutException:
            self.quit_driver()

    def get_element_count(self, form_xpath):
        """ get the same element count """
        return len(self.driver.find_elements_by_xpath(form_xpath))


    def get_element_text(self, form_xpath):
        """ get element text """
        try:
            element = self.driver.find_element_by_xpath(form_xpath)
        except NoSuchElementException:
            return None
        return str(element.text)

    def is_element_exist(self, form_xpath):
        """ Check if the element exists"""
        try:
            self.driver.find_element_by_xpath(form_xpath)
            return True
        except NoSuchElementException:
            return False

    def wait_element_clickable(self, wait_time_limit, form_xpath):
        """ Wait for the element clickable """
        try:
            WebDriverWait(self.driver, wait_time_limit).until(
                EC.element_to_be_clickable((By.XPATH, form_xpath))
            )
        except TimeoutException:
            self.quit_driver()

    def set_url(self, url):
        """ Set url """
        self.url = url

    def close_page(self):
        """ close the browser """
        self.driver.close()

    def quit_driver(self):
        """ quit the driver """
        self.driver.quit()

    def refresh_page(self):
        """ refresh the current url page """
        self.driver.refresh()

    def print_page(self):
        """ print the current url page html """
        self.logger.info(self.driver.page_source)

    def screenshot(self, file_name):
        """ capture web page snapshot """
        self.driver.save_screenshot(file_name)
