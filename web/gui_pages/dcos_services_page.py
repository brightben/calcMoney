""" DCOS services page class """
from gui_pages.base_page import BasePage
from gui_pages.dcos_services_detail_page import DCOSServicesDetailPage

class DCOSServicesPage(BasePage):
    """ DCOS services page """
    url = '/#/services/'

    def go_service_detail_by_name(self, service_name):
        """ go to service detail """
        search_element = '//span[@class="text-overflow"][contains(text(),"'+service_name+'")]'
        self.wait_element_located(self.timeout, search_element)
        self.click_element(search_element)
        page = DCOSServicesDetailPage(self.driver, url_prefix=self.url+'%2F'+service_name+'/')
        return page

    def is_service_exist_by_name(self, service_name):
        """ check if service xxx is in DC/OS service page """
        search_element = '//span[@class="text-overflow"][contains(text(),"'+service_name+'")]'
        self.wait_element_located(self.timeout, '//a[@href="#/services/"]')
        return self.is_element_exist(search_element)
