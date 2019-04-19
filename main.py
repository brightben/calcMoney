import json
import sys
import logging
from utility_func import clogging
from calcFunc import calcFunc

clogging.basicConfig(
    filename='out.log',
    format='%(levelname)-8s %(asctime)s %(name)s:%(lineno)d| %(message)s',
    level=logging.INFO,
)

CONFIG_FILE = 'conf/config.json'

with open(CONFIG_FILE, 'r') as f:
    try:
        CONFIG = json.load(f)
    except ValueError:
        logging.error("Decoding JSON failed")
        exit()

def main():
    logging.info("Calculating")
    calcfunc = calcFunc(CONFIG)
    finalMoney = calcfunc.calcTotalMoney()
    logging.info("Total Money: %.3fw" % (finalMoney/10000))

if __name__ == '__main__':
    main()
