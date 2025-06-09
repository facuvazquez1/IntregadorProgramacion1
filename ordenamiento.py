# ordenamiento.py
# Bubble Sort y Quick Sort aplicables a listas de valores comparables.

def bubble_sort(arr):
    """Ordena in-place. Requiere lista."""
    if not isinstance(arr, list):
        raise TypeError("bubble_sort: se espera una lista")
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr):
    """Devuelve lista nueva ordenada. Requiere lista."""
    if not isinstance(arr, list):
        raise TypeError("quick_sort: se espera una lista")
    if len(arr) < 2:
        return arr[:]
    pivot = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivot]
    iguales = [x for x in arr if x == pivot]
    mayores = [x for x in arr if x > pivot]
    return quick_sort(menores) + iguales + quick_sort(mayores)
