from random_utils import *

print("Float:", get_random_float())
print("Integer:", get_random_integer(0, 10))
print("Odd:", get_random_odd(1, 10))
print("Even:", get_random_even(0, 10))

fruits = ['apple', 'banana', 'orange','cheery']
print(fruits)
print("Choice:", get_random_choice(fruits))
print("Multiple:", get_multiple_choices([1,2,3,4,5], 2))
print("Sample:", get_sample([1,2,3,4,5], 2))
print("Shuffle:", shuffle_items(['A','K','Q','J']))

print("Uniform:", get_uniform(1, 10))

print(set_seed(4))
