""" Class for DCOS test case """
import unittest
import sys
import logging
import logging_utility
import json
import time
from testcase_utility import (load_driver, get_url_title_on_web)
from marathon_utility import list_app
from config_struct import ServiceConfigData

logging_utility.basicConfig(
    stream=sys.stdout,
    format='%(levelname)-8s %(asctime)s %(name)s:%(lineno)d| %(message)s',
    level=logging.INFO,
)

with open('conf/config.json', 'r') as f:
    try:
        CONFIG = json.load(f)
    except IOError:
        logging.critical('Opening file error, config file not found')
        exit(1)
    except ValueError:
        logging.critical('Decoding Config JSON failed')
        exit(1)

class DCOSTestCase(unittest.TestCase):
    """ Class of DCOS testcase """

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()
        logging.info('delete service')
        logging.info('End of functional test: test_dcos')

    def setUp(self):
        logging.info('Start functional test: test_dcos ...')
        logging.info('SET UP ')
        self.service_config = ServiceConfigData(name='dcostestcase',
                                                port_number=['80',
                                                             CONFIG['DCOS_TEST_PORT_LIST'][0]],
                                                fqdn='www.google.com',
                                                docker_name=CONFIG['DOCKER_LIST'][0],
                                                network_type='BRIDGE')
        self.driver = None

    def test_for_dcos(self):
        """ Test flow of dcos
            1. check service list on dcos
            2. check google on web
            3. check service list after doing my teammate work
        """
        data_before = {}
        data_after = {}
        logging.info('get dcos resource before trigger service up')
        data_before['message'] = list_app(self.service_config.get_name())

        logging.info('get google website title before trigger service up')
        data_before['google_title'] = get_url_title_on_web('http://'+self.service_config.get_fqdn())
        self.assertIn('Google', data_before['google_title'])
        logging.info('The title of "http://'+self.service_config.get_fqdn() + \
                     '" now is "'+data_before['google_title']+'"')
        logging.info('deploy service "'+self.service_config.get_name()+'"')

        data_after['message'] = list_app(self.service_config.get_name())
        data_after['google_title'] = get_url_title_on_web('http://'+self.service_config.get_fqdn())
        logging.info('before title: '+data_before.get('google_title'))
        logging.info('after title: '+data_after.get('google_title'))
        logging.info('before message: '+data_before['message'])
        logging.info('after message: '+data_after['message'])
        self.assertTrue('does not exist' in data_before.get('message'))

if __name__ == '__main__':
    unittest.main()
