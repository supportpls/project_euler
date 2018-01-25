#project euler problem8
#by dan ikonnikov

import operator
import functools
import re

raw=open("problem8num.txt","r")

content = raw.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
large=''.join(content)
#print (large)
'''
temp = re.split('0',large)
print(type(temp))

list2=list()

for i in temp:
    print (len(i))
    if len(i)>12:
        list2.append(i)

print (list2)

'''
maxnum=len(large)
startnum=0
endnum=startnum+13
maxlist=list()

def product_calc (large_sub):
    large_int=list()
    for i in large_sub:
        large_int.append(int(i))
    int_sum=functools.reduce (lambda x,y: x*y, large_int)
    return (int_sum)

while endnum  != maxnum:
    large_sub=list(large[startnum:endnum])
    if '0' in large_sub:
        pass
    else:
        print (large_sub)
        prod=product_calc(large_sub)
        print(prod)
        maxlist.append(prod)
    startnum=startnum+1
    endnum=endnum+1

max_val=max(maxlist)
print(max_val)
