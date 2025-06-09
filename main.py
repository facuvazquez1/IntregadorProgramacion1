# main.py
# Simula catálogo de biblioteca: menú interactivo con generación, orden y búsqueda.

import random
import timeit
from ordenamiento import bubble_sort, quick_sort
from busqueda import linear_search, binary_search

def generar_catalogo(n=1000):
    """
    Genera lista de n ISBN (13 dígitos) aleatorios y únicos.
    """
    if not (isinstance(n, int) and n > 0):
        raise ValueError("generar_catalogo: n debe ser entero positivo")
    catalogo = set()
    while len(catalogo) < n:
        isbn = random.randint(10**12, 10**13 - 1)
        catalogo.add(isbn)
    return list(catalogo)

def medir_tiempo(func, *args, repeats=5):
    """
    Mide tiempo promedio de func(*args) en segundos.
    Captura errores para no interrumpir la simulación.
    """
    try:
        timer = timeit.Timer(lambda: func(*args))
        tiempos = timer.repeat(repeat=repeats, number=1)
        return sum(tiempos) / repeats
    except Exception as e:
        print(f"[Error medir_tiempo {func.__name__}]: {e}")
        return None

def mostrar_tiempos_completos():
    """
    Genera un catálogo, selecciona un ISBN de prueba y muestra
    los tiempos de ordenamiento y búsqueda.
    """
    catalogo = generar_catalogo()
    objetivo = catalogo[random.randrange(len(catalogo))]

    # Bubble Sort
    copia_b = catalogo[:]
    t_b = medir_tiempo(bubble_sort, copia_b)

    # Quick Sort
    copia_q = catalogo[:]
    t_q = medir_tiempo(quick_sort, copia_q)

    # Búsqueda Lineal
    t_lin = medir_tiempo(linear_search, catalogo, objetivo)

    # Búsqueda Binaria
    ordenado = quick_sort(catalogo)
    t_bin = medir_tiempo(binary_search, ordenado, objetivo)

    print(f"\nISBN de prueba: {objetivo}")
    print(f"Bubble Sort: {t_b:.6f} s" if t_b is not None else "Bubble Sort: error")
    print(f"Quick Sort:  {t_q:.6f} s" if t_q is not None else "Quick Sort: error")
    print(f"Lineal:      {t_lin:.6f} s" if t_lin is not None else "Lineal: error")
    print(f"Binaria:     {t_bin:.6f} s\n")

def menu():
    """
    Menú principal para interactuar con el catálogo:
    1) Mostrar todos los tiempos
    2) Medir solo Bubble Sort
    3) Medir solo Quick Sort
    4) Buscar un ISBN
    5) Salir
    """
    while True:
        print("=== Menú de Gestión de Catálogo ===")
        print("1) Generar catálogo y ver todos los tiempos")
        print("2) Ordenar con Bubble Sort (y ver tiempo)")
        print("3) Ordenar con Quick Sort (y ver tiempo)")
        print("4) Buscar ISBN (lineal o binaria)")
        print("5) Salir")
        opc = input("Elige una opción (1-5): ").strip()

        if opc == "1":
            mostrar_tiempos_completos()

        elif opc == "2":
            cat = generar_catalogo()
            t = medir_tiempo(bubble_sort, cat)
            print(f"\nBubble Sort: {t:.6f} s\n" if t is not None else "\nBubble Sort: error\n")

        elif opc == "3":
            cat = generar_catalogo()
            t = medir_tiempo(quick_sort, cat)
            print(f"\nQuick Sort: {t:.6f} s\n" if t is not None else "\nQuick Sort: error\n")

        elif opc == "4":
            cat = generar_catalogo()
            ordenado = quick_sort(cat)
            isbn_str = input("Ingresa ISBN a buscar: ").strip()
            try:
                isbn = int(isbn_str)
                metodo = input("Método (L=lineal / B=binaria): ").upper()
                if metodo == "L":
                    idx = linear_search(cat, isbn)
                else:
                    idx = binary_search(ordenado, isbn)
                msg = f"ISBN encontrado en posición {idx}" if idx != -1 else "ISBN no encontrado"
                print(f"\n{msg}\n")
            except ValueError:
                print("\nISBN inválido. Debe ser un número entero.\n")

        elif opc == "5":
            print("Saliendo...")
            break

        else:
            print("\nOpción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    menu()
