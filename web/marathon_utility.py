""" utility functions of marathon restful api for test case development """
import os
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

def list_app(service_id):
    """ List the app """
    logger.info("List this app : " + service_id)
    for marathon_url in CONFIG['MARATHON_URL']:
        command = 'curl -s -X GET '+marathon_url+'/apps/'+service_id
        return os.popen(command).read()

def destroy_app(service_id):
    """ Delete this app """
    logger.info("delete app : " + service_id)
    for marathon_url in CONFIG['MARATHON_URL']:
        command = 'curl -s -X DELETE '+marathon_url+'/apps/'+service_id
        return os.popen(command).read()
