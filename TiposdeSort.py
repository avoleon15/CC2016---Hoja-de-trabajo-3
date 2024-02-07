#Alvaro Jose Leon Aguilar
#HDT 3
import time
import cProfile
import random
#1 gnome_sort
def gnome_sort(arr):
    index = 0
    n = len(arr)
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1
    return arr

#merge_sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

#quick_sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Usar una lista como pila para almacenar los límites de los subarreglos
    stack = [(0, len(arr) - 1)]
    
    while stack:
        # Obtener los límites del subarreglo actual de la pila
        low, high = stack.pop()
        
        if low < high:
            pivot = arr[high]
            i = low - 1
            
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            partition_index = i + 1
            
            # Agregar los límites de los subarreglos izquierdo y derecho a la pila
            stack.append((low, partition_index - 1))
            stack.append((partition_index + 1, high))
    
    return arr



#counting_sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(n):
        arr[i] = output[i]

#radix_sort
def radix_sort(arr):
    max_element = max(arr)
    exp = 1
    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

#selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#shell short
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
    return arr

#heapify
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

#heap sort
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


numeros_random = [random.randint(0,10000) for y in range(3000)]
numeros_ordenados = [random.randint(0,10000) for y in range(3000)]
numeros_ordenados = gnome_sort(numeros_ordenados)

menu = 0
tipo = 0

while menu != 8:
    print("""1. Gnome sort
2. Merge sort
3. Quick sort
4. Radix Sort
5. Selection Sort
6. Shell Sort
7. Heap Sort
8. Salir""")
    menu = int(input("Ingrese el numero del sort que quiere acceder: "))
    
    if menu == 1:
        start_time = time.time()
        sorted_data = gnome_sort(numeros_random)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        gnome_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        sorted_data = gnome_sort(numeros_random)[::-1]
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Descendente):", elapsed_time)
        start_time = time.time()
        gnome_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Descendente):", elapsed_time)
        start_time = time.time()
        sorted_data = gnome_sort(numeros_ordenados)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados:", elapsed_time)
        cProfile.run('gnome_sort(numeros_random)')

    elif menu == 2:
        start_time = time.time()
        sorted_data = merge_sort(numeros_random)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        merge_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        sorted_data = merge_sort(numeros_random)[::-1]
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Descendente):", elapsed_time)
        start_time = time.time()
        merge_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Descendente):", elapsed_time)
        start_time = time.time()
        sorted_data = gnome_sort(numeros_ordenados)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados:", elapsed_time)
        cProfile.run('merge_sort(numeros_random)')
        
    elif menu == 3:
        start_time = time.time()
        sorted_data = quick_sort(numeros_random)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        quick_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        sorted_data = quick_sort(numeros_random)[::-1]
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Descendente):", elapsed_time)
        start_time = time.time()
        quick_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Descendente):", elapsed_time)
        start_time = time.time()
        sorted_data = gnome_sort(numeros_ordenados)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados:", elapsed_time)
        cProfile.run('quick_sort(numeros_random)')
        
    elif menu == 4:
        start_time = time.time()
        sorted_data = counting_sort(numeros_random)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        counting_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        sorted_data = counting_sort(numeros_random)[::-1]
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Descendente):", elapsed_time)
        start_time = time.time()
        counting_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Descendente):", elapsed_time)
        start_time = time.time()
        sorted_data = gnome_sort(numeros_ordenados)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados:", elapsed_time)
        cProfile.run('counting_sort(numeros_random)')
        
    elif menu == 5:
        start_time = time.time()
        sorted_data = selection_sort(numeros_random)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        selection_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        sorted_data = selection_sort(numeros_random)[::-1]
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Descendente):", elapsed_time)
        start_time = time.time()
        selection_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Descendente):", elapsed_time)
        start_time = time.time()
        sorted_data = gnome_sort(numeros_ordenados)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados:", elapsed_time)
        cProfile.run('selection_sort(numeros_random)')
        
    elif menu == 6:
        start_time = time.time()
        sorted_data = shell_sort(numeros_random)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        shell_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        sorted_data = shell_sort(numeros_random)[::-1]
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Descendente):", elapsed_time)
        start_time = time.time()
        shell_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Descendente):", elapsed_time)
        start_time = time.time()
        sorted_data = gnome_sort(numeros_ordenados)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados:", elapsed_time)
        cProfile.run('shell_sort(numeros_random)')
        
    elif menu == 7:
        start_time = time.time()
        sorted_data = heap_sort(numeros_random)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        heap_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Ascendente):", elapsed_time)
        start_time = time.time()
        sorted_data = heap_sort(numeros_random)[::-1]
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos desordenados (Descendente):", elapsed_time)
        start_time = time.time()
        heap_sort(sorted_data)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados (Descendente):", elapsed_time)
        start_time = time.time()
        sorted_data = gnome_sort(numeros_ordenados)
        elapsed_time = time.time() - start_time
        print("Tiempo de ejecución para datos ya ordenados:", elapsed_time)
        cProfile.run('heap_sort(numeros_random)')
        
    elif menu == 8:
        print("Gracias por utilizar este programa.")
        break
    
    else:
        print("Ingrese una respuesta dentro de las opciones.")
