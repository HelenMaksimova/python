import random
import math

print('My tries coding')

# create arrays with generator

test_array = [random.randint(-100, 100) for i in range(20)]

print('Исходный массив случайных чисел от -100 до 100:\n', test_array)

if_array = [math.sqrt(elem) for elem in test_array if elem > 0 and elem % 2 == 0]

print('Массив корней из чётных чисел:\n', if_array)
