# busqueda.py
# Búsqueda lineal y binaria en listas de valores comparables.

def linear_search(arr, target):
    """
    Recorre arr buscando target. Devuelve índice o -1.
    """
    if not isinstance(arr, list):
        raise TypeError("linear_search: se espera una lista")
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

def binary_search(arr, target):
    """
    Busca target en arr ordenada. Devuelve índice o -1.
    """
    if not isinstance(arr, list):
        raise TypeError("binary_search: se espera una lista")
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
