import os
import fnmatch
import zipfile

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

def all_files(root, patterns='*', single_level=False, yield_folders=False):
    """
    Expand patterns form semicolon-separated string to list
    example usage: thefiles = list(all_files('/tmp', '*.py;*.htm;*.html'))
    """
    patterns = patterns.split(';')

    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)

        files.sort()

        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path, name)
                    break

        if single_level:
            break
