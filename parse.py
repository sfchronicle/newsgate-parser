import os
import zipfile

from lib.utils import all_files
from ipdb import set_trace as debugger

DATA_DIR = os.path.join(os.getcwd(), 'data')
DUMP_DIR = os.path.join(os.getcwd(), 'dump')

def unzip(source_filename, dest_dir):
    """
    Unzip a zip file into dir
    http://stackoverflow.com/a/12886818/868724
    """
    with zipfile.ZipFile(source_filename) as zf:
        # Path traversal defense copied from
        # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
        for member in zf.infolist():
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                drive, word = os.path.splitdrive(word)
                head, word = os.path.split(word)
                if word in (os.curdir, os.pardir, ''): continue
                path = os.path.join(path, word)
            zf.extract(member, path)

if __name__ == '__main__':
    if not os.path.exists(DUMP_DIR):
        os.makedirs(DUMP_DIR)
    zipfiles = list(all_files(DATA_DIR, '*.zip'))

    for zf in zipfiles:
        unzip(zf, DUMP_DIR)
