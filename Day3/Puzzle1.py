import sys
import re
path = sys.argv[1]
with open(path) as f:
    text = f.read()

# Getting regex pattern ready
pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

# getting mul() function ready
def mul(a,b):
    return int(a) * int (b)
# Getting sum in single line
c = sum([eval(x) for x in re.findall(pattern,text)])
print(c)
