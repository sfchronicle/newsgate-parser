import os
import zipfile

import xmltodict
from lib.utils import all_files, unzip
from ipdb import set_trace as debugger

DATA_DIR = os.path.join(os.getcwd(), 'data')
DUMP_DIR = os.path.join(os.getcwd(), 'dump')

def transform_xml_to_json():
    """
    Take xml output and trasform to json
    """
    xml_files = list(all_files(DUMP_DIR, '*.xml'))

    for xf in xml_files:
        pass

if __name__ == '__main__':
    if not os.path.exists(DUMP_DIR):
        os.makedirs(DUMP_DIR)
    zipfiles = list(all_files(DATA_DIR, '*.zip'))

    for zf in zipfiles:
        unzip(zf, DUMP_DIR)
