import os
import sys
import zipfile
import logging
import logging_utility

logging_utility.basicConfig(
    stream=sys.stdout,
    format='%(levelname)-8s %(asctime)s %(name)s:%(lineno)d| %(message)s',
    level=logging.INFO,
)

dir_name = '/home/brightben/brightbenWorkSpace/calcMoney/test_zip'
extension = ".zip"

def unzip(dir_name, extension):
    """ function for unzip all zip files in a folder """
    for item in os.listdir(dir_name):
        if item.endswith(extension): # Check extension type
            file_name = os.path.abspath(item)
            logging.info("Unzip file name: " + file_name)
            zip_file = zipfile.ZipFile(file_name)
            zip_file.extractall(dir_name)
            zip_file.close()
            #os.remove(file_name) # Delete zip file



def main():
    logging.warning("Extract all .zip files in folder: " + dir_name )
    unzip(dir_name, extension)
    logging.warning("Extract complete")
    #read your data with loop of listdir

if __name__ == '__main__':
    main()
