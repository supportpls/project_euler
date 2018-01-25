#project euler problem 11
#by dan ikonnikov

import operator
import functools
import re

raw=open("problem11_numb","r")
print (raw)
content = raw.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
z=len(content)
matrix=[]
prod_list=[]
for x in range (0,z):
    large = content[x].split(" ")
    matrix.append(large)


def test3(row,col):
    print (row, col, "testing diag")
    print (matrix[row][col])
    val_row=int(matrix[row][col])*int(matrix[row][col+1])*int(matrix[row][col+2])*int(matrix[row][col+3])
    val_col=int(matrix[row][col])*int(matrix[row+1][col])*int(matrix[row+2][col])*int(matrix[row+3][col])
    val_diag=int(matrix[row][col])*int(matrix[row+1][col+1])*int(matrix[row+2][col+2])*int(matrix[row+3][col+3])
    val_set=[val_row, val_col,val_diag]
    print (max(val_set))
    return (max(val_set))

def test4(row,col):
    print (row, col, "testing diag")
    print (matrix[row][col])
    val_row=int(matrix[row][col])*int(matrix[row][col+1])*int(matrix[row][col+2])*int(matrix[row][col+3])
    val_col=int(matrix[row][col])*int(matrix[row+1][col])*int(matrix[row+2][col])*int(matrix[row+3][col])
    val_diag_down=int(matrix[row][col])*int(matrix[row+1][col+1])*int(matrix[row+2][col+2])*int(matrix[row+3][col+3])
    val_diag_up=int(matrix[row][col])*int(matrix[row-1][col+1])*int(matrix[row-2][col+2])*int(matrix[row-3][col+3])
    val_set=[val_row, val_col,val_diag_down,val_diag_up]
    print (max(val_set))
    return (max(val_set))

def test_row(row,col):
    print (row, col, "testing row only")
    print (matrix[row][col])
    val_row=int(matrix[row][col])*int(matrix[row][col+1])*int(matrix[row][col+2])*int(matrix[row][col+3])
    val_diag_up=int(matrix[row][col])*int(matrix[row-1][col+1])*int(matrix[row-2][col+2])*int(matrix[row-3][col+3])
    val_set=[val_row, val_diag_up]
    print(max(val_set))
    return (max(val_set))

def test_col(row,col):
    print (row, col, "testing column only")
    print (matrix[row][col])
    val_col=int(matrix[row][col])*int(matrix[row+1][col])*int(matrix[row+2][col])*int(matrix[row+3][col])
    print (val_col)
    return (val_col)

for row in range (0,z):
    if row < 3:
        for col in range (0,z):
            if col < 17:
                test_prod=test3(row,col)
                prod_list.append(test_prod)
            else:
                test_prod=test_col(row,col)
                prod_list.append(test_prod)
    elif row < 17:
        for col in range (0,z):
            if col < 17:
                test_prod=test4(row,col)
                prod_list.append(test_prod)
            else:
                test_prod=test_col(row,col)
                prod_list.append(test_prod)
    else:
        for col in range (0,z-3):
            test_prod=test_row(row,col)
            prod_list.append(test_prod)
print (prod_list)
max_prod=max(prod_list)
print ("max product is:", max_prod)
