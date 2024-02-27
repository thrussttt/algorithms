# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1
#
#
# def get_target():
#     target = int(input("Введите число для поиска: "))
#     return target
#
#
# def get_arr():
#     arr_str = input("Введите список чисел через пробел для поиска: ")
#     split_arr = arr_str.split()
#     return [int(num) for num in split_arr]
#
#
# split_arr = get_arr()
# target = get_target()
# result = binary_search(split_arr, target)
#
# if result != -1:
#     print(f"Элемент {target} найден по индексу {result}")
# else:
#     print(f"Элемент {target} не найден в массиве")
#
#
# # Задача на бинарный поиск:
# #
# # Представьте, что у вас есть отсортированный список целых чисел,
# # который представляет собой оценки студентов по математике.
# # Ваша задача - написать программу, которая будет искать оценку студента по его имени.
# # Для этого вы можете использовать два списка:
# # один для имен студентов и другой для соответствующих оценок.
# #
# # Задача программы:
# #
# # Принять имя студента от пользователя.
# # Выполнить бинарный поиск по списку имен студентов, чтобы найти индекс, соответствующий введенному имени.
# # Если имя найдено, вывести оценку этого студента. Если нет, сообщить, что студент не найден.
#
#
# def binary_search(student_names, target_name, grades):
#     left, right = 0, len(student_names) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if student_names[mid] == target_name:
#             return grades[mid]
#         elif student_names[mid] < target_name:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return None
#
#
# # Данные
# student_names = ["Анна", "Василий", "Григорий", "Екатерина", "Михаил"]
# grades = [75, 82, 90, 68, 95]
#
# # Ввод имени студента
# target_name = input("Введите имя студента: ")
#
# # Поиск оценки с помощью бинарного поиска
# grade = binary_search(student_names, target_name, grades)
#
# # Вывод результата
# if grade is not None:
#     print(f"{target_name} получил(а) оценку {grade} по математике.")
# else:
#     print(f"Студент с именем {target_name} не найден.")


def sorted_arr(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True


def binary_s(arr, target):
    if sorted_arr(arr) is False:
        return False
    else:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1

        return -1


my_list = [1, 2, 3, 4, 45, 63, 78, 93, 1001]
print(binary_s(my_list, 63))
