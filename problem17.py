#project euler
#problem 17

sum_let=0

letter_values={1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}


def letter_count (input_num):
    #first two check - if the amount is over 100
    digit1=input_num/100
    digit2=int(digit1)

    if input_num<21:
        #we can just lookup the dictiary value for values 20 and under
        print (letter_values[input_num])
        output_val=letter_values[input_num]
    elif digit2 == 10:
        #this is for one thousand
        output_val=11
    elif digit2 == 0:
        #this is for just  under 100
        digit3=input_num%100
        digit4=digit3%10
        if digit4==0:
            output_val=letter_values[digit3]
            print (letter_values[digit3])
        #this is for tens  + single digit value
        else:
            digit5=digit3-digit4
            print (letter_values[digit4]+letter_values[digit5])
            output_val=letter_values[digit4]+letter_values[digit5]
    else:
        #this is for round hundres
        digit3=input_num%100
        if digit3 == 0:
            print (7+letter_values[digit2])
            output_val=7+letter_values[digit2]
        else:
        #this is for hundres + tens only or tens + single digit values
            digit4=digit3%10
            if digit4==0:
                #x hunded(7) and(3) x tens
                print (10+letter_values[digit2]+letter_values[digit3])
                output_val=10+letter_values[digit2]+letter_values[digit3]
            else:
                if digit3 < 21:
                    print (letter_values[digit2]+7+3+letter_values[digit3])
                    output_val=letter_values[digit2]+7+3+letter_values[digit3]
                #x hunded(7) and(3) x tens x singles
                else:
                    digit5=digit3-digit4
                    print (letter_values[digit2]+7+3+letter_values[digit4]+letter_values[digit5])
                    output_val=letter_values[digit2]+7+3+letter_values[digit4]+letter_values[digit5]
    return (output_val)

for i in range (1,1001):
    val=letter_count(i)
    sum_let=sum_let+val
    print ('checking', i, 'result', val)
    print (sum_let)

print (sum_let)
