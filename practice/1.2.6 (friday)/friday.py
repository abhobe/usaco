"""
ID: arjun.a4
LANG: PYTHON3
TASK: friday
"""
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

d13s = [0,0,0,0,0,0,0]

fin =  open('friday.in', 'r')
fout =  open('friday.out', 'w')
topYear = int(fin.readline())

fys = []

for i in range(topYear):
    fys.append(1900+i)
thirDay = 0

caln = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
call = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

for y in fys:
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        cal = call
    else:
        cal = caln
    for mon in cal:
        d13s[thirDay] += 1
        thirDay = (thirDay+mon) % 7

for i in range(len(d13s)):
    fout.write(str(d13s[i]))
    if i < len(d13s)-1:
        fout.write(" ")
fout.write("\n")
fout.close
