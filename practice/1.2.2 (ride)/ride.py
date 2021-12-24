"""
ID: arjun.a4
LANG: PYTHON3
TASK: ride
"""

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

alphas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

group = fin.readline()
comet = fin.readline()

gnum = 1
for i in group:
    try:
        gnum = gnum * (alphas.index(i) + 1)
    except:
        break

cnum = 1
for i in comet:
    try:
        cnum = cnum * (alphas.index(i) + 1)
    except:
        break

if cnum % 47 == gnum % 47:
    fout.write('GO\n')
else:
    fout.write('STAY\n')
