""" DCOS dashboard class """
from gui_pages.base_page import BasePage
from gui_pages.dcos_services_page import DCOSServicesPage

class DCOSDashboardPage(BasePage):
    """ DCOS dashboard page """

    def go_service_page(self):
        """ go to service page """
        page = DCOSServicesPage(self.driver, url_prefix=self.url)
        page.navigate()
        return page

    def get_cpu_allocation_usage(self):
        """ get cpu allocation on page """
        self.wait_element_located(self.timeout, '//div[@data-reactid=".0.0.2.1.2"]')
        return self.get_element_text('//span[@data-reactid=".0.0.2.1.2.0.0.0.0.1.0.0.1"]')

    def get_cpu_allocation_percentage(self):
        """ get cpu allocation percentage on page """
        self.wait_element_located(self.timeout, '//div[@data-reactid=".0.0.2.1.2"]')
        return self.get_element_text('//span[@data-reactid=".0.0.2.1.2.0.0.0.0.1.0.0.0.0"]')

    def get_mem_allocation_usage(self):
        """ get memory allocation on page """
        self.wait_element_located(self.timeout, '//div[@data-reactid=".0.0.2.1.2"]')
        return self.get_element_text('//span[@data-reactid=".0.0.2.1.2.0.0.1.0.1.0.0.1"]')

    def get_mem_allocation_percentage(self):
        """ get memory allocation percentage on page """
        self.wait_element_located(self.timeout, '//div[@data-reactid=".0.0.2.1.2"]')
        return self.get_element_text('//span[@data-reactid=".0.0.2.1.2.0.0.1.0.1.0.0.0.0"]')

    def get_disk_allocation_usage(self):
        """ get disk allocation on page """
        self.wait_element_located(self.timeout, '//div[@data-reactid=".0.0.2.1.2"]')
        return self.get_element_text('//span[@data-reactid=".0.0.2.1.2.0.0.2.0.1.0.0.1"]')

    def get_disk_allocation_percentage(self):
        """ get disk allocation percentage on page """
        self.wait_element_located(self.timeout, '//div[@data-reactid=".0.0.2.1.2"]')
        return self.get_element_text('//span[@data-reactid=".0.0.2.1.2.0.0.2.0.1.0.0.0.0"]')
