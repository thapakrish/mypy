# @author Krishna
# Thunking in python?
# Recursion.
# Mutual recursion
# Streams


def dog_tail(a , b):
    """
    Some recursion. Add all the numbers from between a to b, inclusive a
    
    int * int -> int


    >>> dog_tail(0,1)
    0
    >>> dog_tail(1,4)
    6
    >>> dog_tail(5,7)
    11    
    >>> dog_tail(5,5)
    0
    
    
    """
    
    if (a==b or b<a):
        return 0
    return a + dog_tail(a+1,b)


def chicken_egg(n):
    """
    some mutual recursion
    >>> chicken_egg(100)
    "Even"
    """
    return chicken(n)
    


def chicken(n):
    if n % 2 == 0:
        return "Even"
    else:
        return egg(n)


def egg(n):
    if n % 2 <> 0:
        return "Odd"
    else:
        return chicken(n)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
