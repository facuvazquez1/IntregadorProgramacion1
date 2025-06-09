# TP: Gestión de Catálogo de Biblioteca en Python

## Descripción

Este proyecto simula la **gestión de un catálogo de biblioteca**:

* Genera 1 000 **ISBN (International Standard Book Number)** aleatorios (13 dígitos), identificador único para libros y ediciones que facilita su catalogación y búsqueda.
* Ordena el catálogo con dos algoritmos (Bubble Sort y Quick Sort).
* Busca un ISBN concreto con búsqueda lineal y binaria.
* Mide los tiempos de cada operación para comparar eficiencia.

## Módulos

* **ordenamiento.py**: Bubble Sort y Quick Sort genéricos.
* **busqueda.py**: Búsqueda lineal y binaria.
* **main.py**: Simula datos, mide tiempos, muestra resultados y ofrece un menú interactivo.

> **Nota**: Al importar módulos, Python crea la carpeta `__pycache__` para almacenar archivos compilados (`.pyc`), acelerando ejecuciones posteriores.

## Caso práctico

En bibliotecas físicas o digitales, es frecuente:

1. Mantener catálogos extensos de libros (ISBN).
2. Ordenarlos para generación de listados o interfaces de usuario.
3. Buscar rápidamente un libro por su ISBN.

Con esta simulación, observamos:

* El coste de mantener catálogos grandes.
* La necesidad de algoritmos eficientes.

## Uso

1. Clona o descarga este repositorio.
2. Ejecuta el programa en terminal:

   ```bash
   python main.py
   ```
3. Al iniciarse, verás un **menú interactivo** con estas opciones:

   1. **Generar catálogo y ver todos los tiempos**: genera 1 000 ISBN y mide los tiempos de Bubble Sort, Quick Sort, búsqueda lineal y búsqueda binaria.
   2. **Ordenar con Bubble Sort**: genera un catálogo nuevo y muestra el tiempo de ejecución de Bubble Sort.
   3. **Ordenar con Quick Sort**: genera un catálogo nuevo y muestra el tiempo de ejecución de Quick Sort.
   4. **Buscar ISBN**: ingresa un ISBN y elige **L** (lineal) o **B** (binaria); el programa mostrará la posición o indicará si no se encuentra.
   5. **Salir**: finaliza la ejecución.

Al seleccionar una opción, sigue las instrucciones en pantalla para ver los resultados y tiempos de cada operación.

## Comparativa de eficiencia

### n = 1 000 (1 000 ítems)

| Operación    | Algoritmo   | Complejidad | Tiempo aproximado (n=1 000) |
| ------------ | ----------- | ----------- | --------------------------- |
| Ordenamiento | Bubble Sort | O(n²)       | 0.1 – 0.5 s                 |
| Ordenamiento | Quick Sort  | O(n log n)  | 0.005 – 0.02 s              |
| Búsqueda     | Lineal      | O(n)        | 0.0001 – 0.001 s            |
| Búsqueda     | Binaria     | O(log n)    | 0.00001 – 0.0001 s          |

### n = 10 000 (10 000 ítems)

| Operación    | Algoritmo   | Complejidad | Tiempo aproximado (n=10 000) |
| ------------ | ----------- | ----------- | ---------------------------- |
| Ordenamiento | Bubble Sort | O(n²)       | 10 – 50 s                    |
| Ordenamiento | Quick Sort  | O(n log n)  | 0.07 – 0.3 s                 |
| Búsqueda     | Lineal      | O(n)        | 0.001 – 0.01 s               |
| Búsqueda     | Binaria     | O(log n)    | 0.00002 – 0.0002 s           |

*Los tiempos son aproximados y pueden variar según el hardware.*

## Reflexiones

* Para catálogos pequeños (< 1 000 ítems), Bubble Sort puede ser aceptable.
* En grandes volúmenes (> 10 000 ítems), Quick Sort o algoritmos más avanzados (Timsort) son preferibles.
* La búsqueda binaria requiere lista ordenada: O(log n), mucho más rápido que la búsqueda lineal O(n).
* En aplicaciones reales, Python utiliza Timsort y estructuras de datos como diccionarios para optimizar ordenamientos y búsquedas.

## Vídeo explicativo en YouTube

* Link a Video de Youtube:
