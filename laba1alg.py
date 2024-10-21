#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
import time
import matplotlib
import matplotlib.pyplot as plt
from collections import defaultdict
                
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
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
def fill_array(arr):
    for i in range(len(arr)):
        arr[i] = random.randint(-len(arr), len(arr))

def almost_sorted(arr):
    sorted_array = list(range(len(arr)))
    num_unsorted_elements = len(arr) // 10
    random_idx = random.sample(range(len(arr)), num_unsorted_elements)
    for idx in random_idx:
        swap_with = random.randint(0, len(arr)-1)
        sorted_array[idx], sorted_array[swap_with] = sorted_array[swap_with], sorted_array[idx]
    return sorted_array

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
    
def running_time(action, arr):
    start_time = time.time()
    action(arr)
    return (time.time() - start_time) * 1000 

def display_statistics():
    results = defaultdict(int)
    results1 = defaultdict(int)
    results2 = defaultdict(int)
    results3 = defaultdict(int)

    # Сбор результатов - в running_time поменять на функцию нужной сортировки
    for i in range(1000, 10000, 200):
        ar = [0] * i
        fill_array(ar)
        results[i] = running_time(selection_sort, ar)
    for i in range(1000, 10000, 200):
        ar1 = [0] * i
        beg_sort(ar1)
        results1[i] = running_time(selection_sort, ar1)
    for i in range(1000, 10000, 200):
        ar2 = [0] * i
        almost_sorted(ar2)
        results2[i] = running_time(selection_sort, ar2)
    for i in range(10000, 1000, -200):
        ar3 = [0] * i
        back_sorted(ar3)
        results3[i] = running_time(selection_sort, ar3)

    # Обработка данных для графика
    sizes = list(results.keys())
    times = list(results.values())
    
    sizes1 = list(results1.keys())
    times1 = list(results1.values())
    
    sizes2 = list(results2.keys())
    times2 = list(results2.values())
    
    sizes3 = list(results3.keys())
    times3 = list(results3.values())

    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 4, 1) 
    plt.plot(sizes, times, label='Для произвольного массива', marker='o')
    plt.title('Время сортировки в зависимости от размера массива')
    plt.xlabel('Размер массива')
    plt.ylabel('Время сортировки, мс')
    plt.legend()
    plt.grid()
    
    plt.subplot(1, 4, 2)  
    plt.plot(sizes1, times1, label='Для отсортированного массива', marker='o')
    plt.title('Время сортировки в зависимости от размера массива')
    plt.xlabel('Размер массива')
    plt.ylabel('Время сортировки, мс')
    plt.legend()
    plt.grid()
    
    plt.subplot(1, 4, 3) 
    plt.plot(sizes2, times2, label='Для почти отсортированного массива', marker='o')
    plt.title('Время сортировки в зависимости от размера массива')
    plt.xlabel('Размер массива')
    plt.ylabel('Время сортировки, мс')
    plt.legend()
    plt.grid()
    
    plt.subplot(1, 4, 4)  
    plt.plot(sizes3, times3, label='Для массива, отсортированного обратно', marker='o')
    plt.title('Время сортировки в зависимости от размера массива')
    plt.xlabel('Размер массива')
    plt.ylabel('Время сортировки, мс')
    plt.legend()
    plt.grid()
   

    plt.tight_layout()  # Компактное размещение графиков
    plt.show()

if __name__ == "__main__":
    display_statistics()


# In[ ]:





# In[ ]:




