import os
import subprocess

# Find all Files in directory
def findDirectories(extensions, topdir):
    results = str()
    for exten in extensions:
        for dirpath, dirnames, files in os.walk(topdir):
            for name in files:
                if name.lower().endswith(exten):
                    results += '%s\n' % os.path.join(dirpath, name)

    results = results.split('\n')
    return results

# Open file
def openFile(directory):
    try:
        os.startfile(directory)
    except AttributeError:
        subprocess.call(['open', directory])

# Search keyword in file
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

# Search keyword in files
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



