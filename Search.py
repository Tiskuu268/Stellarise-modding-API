import os
import subprocess

def findDirectories(extensions, topdir):
    results = str()
    for exten in extensions:
        for dirpath, dirnames, files in os.walk(topdir):
            for name in files:
                if name.lower().endswith(exten):
                    results += '%s\n' % os.path.join(dirpath, name)

    results = results.split('\n')
    return results


def click_on_file(filename):
    try:
        os.startfile(filename)
    except AttributeError:
        subprocess.call(['open', filename])

def search(word, directory):
    extensions = ['.txt','.yml', '.lua']
    files = findDirectories(extensions,directory)
    found = []
    for file in files:
        f = open(file)

