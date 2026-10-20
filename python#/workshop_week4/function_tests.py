import math
import random

def ten_times(number):
    return number * 10

def multiplier(num1, num2):
    return num1 * num2

def pi():
    return math.pi

def pounder(amount):
    return '£' + str(amount)

def printer(text, number):
    return text * number

def greeter(string):
    if string:
        return 'Hello ' + string
    else:
        return 'pls enter a valid string'

def a_thousand_times():
    name = 'josh'
    return name * 1000

def random_two(list):
    return random.choices(list, k=2)

def list_adder(list1, list2):
    total_list=[]
    for i, j in zip(list1, list2):
        sum = i + j
        total_list.append(sum)
    return total_list

def dict_former(key_list, value_list):
    dict = {}
    for i, j in zip(key_list, value_list):
        dict[i] = j
    return dict


debugger = [ten_times(10), multiplier(2,2), pi(), pounder(23), printer('josh', 3),  greeter(''), greeter('josh'), random_two([1,2,3,4,6]), list_adder([1,3,5,7],[23,5,3,1]), dict_former(['a','b','c','d'], ['apple', 'boy', 'come', 'dick'])]

print(debugger)