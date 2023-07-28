#https://docs.python.org/3/tutorial/
msg="Hello World"
print(msg)
print(msg.upper())
msgArr = msg.split()
for token in msgArr:
  print(token.upper())

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    print("inloop"+x)
    break
print(x)

for x in range(2, 6):
  print(x)

def parity(x):
  result = "odd"
  if (x % 2 == 0):
    result = "even"
  return result

print("parity of 5 "+ parity(5));
for num in range(4):
  print("parity of ", num ,"is", parity(num));

num = 5;
print("Integer", int(num));
print("Float", float(num));
print("boolean", bool(num));
print("string ", str(float(num)))

# See the special char is turned off by defining a raw string
print ('This \is \not a \newline');
print (r'This \is \not a \newline');
# raw string perfect example
print(r'C:\some\name') 

print("""
Multi-line
String
with special \n
char
""")
      
text_str = ('String continuation in ..\n' 
' in next line\n'
'Concatenation of list values like..'        
      )


print(text_str)

str_test = 'String continuation in multiple lines'
str_test1 = ("String"
" continuation in "
'multiple lines')
print(str_test1)
if (str_test==str_test1):
  print("String in multiple lines met")
else:
  print("String in multiple lines NOT met")

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

print(2*"Blah " + " Black sheep.. multiplication of String!")

bool_condition_var=False
if (bool_condition_var):
  print ("condition met")
else:
  print ("condition not met")

python_str="Python"
print("first char ",python_str[0])
print("last char ",python_str[-1])
print("2 to 5 char ",python_str[2:5])
print("J"+python_str[1:])
print(python_str[-2:]+ " going")
#print(python_str[41], "range check in index")
print("no range check in bouns", python_str[41:])

squares=[1,4,9,16,25]
print(f'indexed {squares[0]}')
print(f'sliced {squares[3:]}')
print(f'sliced {squares[-3:]}')
squares=squares+[37,49]
print(f'concatenated {squares}')
squares[-2]=36
print(f'updated valued {squares}')

letters=['a','b','c']
print(f'letters {letters}')
print(f'letters {letters[1].upper()}')

mixed=letters+squares
print(f'mixed {mixed}')
print(f'doubled {mixed*2}')
print(f'mixed orig {mixed}')
combo=[letters,squares]
print(f'combo first letters[1] {combo[0]}')
print(f'combo second squares[3] {combo[1][3]}')

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(f'mixed {x[0]}')

i=1
while i<5:
  i=i+1
  print(f'index {i}')

#https://docs.python.org/3/tutorial/controlflow.html
# Control Statements

today="Thu"
if (today=="Wed"):
  yesterday="Tue"
elif (today=="Tue"):
  yesterday="Mon"
elif (today=="Mon"):
  yesterday="Sun"
else:
  yesterday="NUL"
print(f'today: {today}; yesterday:{yesterday}')

animals=['cat','dog','goat']
for animal in animals:
  print(f'animal: {animal.upper()}; len:{len(animal)}')


mapLen={'Binu':4, 'Elanor':6, 'Steve':5}
for name, leng in mapLen.items():
  print(f'animal: {name.upper()}; len:{len(name)}; leng:{leng}')

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print(f'Users:{users}')

#Iterate over a copy so that delete does not affect
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(f'Users:{users}')

active_users ={}
for user, status in users.items():
  if status == 'active':
    active_users[user] = status
print(f'Active Users:{active_users}')

#range
for r in range(5):
  print(f'r:{r}')

print(f'range:{list(range(5, 10))}')
print(f'range:{list(range(3, 15, 3))}')

rhyme=["Blah", "Blah", "Black", "Sheep"]
for i in range(len(rhyme)):
  print(f'rhymeword:{rhyme[i]}')

print(f'range:{sum(range(4))}')

for num in range(2,7):
  if (num % 2 == 1):
    print(f'odd:{num}')
    continue
  print(f'even:{num}')

# Case statement

http_error=200
match http_error:
  case 200:
    print(f'Success')
  case 400:
    print(f'Bad Request')
  case 404:
    print(f'Not Found')
  case _:
    print(f'unknown')

match http_error:
  case 200|400|404:
    print(f'Known')
  case _:
    print(f'Unknown')

#Class with contructor
class Point:
  x: int
  y: int
  def __init__(self, x, y):
      self.x = x
      self.y = y
  def area(self):
    print(f'Area:{self.x*self.y}')
  def arearet(self):
    return self.x*self.y

