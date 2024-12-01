import sys
path = sys.argv[1]
with open(path) as f:
    text = f.readlines()

# Getting the 2 lists ready
l1,l2 = [],[]
for line in text:
    l1.append(line.split()[0])
    l2.append(line.split()[1])

# Sorting the lists
l1,l2 = sorted(l1),sorted(l2)

# Calculating differences between pairs
d = 0
for i in range(len(l1)):
    d += abs(int(l1[i]) - int(l2[i]))
print(d) 