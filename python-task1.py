import random
import numpy as np


def find_max(array):
    max_n = array[0]
    for i in range(1, len(array)):
        if array[i] > max_n:
            max_n = array[i]
    return max_n


def find_min(array):
    min_n = array[0]
    for i in range(1, len(array)):
        if array[i] < min_n:
            min_n = array[i]
    return min_n


def find_mean(array):
    mean_n = 0
    for i in range(len(array)):
        mean_n = mean_n + array[i]
    mean_n = mean_n / len(array)
    return mean_n

if __name__ == "__main__":
    # забиваем массив числами
    mas = [random.random() for _ in range(100)]
    # Простое решение
    print("Simple solution: Built-in functions + NumPy")
    print("Max num:", max(mas))
    print("Min num:", min(mas))
    print("Avg num:", sum(mas) / len(mas))
    print("NumPy Avg", np.mean(mas))
    
    # Всё ещё простое, но ручное решение
    print("\nWonky: Gently made by hand")
    print("Max num:", find_max(mas))
    print("Min num:", find_min(mas))
    print("Avg num:", find_mean(mas))
    print("---Job's done!---")
