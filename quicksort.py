def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Выбираем опорный элемент
    left = [x for x in arr if x < pivot]  # Подмассив всех элементов меньше опорного
    middle = [x for x in arr if x == pivot]  # Подмассив всех элементов равных опорному
    right = [x for x in arr if x > pivot]  # Подмассив всех элементов больше опорного

    return quicksort(left) + middle + quicksort(right)


arr = [3, 6, 8, 10, 1, 2, 1]
print("Исходный массив:", arr)
sorted_arr = quicksort(arr)
print("Отсортированный массив:", sorted_arr)


def mark_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]["средний балл"]  # Обращение к ключу в генераторе списоков нужно только в условиях
    left = [x for x in arr if x["средний балл"] < pivot]
    middle = [x for x in arr if x["средний балл"] == pivot]
    right = [x for x in arr if x["средний балл"] > pivot]

    return mark_sort(left) + middle + mark_sort(right)


students = [
    {"имя": "Анна", "средний балл": 4.5},
    {"имя": "Владимир", "средний балл": 3.9},
    {"имя": "Елена", "средний балл": 4.8},
    {"имя": "Петр", "средний балл": 4.2},
    {"имя": "Иван", "средний балл": 4.0}
]

mark = mark_sort(students)
for student in mark:
    print(student)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sq = [x ** 2 for x in numbers if x % 2 == 0]

print(even_sq)

# Задача: Дан список пар (кортежей) целых чисел.
# Каждая пара представляет собой координаты точки на плоскости.
# Необходимо отсортировать список так,
# чтобы точки были упорядочены по расстоянию от начала координат в порядке возрастания.

# Пример:
# Исходный список:
# points = [(3, 4), (1, 2), (5, 6), (2, 2), (0, 1)]
# Ожидаемый результат:
# sorted_points = [(0, 1), (1, 2), (2, 2), (3, 4), (5, 6)]

import math


def distance_from_origin(point):
    return math.sqrt(point[0] ** 2 + point[1] ** 2)


def quick_sort_by_distance(points):
    if len(points) <= 1:
        return points

    pivot = points[len(points) // 2]
    left = [point for point in points if distance_from_origin(point) < distance_from_origin(pivot)]
    middle = [point for point in points if distance_from_origin(point) == distance_from_origin(pivot)]
    right = [point for point in points if distance_from_origin(point) > distance_from_origin(pivot)]

    return quick_sort_by_distance(left) + quick_sort_by_distance(middle) + quick_sort_by_distance(right)


points = [(3, 4), (1, 2), (5, 6), (2, 2), (0, 1)]

sorted_points = quick_sort_by_distance(points)
print(sorted_points)
