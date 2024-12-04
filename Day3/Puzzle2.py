import sys
import re
# path = sys.argv[1]
with open('tempInput.txt') as f:
    text = f.read()

# Getting regex pattern ready
pattern = r"(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))"

# getting mul() function ready
def mul(a,b):
    return int(a) * int (b)
# Getting sum in single line
comb = re.findall(pattern,text)
print(comb)
e = 1
d=0
for func in comb:
    if(func[:3] == "mul"):
        if(e==1):
            d+=eval(func)
    elif(func == "do()"):
        e=1
    else:
        e=0
print(d)
