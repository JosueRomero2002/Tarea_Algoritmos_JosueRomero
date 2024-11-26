#  Insertion Sort
import time

def insertionSort(arreglo):
    n = len(arreglo)

    for i in range(1, n):
        elementoActual = arreglo[i]
        j = i - 1

        while j >= 0 and arreglo[j] > elementoActual:
            arreglo[j+1] = arreglo[j]
            j= j - 1

        arreglo[ j+1] = elementoActual

    return arreglo





with open("Arreglo10000.txt", "r") as file:
    contenido = file.read()
arregloLeido = eval(contenido) 
start_time = time.time()  
sortedArray = (insertionSort(arregloLeido))
end_time = time.time() 


elapsed_time = end_time - start_time
print("Sorted array:", sortedArray)
print(f"took {elapsed_time:.6f} seconds.")