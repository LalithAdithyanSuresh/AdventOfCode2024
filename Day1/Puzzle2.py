import sys
path = sys.argv[1]
with open(path) as f:
    text = f.readlines()
l1,l2 = [],[]
for line in text:
    l1.append(line.split()[0])
    l2.append(line.split()[1])
d = 0
for i in range(len(l1)):
    d += int(l1[i]) * l2.count(l1[i])
print(d) 