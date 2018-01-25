#project euler problem 13
#by dan ikonnikov

import operator
import functools
import re

raw=open("problem13_num","r")
print (raw)
content = raw.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print (content)
z=0
x=len(content)
for i in range (0,x):
    z=z+int(content[i])

c=str(z)
v=c[0:10]
print (z)
print (v)
