# bubbleSort
import time

def bubbleSort(arreglo):

    n = len(arreglo)
    for i in reversed(range(1, n)): #de n-1 hasta 1
        for j in range(i):  
            if arreglo[j] > arreglo[j + 1]: 

                temp = arreglo[j + 1]
                arreglo[j + 1] = arreglo[j]
                arreglo[j] = temp

    return arreglo


with open("Arreglo10000.txt", "r") as file:
    contenido = file.read()
arregloLeido = eval(contenido) 
start_time = time.time()  
sortedArray = (bubbleSort(arregloLeido))
end_time = time.time() 


elapsed_time = end_time - start_time
print("Sorted array:", sortedArray)
print(f"took {elapsed_time:.6f} seconds.")