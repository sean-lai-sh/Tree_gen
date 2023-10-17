
import pandas as pd
import numpy as np
import math

# Function is yet to work when order of left right left right functions are important!!!.
def tree_gen(n, rule_l, rule_r):
    lst = tree_gen_help(0, n, [0])  # O(2^n)
    for i in range(len(lst)):
        compute_val(lst, i, rule_l(n-lst[i]), rule_r(lst[i]))
    return lst

"""
Assume that:
1. start < end
2. lst is of type list
3. lst is intially [0]
"""
def tree_gen_help(start, end, lst):
    if start == end:
        return lst
    new_lst = lst * 2 # 1 + 2 + 4 + 8 + 16 + 32 + 64 ... + 2^(n-1) + 2^n = 2^n -1
    for i in range(len(lst), len(new_lst)): # O(n) as goes from n/2 -> n
        new_lst[i] += 1
    return tree_gen_help(start + 1, end, new_lst) # O(n) as runs from start -> end

def compute_val(arr, index, rule_l, rule_r):
    arr[index] = rule_l + rule_r

def sub_l(n):
    return n * -1

def add_r(n):
    return n * 1

def add_a(n):
    return "a" * n

def add_c(n):
    return "c" * n
print(tree_gen(2, sub_l,add_r))
print(tree_gen(3, add_a,add_c))