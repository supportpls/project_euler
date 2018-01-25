#project euler problem4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
#Mary Nguyen - Algorithm design
#Dan Ikonnikov - Legwork

#initialise
init_val=999
print (init_val)

#create the palindrome valie
def pali_create (test_val):
    print (test_val)
    test_val_str=str(test_val)
    val_start_front=test_val_str[0]
    val_mid_front=test_val_str[1]
    val_end_front=test_val_str[2]
    pali_list=[val_start_front,val_mid_front,val_end_front,val_end_front,val_mid_front,val_start_front]
    pali_int=int(''.join(pali_list))
    return pali_int

#now to test the palindrome for two three digit factors
def pali_factor_test (pali_int):
    print ('Testing palindrome ', pali_int)
    factor_test1=999
    while True:
        factor_test2=pali_int/factor_test1
        print (pali_int)
        print (factor_test1,factor_test2)
        print ('stuck at loop in line 28')
        if factor_test2<factor_test1:
            print ('stuck in loop on line 31')
            if pali_int%int(factor_test2)==0:
                print ('stuck in loop on line 33')
                out='y'
                print ("Success")
                factor1=int(factor_test1)
                factor2=int(factor_test2)
                break
            else:
                print ('stuck in loop on line 40')
                factor_test1=factor_test1-1
        elif factor_test2>factor_test1:
            print ('breaking loop at line 43')
            out='n'
            print ("Failure")
            factor1=0
            factor2=0
            break
    return out, factor1, factor2

#main function runs the palindrome creator using the initial value and sends it to the testing algorithm
#def main(init_val):
while True:
    pali_int = pali_create (init_val)
    print (pali_int)
    out_pali_test=pali_factor_test (pali_int)
    print(out_pali_test)
    out=out_pali_test[0]
    print (out)
    factor1=out_pali_test[1]
    print(factor1)
    factor2=out_pali_test[2]
    print (factor2)
    if out =='n':
        init_val=init_val-1
        pali_int=pali_create (init_val)
        print ('Next Test ', pali_int)
    elif out == 'y':
        print (factor1,factor2,pali_int)
        break
#    return

#main (init_val)
