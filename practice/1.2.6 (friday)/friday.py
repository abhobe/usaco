
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

d13s = [0,0,0,0,0,0,0]

fin =  open('friday.in', 'r')
fout =  open('friday.out', 'w')
topYear = int(fin.readline())

fys = []

for i in range(topYear):
    fys.append(1900+i)
startDay = 2

for y in fys:
    for mon in months:
        d13s[(startDay+12) % 7] += 1
        if mon == 'Jan' or mon == 'Mar' or mon == 'May' or mon == 'Jul' or mon == 'Aug' or mon == 'Oct' or mon == 'Dec':
            startDay = (startDay+31) % 7
        elif mon != 'Feb':
            startDay = (startDay+30) % 7
        elif y % 100 == 0 or  y % 4 !=  0:
            startDay = (startDay + 28) % 7
        elif y % 4 == 0 and y % 100 != 0:
            startDay = (startDay + 29) % 7

for i in d13s:
    fout.write(str(i)+" ")
fout.write("\n")
fout.close
