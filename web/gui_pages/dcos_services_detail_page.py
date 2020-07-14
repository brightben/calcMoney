""" DCOS services detail page class """
from gui_pages.base_page import BasePage

class DCOSServicesDetailPage(BasePage):
    """ DCOS services detail page """

    def delete_service(self):
        """ Delete service """
        self.wait_element_located(self.timeout, '//button[contains(@class,"dropdown-toggle")]')
        self.click_element('//button[contains(@class,"dropdown-toggle")]')
        self.wait_element_located(self.timeout, '//span[contains(text(),"Destroy")]')
        self.click_element('//span[contains(text(),"Destroy")]')
        self.wait_element_located(self.timeout, '//button[contains(@class,"button-danger")]')
        self.click_element('//button[contains(@class,"button-danger")]')
