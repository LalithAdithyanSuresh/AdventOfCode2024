import sys
path = sys.argv[1]
with open(path) as f:
    text = f.readlines()

# Getting Reports Ready
reports = [x.split() for x in text]
reports = [[int(x) for x in y] for y in reports]

# Checking if level is safe or not
c = 0
for report in reports:
    f = 1
    if(not (sorted(report) == report or sorted(report) == report[::-1])):
        continue
    p = report[0]
    for level in report[1:]:
        if(not(abs(p-level) >=1 and abs(p-level) <=3)):
            f=0
            break
        p = level
    if(f==1):
        c+=1

print(c)
