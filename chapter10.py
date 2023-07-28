import os
print(os.getcwd()) 

import glob
print(glob.glob('*.py'))

import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(f'Mean={statistics.mean(data):2.4f}')
print(f'Median={statistics.median(data)}')
print(f'Variance={statistics.variance(data)}')

from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        #print(line)
        words = line.split(': ')
        match(words[0]):
            case 'week_number':
                print(f'week_number={words[1]}')
            case 'day_of_year':
                print(f'day_of_year={words[1]}')
            case 'day_of_week':
                print(f'day_of_week={words[1]}')
            case _:
                if words[1].strip() != '':
                    print(f'{words[0]}={words[1]}')

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)



if __name__ == "__main__":
    unittest.main()  # Call