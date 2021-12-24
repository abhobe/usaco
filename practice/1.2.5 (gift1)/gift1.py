"""
ID: arjun.a4
LANG: PYTHON3
TASK: gift1
"""
class gifter:
    def __init__(self, name, bank, amt, numf, friends):
        self.name = name
        self.bank = bank
        self.amt = amt
        self.numf = numf
        self.friends = friends

fin = open('gift1.in', "r")
fout = open('gift1.out', 'w')

gnum = int(fin.readline())

friends = {}
for i in range(gnum):
    f = fin.readline().rstrip('\n')
    friends[f] = gifter(f,0,0,0,[])

for i in range(gnum):
    giver = friends[fin.readline().rstrip('\n')]
    amt, numf = map(int, fin.readline().split())
    giver.amt = amt
    giver.numf = numf

    giver.bank -= amt

    for k in range(numf):
        recp = friends[fin.readline().rstrip('\n')]
        giver.friends.append(recp.name)
        try:
            recp.bank += amt // numf
        except:
            pass
    
    if numf != 0:
        giver.bank += amt % numf

for i in friends:
    fout.write(friends[i].name + " " + str(friends[i].bank) + "\n")
fout.close()
