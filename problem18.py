with open('problem18_triangle') as f:
    content = [x.strip('\n') for x in f.readlines()]

full_1=list()
full_2=list()

for i in content:
    q=i.split(' ')
    full_1.append(q)


print (full)

lenfull=len(full)
pathlist=list()
sumval=int(0)

for sub in full_1:
    if len(sub)==1:
        pathlist.append(sub[0])
        sumval=sumval+int(sub[0])
    elif len(sub)==2:
        pathlist.append(max(sub))
        sumval=sumval+int(max(sub))
    else:
        pathlen=len(pathlist)
        position=full[pathlen-1].index(pathlist[pathlen-1])
        num1=sub[position]
        num2=sub[position+1]
        if num1>num2:
            pathlist.append(num1)
            sumval=sumval+int(num1)
        else:
            pathlist.append(num2)
            sumval=sumval+int(num2)

print (pathlist)
print (sumval)
