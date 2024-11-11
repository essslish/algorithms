import matplotlib.pyplot as plt
import numpy as np
from time import time
import random
from time import *
from random import randint, seed
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Строим кучу (максимальную кучу)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлекаем элементы из кучи один за другим
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

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

def quick_sort(arr): #быстрая
    if len(arr) > 1:
        random_index = arr[randint(0, len(arr)-1)]
        less = [x for x in arr if x < random_index]
        equal = [x for x in arr if x == random_index]
        great = [x for x in arr if x > random_index]
        arr = quick_sort(less) + equal + quick_sort(great)
    return arr


def back_sorted(arr):
    arr.sort(reverse=True)

def plot_complexity():
    sizes = np.arange(1, 16001, 66)
    time_arr_bubble = []
    time_arr_selection = []
    time_arr_insertion = []
    time_arr_merge = []
    time_arr_heap = []
    time_arr_shell = []
    time_arr_quick = []
    time_arr_shell_hibbard = []
    time_arr_shell_pratt = []
    x_arr = sizes

    for i in sizes:
        arr = [0] * i
        back_sorted(arr)

        # Измеряем время для пузырьковой сортировки
        start_time = time()
        bubble_sort(arr.copy())
        finish_time = time()
        time_arr_bubble.append(finish_time - start_time)

        # Измеряем время для сортировки выбором
        start_time = time()
        selection_sort(arr.copy())
        finish_time = time()
        time_arr_selection.append(finish_time - start_time)

        # Измеряем время для сортировки вставкой
        start_time = time()
        insertion_sort(arr.copy())
        finish_time = time()
        time_arr_insertion.append(finish_time - start_time)

        # Измеряем время для сортировки слиянием
        start_time = time()
        merge_sort(arr.copy())
        finish_time = time()
        time_arr_merge.append(finish_time - start_time)

        # Измеряем время для пирамидальной сортировки
        start_time = time()
        heapSort(arr.copy())
        finish_time = time()
        time_arr_heap.append(finish_time - start_time)

        # Измеряем время для сортировки Шелла
        start_time = time()
        shell_sort(arr.copy())
        finish_time = time()
        time_arr_shell.append(finish_time - start_time)

        # Измеряем время для Хибборда
        start_time = time()
        shell_sort_hibbard(arr.copy())
        finish_time = time()
        time_arr_shell_hibbard.append(finish_time - start_time)

        # Измеряем время для Пратта
        start_time = time()
        shell_sort_pratt(arr.copy())
        finish_time = time()
        time_arr_shell_pratt.append(finish_time - start_time)

        # Измеряем время для быстрой сортировки
        start_time = time()
        quick_sort(arr.copy())
        finish_time = time()
        time_arr_quick.append(finish_time - start_time)

    # Построение графика
    plt.figure(figsize=(10, 6))

    # Добавляем точки для пузырьковой сортировки
    plt.scatter(x_arr, time_arr_bubble, label="Пузырьковая сортировка (O(n^2))", s=10, marker='o')

    # Добавляем точки для сортировки выбором
    plt.scatter(x_arr, time_arr_selection, label="Сортировка выбором (O(n^2))", s=10, marker='x')

    # Добавляем точки для сортировки вставкой
    plt.scatter(x_arr, time_arr_insertion, label="Сортировка вставкой (O(n^2))", s=10, marker='^')

    # Добавляем точки для сортировки слиянием
    plt.scatter(x_arr, time_arr_merge, label="Сортировка слиянием (O(n log n))", s=10, marker='s')

    # Добавляем точки для пирамидальной сортировки
    plt.scatter(x_arr, time_arr_heap, label="Пирамидальная сортировка (O(n log n))", s=10, marker='d')

    # Добавляем точки для сортировки Шелла
    plt.scatter(x_arr, time_arr_shell, label="Сортировка Шелла (O(n log n))", s=10, marker='*')

    # Добавляем точки для сортировки Хибборда
    plt.scatter(x_arr, time_arr_shell_hibbard, label="Сортировка Шелла по Хиббарду (O(n^(3/2)))", s=10, marker='^')

    # Добавляем точки для сортировки Пратта
    plt.scatter(x_arr, time_arr_shell_pratt, label="Сортировка Шелла по Пратту (O(n log^2 n))", s=10, marker='o')

    # Добавляем точки для быстрой сортировки
    plt.scatter(x_arr, time_arr_quick, label="Быстрая сортировка (O(n log n))", s=10, marker='p')

    # Добавляем полиномиальную аппроксимацию
    p_bubble = np.polyfit(x_arr, time_arr_bubble, 2)
    plt.plot(x_arr, np.polyval(p_bubble, x_arr), color='blue', label="Пузырьковая сортировка (O(n^2))")

    p_merge = np.polyfit(x_arr, time_arr_merge, 1)
    plt.plot(x_arr, np.polyval(p_merge, x_arr), color='red', label="Сортировка слиянием(n log n)")

    p_selection = np.polyfit(x_arr, time_arr_selection, 2)
    plt.plot(x_arr, np.polyval(p_selection, x_arr), color='orange', label="Сортировка выбором (O(n^2))")

    p_insertion = np.polyfit(x_arr, time_arr_insertion, 2)
    plt.plot(x_arr, np.polyval(p_insertion, x_arr), color='green', label="Сортировка вставкой (O(n^2))")

    p_heap = np.polyfit(x_arr, time_arr_heap, 1)
    plt.plot(x_arr, np.polyval(p_heap, x_arr), color='purple', label="Пирамидальная сортировка (O(n log n))")

    p_shell = np.polyfit(x_arr, time_arr_shell, 1)
    plt.plot(x_arr, np.polyval(p_shell, x_arr), color='brown', label="Сортировка Шелла (O(n log n))")

    p_shell_h = np.polyfit(x_arr, time_arr_shell_hibbard, 2)
    plt.plot(x_arr, np.polyval(p_shell_h, x_arr), color='black', label="Сортировка Шелла по Хибборду (O(n^(3/2)))")

    p_shell_p = np.polyfit(x_arr, time_arr_shell_pratt, 1)
    plt.plot(x_arr, np.polyval(p_shell_p, x_arr), color='grey', label="Сортировка Шелла по Пратту (O(n log^2 n))")

    p_quick = np.polyfit(x_arr, time_arr_quick, 1)
    plt.plot(x_arr, np.polyval(p_quick, x_arr), color='pink', label="Быстрая сортировка (O(n log n))")

    plt.xlabel("Размер массива (n)")
    plt.ylabel("Время выполнения (сек)")
    plt.title("Временная сложность алгоритмов сортировки")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_complexity()
