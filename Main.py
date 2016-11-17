# ¤¤¤ Leian kuidas pääseda ligi kõikidele vajalikkele failidele ¤¤¤

import os
file = os.listdir("C:\Program Files (x86)\Steam\steamapps\common\Stellaris")

print(file)
new = []
for i in file:
    if 'dll' not in i and 'py' not in i and 'txt' not in i and 'bin' not in i and 'exe' not in i and 'dat' not in i:
        new += [i]

print(new)
s = []
for i in new:
    s += os.listdir('C:\Program Files (x86)\Steam\steamapps\common\Stellaris\%s' %(i))
    print(s)

