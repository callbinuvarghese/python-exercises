def testList():
    '''
    Python List preserve order and allow duplicates
    '''
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    # Count list occurance for existing
    print(f"Count of Apple in List {fruits.count('apple')}")
    print(f"Count of Kiwi in List {fruits.count('kiwi')}")

    # Count list occurance for non-existing
    print(f"Count of PineApple in List {fruits.count('pineapple')}")

    #Reverse list
    fruits.reverse()
    print(f"List reversed: {fruits}")

    #Append to List
    print(f"List Count before append: {len(fruits)}")
    fruits.append('pineapple')
    print(f"List Count after append: {len(fruits)}")

    #Sort list
    print(f"List unsorted: {fruits}")
    fruits.sort()
    print(f"List sorted: {fruits}")

    #Find element in list
    print(f"List find with index: {fruits.index('kiwi')}")
    
    # try to find an item not in list
    try:
        print(fruits.index("strawberry"))
    except ValueError:
        print("That item does not exist")


def listAsStack():
    '''5.1.1'''
    stack = [3, 4, 5]
    print(f"List before Append: {stack}")
    stack.append(6)
    print(f"List after Append: {stack}")
    stack.pop()
    stack.pop()    
    print(f"List after Pop: {stack}")

def listAsQueue():
    '''5.1.2'''
    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    print(f"queue : {queue}")
    queue.append("Terry")
    queue.append("Graham")
    print(f"queue after append: {queue}")
    queue.popleft()
    print(f"queue after popleft: {queue}")

def listComprehensions():
    '''5.1.3 and 4'''
    squares = []
    for x in range(10):
        squares.append(x**2)
    print(f"squares  {squares}")

    #same with simpler for loop
    squares = [x**2 for x in range(10)]
    print(f"squares  {squares}")

    # same with lambda
    squares = list(map(lambda x: x**2, range(10)))
    print(f"squares  {squares}")

    # list of tuples
    list1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    print(f"[(x,y)]=  {list1}")

    vec = [-4, -2, 0, 2, 4]
    vec2 = [x*2 for x in vec]
    print(f"[vec*2]=  {vec2}")
    # see that the len of the list changed
    vec2 = [x for x in vec if x >= 0]
    print(f"[vec*2 if x>=0]=  {vec2}")
    vec2 =[(x, x**2) for x in range(6)]
    print(f"[vec*2]=  {vec2}")

    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    freshfruit = [x.strip().title() for x in freshfruit]
    print(f"[freshfruit]=  {freshfruit}")

    #list of lists; to combine into 1 list; tough to grasp
    vec = [[1,2,3], [4,5,6], [7,8,9]]
    combined = [num for elem in vec for num in elem]
    print(f"[combined]=  {combined}")

    #list of lists; to combine into 1 list
    vec = [[1,2,3], [4,5], [6,7,8,9,10,11]]
    combined = [num for elem in vec for num in elem]
    print(f"[combined]=  {combined}")

    # combine 2 lists into 1 list
    ls1 = [15,20,35,40]
    ls2 = [99,44,13]
    print(f"[combined]=  {ls1+ls2}")

    num1=[1,2,3]
    num2=[4,5,6]
    #combine lists using list comprehension
    num3=[x for n in (num1,num2) for x in n]
    print(f"[combined]=  {num3}")
   
    ls1 = [6,7,8]
    ls2 = [9,10,11]
    ls3 = [12,13,14]
    #merging lists using unpacking operator(*) 
    ls = [*ls1,*ls2,*ls3]
    print(f"[combined]=  {ls}")

    from math import pi
    piList= [str(round(pi, i)) for i in range(1, 6)]
    print(f"[combined]=  {piList}")

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    transposed = [[row[i] for row in matrix] for i in range(4)]
    print(f"[transposed]=  {transposed}")
    # the same with more simpler code
    transposed = []
    for i in range(4):
         transposed_row = []
         for row in matrix:
            transposed_row.append(row[i])
         transposed.append(transposed_row)
    print(f"[transposed]=  {transposed}")

