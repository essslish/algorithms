#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
from time import *
import numpy as np
import matplotlib.pyplot as plt
from random import randint, seed
from math import *
                
# Сортировка выбором
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        mini = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

# Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
# Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)  
    for bypass in range(1, n):  
        for i in range(n-bypass):  
            if arr[i] > arr[i+1]:  
                arr[i], arr[i+1] = arr[i+1], arr[i]
                
# Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 
    left_part = merge_sort(arr[:mid]) 
    right_part = merge_sort(arr[mid:])  
    
    return merge(left_part, right_part)

def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

# Сортировка Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2 

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        gap //= 2 

def pratt_sequence(n):
    sequence = []
    i, j = 0, 0
    while True:
        value = (2 ** i) * (3 ** j)
        if value > n:
            break
        sequence.append(value)
        if i < j:
            j += 1
        else:
            i += 1
    return sorted(sequence)

#сортировка Шелла с последовательностью Пратта
def shell_sort_pratt(arr):
    n = len(arr)
    gaps = pratt_sequence(n)
    
    for gap in reversed(gaps):
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

def hibbard_sequence(n):
    sequence = []
    k = 1
    while (2 ** k) - 1 < n:
        sequence.append((2 ** k) - 1)
        k += 1
    return sequence

#сортировка Шелла с последовательностью Хиббарда
def shell_sort_hibbard(arr):
    n = len(arr)
    gaps = hibbard_sequence(n)
    
    for gap in reversed(gaps):
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)        
        
# Пирамидальная сортировка         
def heapify(arr, n, i):
    main = i
    left_child = (2 * i) + 1
    right_child = (2 * i) + 2

    if left_child < n and arr[left_child] > arr[main]:
        main = left_child
    if right_child < n and arr[right_child] > arr[main]:
        main = right_child

    if main != i:
        arr[i], arr[main] = arr[main], arr[i]
        heapify(arr, n, main)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
def fill_array(arr):
    for i in range(len(arr)):
        arr[i] = random.randint(-len(arr), len(arr))

def almost_sorted(q,_seed):
    a = [i for i in range(1,q-ceil((q*0.1))+1)]
    seed(_seed)
    for j in range(0, ceil(q*0.1)):
        a.append(randint(0, q//2))
    return a

def beg_sort(arr):
    current_value = random.randint(-len(arr), len(arr)) 
    for i in range(len(arr)):
        arr[i] = current_value
        step = random.randint(-len(arr), len(arr))
        current_value += step 

def back_sorted(arr):
    for i in range(len(arr)):
        arr[i] = random.randint(-len(arr), len(arr))
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
    
time_arr = []
x_arr = []
for i in range(0, 6001, 66):
    arr = [0] * i
    back_sorted(arr)
    #arr= almost_sorted(i,41) #когда нужен почти отсортированный массив
    start_time = time()
    heap_sort(arr) #менять название сортировки
    finish_time = time()
    time_arr.append(finish_time-start_time)
    x_arr.append(i)



p = np.polyfit(x_arr, time_arr, 2)
# Создаем фигуру для графиков
plt.figure(figsize=(10, 6))
plt.scatter(x_arr,time_arr)
# Настройка графика
plt.title('Обратно отсортированный массив')
plt.xlabel('Размер входных данных n')
plt.ylabel('Время выполнения T(n)')
plt.legend()  # Добавляем легенду
plt.grid()    # Добавляем сетку
# Показываем график
plt.plot(x_arr, np.polyval(p, x_arr), color='red')

plt.tight_layout()
plt.show()




