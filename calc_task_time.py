import time

def calc_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter() 
        result = func(*args, **kwargs)
        end = time.perf_counter()
        
        duration = end - start
        print(f"Execution time: {duration} seconds")
        return result
    return wrapper

@calc_time
def calculate_average(n1, n2, n3, n4):
    total = n1 + n2 + n3 + n4 
    avg = total / 4
    print(f"The average is: {avg}")

calculate_average(1, 2, 3, 4)


#  Also :
#  Limits the output to 6 decimal places
# print(f"Execution time: {duration:.6f} seconds") 
# What A Stuff Dude! 