import os.path
import sys

file=input('Enter the file name: ')
if not os.path.isfile(file):
    print('file name ',file,' doesn\'t exist!!!')
    sys.exit(0)

d = dict() 

with open(file,'r') as text:
    for line in text: 

        line = line.strip() 

        words = line.split(" ") 

        for word in words: 

            if word in d:  

                d[word] = d[word] + 1

            else:  

                d[word] = 1


for key in list(d.keys()): 

    print(key, ":", d[key]) 
