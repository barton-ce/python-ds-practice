def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a > b:
        print('First is Greater')
    elif a == b:
        print('Numbers are Equal')
    elif a < b: 
        print('Second is greater')

number_compare(10, 10)
number_compare(-1, 1)