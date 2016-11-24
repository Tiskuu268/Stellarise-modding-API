# ¤¤¤ Leian kuidas pääseda ligi kõikidele vajalikkele failidele ¤¤¤


file = "C:\Program Files (x86)\Steam\steamapps\common\Stellaris"
address = []
import os
for root, dirs, files in os.walk(file):
    for file in files:
        if file.endswith(".lua"):
            address += [ os.path.join(root, file)]
language = 'english'
print(address)
clear = []
for i in address:
    if language in i:
        clear += [i]

def search(one, word):
    for s in one:
        with open(s, encoding= 'UTF-8') as new:
            main = new.readlines()
        for i in main:
            if word in i:
                print(i)
    print(1)


search(address, 'EMPIRE')