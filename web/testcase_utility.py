""" utility functions for test case development """
import os
import time
import socket
import httplib
import json
import logging
import dns.resolver
from dns.exception import DNSException
from urllib2 import urlopen, HTTPError, URLError
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException

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

def load_driver():
    """ load webdriver """
    driverPath = "http://127.0.0.1:4444/wd/hub"
    try:
        driver = webdriver.Remote(driverPath, DesiredCapabilities.FIREFOX)
        return driver
    except WebDriverException:
        logger.critical("Failed to start driver at " + driverPath)
        exit(1)

def get_url_title_on_web(url):
    """ get specific url title on web"""
    logger.info("Get url title on web")
    driver = webdriver.Firefox()
    driver.get(url)
    title = driver.title
    driver.quit()
    return title

def is_url_ok(url):
    """ is url ok """
    try:
        urlopen(url)
    except HTTPError:
        return 0
    except URLError:
        return 0
    else:
        return 1
