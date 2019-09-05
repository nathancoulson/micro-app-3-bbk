import random
import math

def list_gen(num):
    num_list = []

    for i in range(num*5):
        num_list.append(random.randint(num, num*5))

    return num_list

def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)

def driver(num):
	num_list = list_gen(num)

	quick_sort(num_list)

	return num_list[num]

def recon_path(app_list):
    path = ""
    length = len(app_list)
    for app in app_list:
        if length > 1:
            path += str(app) + "-"
        else:
            path += str(app)
        length -= 1
    return path
