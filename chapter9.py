def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = []

    def f(self):
        return 'hello world'

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class Dog:

    tricks = []             # mistaken use of a class variable
    kind = 'canine'         # class variable shared by all instances
    color = ''              

    def __init__(self, name):
        self.name = name
        self.abilities = [] # mutable; but will be tied to individual instance

    def add_trick(self, trick):
        self.tricks.append(trick)

    def add_ability(self, ability):
        self.abilities.append(ability)

class Warehouse:
   purpose = 'storage'
   region = 'west'

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int


class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index-1
        return self.data[self.index]

class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age
    
    def __str__(self):
        return f'The creature type is {self.name} and the age is {self.age}'

    def __repr__(self):
        return f'Ocean(\'{self.name}\', {self.age})'

def reverse(data):
    '''
    the yield statement whenever they want to return data. 
    '''
    for index in range(len(data)-1, -1, -1):
        yield data[index]

class A:
    def __init__(self, item):
        self.item = item
    def __getitem__(self, index):
        return self.item[index]
    def __setitem__(self, index, item1):
        self.item[index] = item1
    def __len__(self):
        return len(self.item)
    def __contains__(self, item):
        return item in self.item

class ReprExample:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __repr__(self):
        return f"ReprExample(a={self.a}, b={self.b}, c={self.c})"
    def __contains__(self, item):
        ret=False
        if (item==self.a):
            ret = True
        elif (item==self.b):
             ret = True
        elif(item==self.c):
             ret = True
        return ret
    

class Comparison:
    def __init__(self, a):
        self.a = a
    def __lt__(self, object2):
        return self.a < object2.a
    def __gt__(self, object2):
        return self.a > object2.a
    def __le__(self, object2):
        return self.a <= object2.a
    def __ge__(self, object2):
        return self.a >= object2.a
    def __eq__(self, object2):
        return self.a == object2.a
    def __ne__(self, object2):
        return self.a != object2.a

class WriteFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None
    def log(self, text):
        self.file.write(text+'n')
    def __enter__(self):
        self.file = open(self.file_name, "a+")
        return self    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

#https://www.analyticsvidhya.com/blog/2021/08/explore-the-magic-methods-in-python/

if __name__ == '__main__':
    scope_test()
    print("In global scope:", spam)

    x = MyClass()
    print(x.f())

    x = Complex(3.0, -4.5)
    print(x.r, x.i)

    bull=Dog("Bulldog")
    pom=Dog("Pomerenian")
    bull.color="Brown"
    pom.color="White"
    print(f"bull.color={bull.color}")    
    print(f"pom.color={pom.color}")    
    print(f"kind={pom.kind}")    
    print(f"bull.name={bull.name}")
    print(f"pom.name={pom.name}")    


    bull.add_trick("Sommersault")
    bull.add_trick("Fetch ball")
    print(bull.tricks) # unexpectedly shared by all dogs

    pom.add_trick("Play dead")
    pom.add_trick("Roll over") 
    print(pom.tricks) # unexpectedly shared by all dogs
    print(bull.tricks)

    bull.add_ability("Eatwell")
    bull.add_ability("Sleepwell")
    pom.add_ability("Swim")
    pom.add_ability("Run")
    print(bull.abilities)
    print(pom.abilities)


    w1 = Warehouse()
    print(w1.purpose, w1.region)
    #storage west
    w2 = Warehouse()
    w2.region = 'east'
    print(w2.purpose, w2.region)
    #storage east
    print(w1.purpose, w1.region)

    list1 = ["Mary", "had", "little"]
    map1 = Mapping(list1)
    print(f"Map.items_list={map1.items_list}")

    key1 = ["k1", "k2", "k3", "k4"]
    val1 = ["v1", "v2"]
    map2 = MappingSubclass(key1) # Subclass does not have __init so base class _init is called
    map2.update(key1,val1)
    print(f"Map.items_list={map2.items_list}")

    john = Employee('john', 'computer lab', 1000)
    print(f'dept={john.dept}')
    print(f'salary={john.salary}')

    
    for char in Reverse("spam"):
        print(char)
    print(dir(Reverse("Some")))
    print("repr:",repr(Reverse("Some")))
    print("str() string: ", str(Reverse("Some")))

    c = Ocean('Jellyfish', 5)
    print("str()", str(c))
    print("repr:",repr(c))

    print(reverse("golf"))
    print(reverse("golf"))

    for char in reverse('golf'):
        print(char)
    
    print(sum(i*i for i in range(10))) 

    xvec = [10, 20, 30]
    yvec = [7, 5, 3]
    print(sum(x*y for x,y in zip(xvec, yvec)) )
    data="golf"
    print(list(data[i] for i in range(len(data)-1, -1, -1)))

    a = A(["1", "2","3"])
    print(f"a[0]={a[0]}")
    print(f"a[1]={a[1]}")
    print(f"a[2]={a[2]}")
    a[0]=9
    print(f"a[0]={a[0]}")
    print(f"len(a)={len(a)}")
    print(f"'2' in a={'2' in a}")
    print(f"2 in a={2 in a}")

    repr_instance = ReprExample(1, 2, 3)
    print(repr(repr_instance))
    repr_instance = ReprExample(c=1, b=2, a=3)
    print(repr(repr_instance))
    print(f"2 in repr_instance={2 in repr_instance}")
    print(f"5 in repr_instance={5 in repr_instance}")

    a = Comparison(1)
    b = Comparison(2)
    print(f"a < b ={a < b}")
    print(f"a > b ={a > b}")
    print(f"a <= b ={a <= b}")
    print(f"a >= b ={a >= b}")
    print(f"a == b ={a == b}")
    print(f"a != b ={a != b}")

    with WriteFile(r"filename.txt") as log_file:
        log_file.log("Log Test 1")
        log_file.log("Log Test 2")

    i = iter(Squares(1, 3))
    print(next(i))
    print(next(i))
    print(next(i))