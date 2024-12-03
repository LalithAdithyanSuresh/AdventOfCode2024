import sys
path = sys.argv[1]
with open(path) as f:
    text = f.readlines()

# Getting Reports Ready
reports = [x.split() for x in text]
reports = [[int(x) for x in y] for y in reports]

# Checking if level is safe or not with a dampener

c = 0
for report in reports:
    f = 1
    if(not (sorted(report) == report or sorted(report) == report[::-1])):
        f=0
    p = report[0]
    for level in report[1:]:
        if(not(abs(p-level) >=1 and abs(p-level) <=3)):
            f=0
            break
        p = level
    if(f==1):
        c+=1
    else:
        w = 0
        for i in range(len(report)):
            tempReport = report.copy()
            tempReport.pop(i)
            f = 1
            if(not (sorted(tempReport) == tempReport or sorted(tempReport) == tempReport[::-1])):
                f=0
            p = tempReport[0]
            for level in tempReport[1:]:
                if(not(abs(p-level) >=1 and abs(p-level) <=3)):
                    f=0
                    break
                p = level
            if(f==1):
                w=1
                break
        if(w==1):
            c+=1

print(c)
