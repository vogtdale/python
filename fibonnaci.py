


def Fibonacci(n): 
    if n<0: 
        return 0
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 
n = int(input()) 
print(Fibonacci(n)) 