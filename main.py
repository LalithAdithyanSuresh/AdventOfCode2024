import os
import subprocess
print("Solutions for AdventOfCode'24")
Folders = os.listdir(__file__.rstrip(__name__ + '.py'))
d = int(input("Enter day (1-25) : "))
if('Day{}'.format(d) not in Folders):
    print("Invalid Day")
    os._exit

# Clearing tempInput
try:
    os.remove('tempInput.txt')
    with open('tempInput.txt','w') as f:
        f.write('REPLACE FILE CONTENTS WITH DAY-{}\'s INPUT\nTHEN SAVE AND EXIT'.format(d))
except:
    pass

# getting input
os.startfile('tempInput.txt')
if(input("Press y to continue : ") != 'y'):
    print('Program halted')
    os._exit

# Getting Answers
print("\nDay-{} Answers".format(d))
print("\tPuzzle-1 : ",end='')
result = subprocess.run(['python','Day{}\\Puzzle1.py'.format(d),__file__.rstrip(__name__ + '.py')+'\\tempInput.txt'],capture_output=True,text=True)
print(result.stdout.rstrip())
print("\tPuzzle-2 : ",end='')
result = subprocess.run(['python','Day{}\\Puzzle2.py'.format(d),__file__.rstrip(__name__ + '.py')+'\\tempInput.txt'],capture_output=True,text=True)
print(result.stdout.rstrip())
