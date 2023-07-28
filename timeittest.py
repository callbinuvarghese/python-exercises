
def test():
    """Stupid test function"""
    L = [i for i in range(100)]

def f(x):
    return x**2
def g(x):
    return x**4
def h(x):
    return x**8

def fun():
    import random
    return random.randint(100, 800)

if __name__ == '__main__':
    
    #import timeit
    #print("The time taken is ",timeit.timeit(stmt='x=15;y=15;sum=x+y'))
   
    #import timeit
    #print(timeit.timeit("test()", setup="from __main__ import test"))
    # need to import function indiviually as above or declare as global below
    #print(timeit.timeit("test()", globals=globals()))

    #import timeit
    #print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))
    # declare globals instead of import

    import timeit
    start = timeit.default_timer()
    print("The start time is :", start)
    fun()
    print("The difference of time is :",timeit.default_timer() - start)

