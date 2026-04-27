num = int(input("enter the no. of fibonacci term you want  :  - "))
def calc_fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return calc_fibonacci(num-1) + calc_fibonacci(num-2)
    
    


''' Reme()


Since we already count it or got it , so now 
we are just calling that fibo() and using it.

'''

for i in range(num):
    print(calc_fibonacci(i) , end = "    ")
