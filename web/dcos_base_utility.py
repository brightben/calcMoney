""" Class for DCOSBaseUtility """
import logging
import json
from selenium import webdriver
from gui_pages.dcos_dashboard_page import DCOSDashboardPage
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from testcase_utility import load_driver

logger = logging.getLogger(__name__)

with open('conf/config.json', 'r') as f:
    try:
        CONFIG = json.load(f)
    except IOError:
        logger.critical('Opening file error, config file not found')
        exit(1)
    except ValueError:
        logger.critical('Decoding Config JSON failed')
        exit(1)

class DCOSBaseUtility(object):
    """ Class for DCOSBaseUtility """

    @classmethod
    def delete_dcos_service(cls, service_name):
        """ delete dcos service """
        driver = load_driver()
        dashboard_page = DCOSDashboardPage(driver, url_prefix=CONFIG['DCOS_DASHBOARD_URL'])
        service_page = dashboard_page.go_service_page()
        if service_page.is_service_exist_by_name(service_name):
            service_detail_page = service_page.go_service_detail_by_name(service_name)
            service_detail_page.delete_service()
            logger.info('"'+service_name+'" has been deleted')
        else:
            logger.info('"'+service_name+'" is on here yet')
        driver.quit()

    @classmethod
    def check_dcos_service(cls, service_name):
        """ check service is created in dcos """
        driver = load_driver()
        dashboard_page = DCOSDashboardPage(driver, url_prefix=CONFIG['DCOS_DASHBOARD_URL'])
        service_page = dashboard_page.go_service_page()
        befound = False
        if service_page.is_service_exist_by_name(service_name):
            logger.info('"'+service_name+'" is found')
            befound = True
        else:
            logger.info('"'+service_name+'" was not found')
        driver.quit()
        return befound

    @classmethod
    def check_dcos_resource(cls):
        """ check and copy dcos resource """
        driver = load_driver()
        data_temp = {}
        dcos_page = DCOSDashboardPage(driver, url_prefix=CONFIG['DCOS_DASHBOARD_URL'])
        dcos_page.navigate()
        data_temp['cpu_allocation_usage'] = dcos_page.get_cpu_allocation_usage()
        data_temp['cpu_allocation_percentage'] = dcos_page.get_cpu_allocation_percentage()
        data_temp['memory_allocation_usage'] = dcos_page.get_mem_allocation_usage()
        data_temp['memory_allocation_percentage'] = dcos_page.get_mem_allocation_percentage()
        data_temp['disk_allocation_usage'] = dcos_page.get_disk_allocation_usage()
        data_temp['disk_allocation_percentage'] = dcos_page.get_disk_allocation_percentage()
        driver.quit()
        return data_temp

    @classmethod
    def print_usage_data(cls, data):
        """ Print data """
        logger.info('++++++++++++++++++++++++++++++++++++++++++')
        logger.info('CPU : ')
        logger.info('\tusage      : '+data.get('cpu_allocation_usage'))
        logger.info('\tpercentage : '+data.get('cpu_allocation_percentage')+"%")
        logger.info('MEMORY : ')
        logger.info('\tusage      : '+data.get('memory_allocation_usage'))
        logger.info('\tpercentage : '+data.get('memory_allocation_percentage') +"%")
        logger.info('DISK : ')
        logger.info('\tusage      : '+data.get('disk_allocation_usage'))
        logger.info('\tpercentage : '+data.get('disk_allocation_percentage')+"%")
        logger.info('++++++++++++++++++++++++++++++++++++++++++')
