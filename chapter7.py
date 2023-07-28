def  test7():
    import math
    name = "Binu Here"
    val = math.pi
    print(f'Hello {name}, the value of pi is {val}')
    print(f'The value of pi is approximately {math.pi:.3f}.')

    print('Hello World\n')
    print(repr('Hello World\n')) 

    yes_votes = 42_572_654
    no_votes = 43_132_495
    percentage = yes_votes / (yes_votes + no_votes)
    print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
    print(f'{yes_votes:-9} YES votes  {percentage:2.2%}')

    x = 10 * 3.25
    y = 200 * 200
    s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
    print(s)
    print(repr((x, y, ('spam', 'eggs'))))

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for keyi, valuei in table.items():
        print(f'key:{keyi:20}; value{valuei:5d}')
    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
    print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

    animals = 'eels'
    print(f'My hovercraft is full of {animals}.')
    print(f'My hovercraft is full of {animals!r}.')
    print(f'My hovercraft is full of {repr(animals)}.')

    bugs = 'roaches'
    count = 13
    area = 'living room'
    print(f'Debugging {bugs=} {count=} {area=}')

    print('We are the {} who say "{}!"'.format('knights', 'Ni'))
    print('{0} and {1}'.format('spam', 'eggs'))
    print('{1} and {0}'.format('spam', 'eggs'))
    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))
    print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

    for i in range(1,11):
        print('i={} i**i={}, i^3={}'.format(i, i*i, i*i*i))
    print('-------------------------')
    for i in range(1,11):
        print('i={:2d} i**i={:3d}, i^3={:4d}'.format(i, i*i, i*i*i))

    print('12'.zfill(5))

def  test72():
    with open('test.txt', 'w',encoding='utf-8') as f:
        f.write("first sentence")
        f.write("second second")
        f.write('\n')
        f.write("third sentence\n")
    #f.close() #with does not need explicit close; close will not cause any issue

    with open('test.txt','r',encoding='utf-8') as f:
        print(f.readline())
        print(f.readline())
        print(f.readline()) # does not fail if go past line; print empty
    #f.close() #with does not need explicit close; close will not cause any issue

    import math
    name="Binu"
    with open('test.txt', 'a') as file_object: #’a’ argument to open the file for appending
      file_object.write("I am 6 years old\n")
      file_object.write("I love playing games\n")
      file_object.write(f"Hi {name}, the value of pi is {math.pi:.3f}")

    try:
        with open('notexist.txt', 'r') as f:
            print(f.readline())
    except FileNotFoundError:
        print('File not existing')
    finally:
        f.close() #with does not need explicit close; close will not cause any issue

    try:
        with open('test.txt') as file_object:
            lines = file_object.readlines()
            for line in lines:
                print(line)
    finally:
        file_object.close() #with does not need explicit close; close will not cause any issue

    file_object=open('test.txt', 'r')
    for line in file_object:
        print(line)
    file_object.close() # need to close the file
    
    f = open('workfile', 'w') 
    f.write('0123456789abcdef')
    f.close()
    f = open('workfile', 'r') 
    f.seek(5)      # Go to the 6th byte in the file
    print(f.read(1))
    f.close()

    #binary
    f = open('test.bin', 'wb')
    f.write(b'0123456789abcdef')
    # Go to the 6th byte in the file
    f.close()
    f = open('test.bin', 'r') 
    f.seek(5)
    binch = f.read(1)
    print(binch)
    f.close() # need close as there is no with

def testJson():
    import json
    #Serialize
    obj = [1, 'simple', 'list']
    json_str = json.dumps(obj, indent=4)
    print(json_str)

    f = open('test.json', 'w') 
    json.dump(obj,f)
    f.close() # need close as there is no with

    with open("test.json", 'r') as f:
        obj = json.load(f)
        print(obj)
        print(json.dumps(obj, indent=4))
        #f.close() # with does not need explicit close; close will not cause any issue
    
    json_str = json.dumps({"Id": 78912, "name":"John Doe", "classes":["math","science"]})
    print(json_str)

if __name__ == '__main__':
    #test7()
    test72()
    testJson()