def testTuples():
    '''5.3
    tuples are immutable; cannot reassign value to an element
    '''
    # bunch of values with no paren is default to Tuples
    t = 12345, 54321, 'hello!'
    print(f"(tuple)=  {t}")
    print(f"(tuple)=  {t[2]}")
    # nested tuples OR tuples of tuples
    u = t, (1, 2, 3, 4, 5)
    print(f"(tuple nested)=  {u[1]}")
    # tuples are immutable
    try:
        t[0] = 88888
    except TypeError:
        print(f"(tuple are immutable)")
    #tuple of lists
    v = ([1, 2, 3], [3, 2, 1])
    print(f"(tuple of lists)=  {v}")
    # can get elements of tuples to variables OR reversing
    x, y, z = t
    print(f"(tuple revesed)=  {x}, {y}, {z}")

def testSet():
    '''5.4
    Unlike Lists, sets cannot have duplicates
    You can't change the items of a set, but you can add to the set and remove from it.
    sets dont have any order preseved
    '''
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    # creat a set from list to dedup
    country_set = set(("USA", "Ukraine", "Nigeria", "Ghana"))
    # sets dont have any order preseved
    print(f"basket=  {basket}")
    print(f"country_set=  {country_set}")
    #Sort not avaialable in Set
    print(f"set unsorted: {basket}")
    sortedbasket = sorted(basket)
    print(f"set sorted: {sortedbasket}")
    # convert Set to list and can sort as well
    basketList = list(basket)
    basketList.sort()
    print(f"set sorted: {basketList}")

    #Check element in set
    print(f"if element in set: { 'orange' in basket  }")
   
    #tokenize string to set; no order preserving
    a = set('abracadabra')
    print(f"tokenized set: {a}")
    # {} taken as default set; strings in ops is taken as set
    b = {x for x in 'abracadabra' if x not in 'abc' }
    print(f"searched subset: {b}")

    # Set operations
    a = set('abracadabra')
    b = set('alacazam')
    # minus; elements of b not present in a
    print(f"a-b: {a-b}")
    # union
    print(f"a|b: {a|b}")
    #intersection; letters in both a and b
    print(f"a&b: {a&b}")
    # letters in a or b but not both
    print(f"a^b: {a^b}")

def testDictionaries():
    '''5.5
    key value pairs
    dictionaries are indexed by keys, 
    keys can be any immutable type; strings and numbers can always be keys
    if values can be modified, can use them ( lists)
    '''
    # constructor record format
    tel = {'jack': 4098, 'sape': 4139}
    print(f"dict tel: {tel}")
    #add more
    tel['guido'] = 4127
    # delete
    del tel['sape']
    print(f"dict tel: {tel}")
    tel['irv'] = 4127
    # Most 
    # list lists the keys
    print(f"dict tel list: {list(tel)}")
    #sorted sort keys and retun
    print(f"dict tel sorted: {sorted(tel)}")
    print(f"dict tel in: {'guido' in tel}")
    print(f"dict tel in: {'xx' in tel}")
    # Constructor with tuples; list of key-value tuples
    dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    d = {x: x**2 for x in (2, 4, 6)}
    print(f"dict : {d}")
    # Constructor with k=v
    d=dict(sape=4139, guido=4127, jack=4098)
    print(f"dict : {d}")

def testDictLoops():
    '''5.6
    dict.items() returns k, v pairs as dict_items
    dict_items as list of tuples(k,v)
    '''
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    print(f"k,v : {knights.items()}")
    for k, v in knights.items():
        print(f"k,v : {k},{v}")
    for k, v in dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]).items():
        print(f"k,v : {k},{v}")
    # enumerate create numeric keys for list
    for i, v in enumerate(['tic','tac','toe']):
        print(f"k,v : {i},{v}")
    # zip combines lists to dict
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))

    import math
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    print(f"raw_data : {raw_data}")
    nums = [x for x in raw_data if not math.isnan(x)]
    print(f"nums : {nums}")
    #same in mor elaborate
    filtered_data = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)
    print(f"nums : {filtered_data}")
    
def main():
    '''https://docs.python.org/3/tutorial/datastructures.html'''
    '''
    testList()
    listAsStack()
    listAsQueue()
    listComprehensions()
    testTuples()
    testSet()
    testDictionaries()
    '''
    testDictLoops()

if __name__ == '__main__':
    main()
