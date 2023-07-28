def exc1():
    while True:
        try:
            x = int(input("Please enter a number: "))
            if x < 0:
                raise Exception("Sorry, no numbers below zero")
            else:
                break
            
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        except Exception:
            print("Oops!  That was no valid positive number.  Try again...")


def exc2():
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))    # the exception type
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
                            # but may be overridden in exception subclasses
        x, y = inst.args     # unpack args
        print('x =', x)
        print('y =', y)

def exc3():
    try:
        f = open('nonexist.txt') # OSError
        #f = open('test.txt')   # ValueError
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error:", err)
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

def this_fails():
    try:
         x = 1/0
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

def exc4():
    divide(12,4)
    divide(5,0)

def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)
def exc5():
    try:
        f()
    except Exception as e:
        print(f'caught {type(e)}: e')

def f():
    raise ExceptionGroup("group1",
                         [OSError(1),
                          SystemError(2),
                          ExceptionGroup("group2",[OSError(3), RecursionError(4)])
                          ])
def exc6():
    try:
        f()
    except* OSError as e:
        print("There were OSErrors")
    except* SystemError as e:
        print("There were SystemErrors")

def f():
    '''
    Document exception; rethrow caught exception
    '''
    try:
        raise TypeError('bad type')
    except Exception as e:
        e.add_note('Add some information')
        e.add_note('Add some more information')
        raise
def exc7():
    f()

def f():
    raise OSError('operation failed')
def exc8():
    excs = []
    for i in range(3):
        try:
            f()
        except Exception as e:
            e.add_note(f'Happened in Iteration {i+1}')
            excs.append(e) # Append exception to list

    # rethrow the list of exceptions together
    raise ExceptionGroup('We have some problems', excs)

if __name__ == "__main__":
    #exc1()
    #exc2()
    #exc3()
    #this_fails()
    #exc4()
    #exc5()
    #exc6()
    #exc7()
    exc8()