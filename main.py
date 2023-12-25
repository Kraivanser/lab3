def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

num = int(input("Введите количество чисел: "))
numbers = [int(input(f"Введите число #{i+1}: ")) for i in range(num)]

bubble_sort(numbers)
print("Отсортированный массив по возрастанию:", numbers)

