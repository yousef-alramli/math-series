def fibonacci(n):
    """
    1. this function accepts numbers as parameter and will give you the fibonacci numpers 
    2. the number that intered will be how many numbers is shown 
    """
    if n <=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
    """
    1. this function accepts numbers as parameter and will give you the fibonacci numpers 
    2. the number that intered will be how many numbers is shown 
    """
    if n == 1:
        return n
    if n <= 0:
        return 2 
    return lucas(n-1)+lucas(n-2)

def sum_series(n, optional_1=0 , optional_2=1):
    """
    function takes three parameters,
    the last two will decide if it will sum of fibonacci numbers (0,1) or lucas numbers (2,1)
    * note: if the last two parameters are empty it will give you the sum of fibonacci numbers 
    """
    if [optional_1 , optional_2] == [0,1]:
        fibonaccii = list([fibonacci(i) for i in range(n)])
        return sum(fibonaccii)
    
    if [optional_1 , optional_2] == [2,1] or optional_1 == none or optional_1 == none:
        lucasi = list([lucas(i) for i in range(n)])
        return sum(lucasi)
    
for i in range(7):
    print(lucas(i))
