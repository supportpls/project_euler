#project euler problem 16

power_int=2**1000
power_char=str(power_int)
power_list=list(power_char)
sum_total=0

for i in power_list:
    i=int(i)
    sum_total=sum_total+i

print (sum_total)
