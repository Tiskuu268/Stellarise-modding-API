import os
import subprocess

def findDirectories(exten, topdir):
    results = str()

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