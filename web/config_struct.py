""" service vm parameter """
import json
import logging

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

class ServiceConfigData(object):
    """class for ServiceConfigData """

    valid_keys = ["name", "port_number", "fqdn", "network_type", "docker_name", "pod_name"]
    def __init__(self, **kwargs):
        for key in self.valid_keys:
            self.__dict__[key] = kwargs.get(key)

    def get_valid_keys(self):
        """ get all valid keys """
        return self.valid_keys

    def add_vaild_key(self, new_key):
        """ add a new vaild key """
        self.valid_keys.append(new_key)

    def get_name(self):
        """ get service name """
        return self.__dict__['name']

    def get_fqdn(self):
        """ get service fqdn """
        return self.__dict__['fqdn']

    def get_port_number(self):
        """ get port number """
        return self.__dict__['port_number']
