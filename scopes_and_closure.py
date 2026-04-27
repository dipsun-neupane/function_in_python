''' x = 9999
def func1():
    x = 101010101                                                            #  1  
    def func2():
        print(x)
    func2()
func1()

'''

'''
def chai(num): #2
    def actual(x):                                                       #  2
        return num ** x #2
    return actual

square = chai(2)  # 'square' is now a function where num is 2
print(square(5))  # Now you provide x (5). Result: 32 (2**5)


'''

def chaicode(num):
    def another(x):
        return num**x
    return another 
'''
                                                             #  3

 '''
result = chaicode(4)
print(result(3))
