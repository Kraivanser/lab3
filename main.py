def bubble_sort(arr, order):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if order == "возрастанию":
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            elif order == "убыванию":
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

num = int(input("Введите количество чисел: "))
order = input("Хотите отсортировать числа по возрастанию или убыванию? ")
numbers = [int(input(f"Введите число #{i+1}: ")) for i in range(num)]

bubble_sort(numbers, order)
print(f"Отсортированный массив по {order}:", numbers)
