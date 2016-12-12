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


def search_in_file(file, string):
    with open(file, encoding='UTF-8') as new:
        found = str()
        while True:
            line = new.readline()
            if line == '':
                break
            elif string in line:
                found = file
                break
    return found


def search(extensions, topdir, string):
    files = findDirectories(extensions,topdir)
    found = []
    cleared = []
    for file in files:
        try:
            found += [search_in_file(file,string)]
        except:
            pass
    for item in found:
        if item != '':
            cleared += [item]
    return cleared



