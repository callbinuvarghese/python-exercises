
def testFib1():
    import fibo

    fibo.fib(1000)
    print(f"result={fibo.fib2(1000)}")

def testFib2():
    from fibo import fib, fib2
    fib(1000)
    print(f"result={fib2(1000)}")

def builtInModuleList():
    '''
    current directory is the start of the search path
    sys.path file in current directory can control python module search path
    PYTHONPATH environment variable can be used to set path

    '''
    import sys
    a = sys.builtin_module_names
    #print(a)

    #print(builtInModuleList())

    import fibo
    # prints the functions in the module imported
    print(dir(fibo))

    # Just to print the functions in the module
    a = dir(fibo)
    methodlist=[f for f in a if not f.startswith('__')]
    print(methodlist)

    import builtins
    print(dir(builtins))
    d = dir(builtins)
    undItemList = [x for x in d if x.startswith('__')]
    print(f"under: {undItemList}")
    upperItemList = [x for x in d if x[0].isupper()]
    print(f"upper: {upperItemList}")
    lowerItemList = [x for x in d if x[0].islower()]
    print(f"lower: {lowerItemList}")

    #import binu
    #binu.some()

if __name__ == '__main__':
    #testFib1()
    #testFib2()
    builtInModuleList()