def where_is(point):
  """first statement can be string that documents the function"""
  match point:
    case Point(x=0, y=0):
      print(f'Origin')
    case Point(x=0, y=y):
      print(f'X Axis; y:{y}')
    case Point(x=x, y=0):
      print(f'Y Axis; x:{x}')
    case Point():
      print(f'Point somewhere')
    case _:
      print(f'Not a point')    

where_is(Point(0,0))
where_is(Point(0,5))
where_is(Point(6,0))
where_is(Point(7,8))
Point(7,8).area()
print(f'Area of point returned:{Point(7,8).arearet()}')

#Functions
def square(n):
  """returns the square of the number"""
  return n*n

print(f'Square of 4 returned:{square(4)}')
# following returns error at run; no syntax highlight for error in IDE
#print(f'Square of d returned:{square("d")}')

def square_formal(n:int):
  """returns square with formal type declaration"""
  return n*n;
print(f'Square of 4 returned:{square_formal(4)}')
# declaring data type does not do syntax highlight for error in IDE
#print(f'Square of 4 returned:{square_formal("d")}')

#https://realpython.com/python-pass-by-reference/
# internal address of the look up space
def modify_passed(passed):
  print(f"Initial address of passed: {id(passed)};passed:{passed} in modify_passed")
  passed = passed + 1
  print(f"Initial address of passed: {id(passed)};passed:{passed} in modify_passed")  
  return passed
passing = 5
print(f"Initial address of passing: {id(passing)};passing:{passing} in main")
print(f'Modify passed:{modify_passed(passing)} in main')
print(f'Modify passed:{passing} in main')
print(f"Final address of passing: {id(passing)};passing:{passing} in main")

# Pass by value proof; Pass by ref is not there
def greet(name, counter):
  counter += 1
  return f'Hello {name}'

counter = 0
print(f'{greet("John", counter)}')
print(f'Counter is {counter}')
print(f'{greet("Mary", counter)}')
print(f'Counter is {counter}')

#Multiple return values for function


def return_multiple():
  """Return multiple values as tuples. tuples in 
  python are enclosed in parentheses
  return commas form them as tuples inside this function
  """
  return 1, 2

# return_multiple to multple return variables
print(f'return tuple {return_multiple()}')
x, y = return_multiple()
print(f'return multi; x:{x}; y:{y}')

def tryparse(string, base=10):
    try:
        return True, int(string, base=base)
    except ValueError:
        return False, None
success, result = tryparse("123")
print(f'Success:{success}, result:{result}')
success, result = tryparse("abc")
print(f'Success:{success}, result:{result}')

#The succes and result tuple can be accessed by index as well
print(f'Success:{tryparse("123")[0]}, result:{tryparse("123")[1]}')

def tryparse(string, base=10):
    try:
        return int(string, base=base)
    except ValueError:
        return None
if (n := tryparse("123")) is not None:
  print(f'Success:{n}')
if (n := tryparse("abc")) is None:
  print(f'Failure:{n}')

res=10 * (n if (n := tryparse("abc")) is not None else 1)
print(f'resul:{res}')

n=tryparse("abc")
if (n is None):
  print(f'Failure:{n}')

# without walrus
n = 30
if n > 10:
    print(f"{n} is greater than 10")

# with walrus
if (n := 15) > 10:
    print(f"{n} is greater than 10")
print(f"n:{n}")

#Walrus (:=) is same as equal to(=) 

# function recursive

def func(n):
  if n == 0:
    return 0
  else: 
    n = n - 1
    print(f"n:{n}")
    return func(n)+n
print(f"fn:{func(5)}")

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#ret=ask_ok('Do you really want to quit?')
#print(f'ret:{ret}')
#ask_ok('OK to overwrite the file?', 2)
#ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i = 5
# default value is evaluated only once in the scope
def f(arg=i):
    print(arg)

i = 6
f()

#default value is evaluated only once in the scope
#default is a mutable object such as a list, dictionary, or instances of most classes
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
'''
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
'''

# None of the following work
#parrot()                     # required argument missing
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argument

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print("-" * 30)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#lambda function
def add_to(n):
  return lambda x: x + n
f=add_to(23)
print(f"return lamba4: {f(4)}")
print(f"return lamba2: {f(2)}")
print(f"return lamba5: {f(5)}")
f=add_to(10)
print(f"return lamba5: {f(5)}")


def make_incrementorx(n):
    return lambda x: x + n
f = make_incrementorx(37)
print(f"f0:{f(0)}")
print(f"f1:{f(1)}")