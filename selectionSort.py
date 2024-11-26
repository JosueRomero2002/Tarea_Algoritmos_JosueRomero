# selectionSort
import time

def selectionSort(arreglo):

    n = len(arreglo)
    
    
    for i in range(0,n):
        limiteIzquierdo = i

        for j in range(i+1, n):
              if arreglo[j] < arreglo[limiteIzquierdo]:
                limiteIzquierdo = j
        
        funcionSwap(arreglo, i, limiteIzquierdo)

    return arreglo

def funcionSwap(arreglo, i, j):
    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]






with open("Arreglo10000.txt", "r") as file:
    contenido = file.read()
arregloLeido = eval(contenido) 
start_time = time.time()  
sortedArray = (selectionSort(arregloLeido))
end_time = time.time() 


elapsed_time = end_time - start_time
print("Sorted array:", sortedArray)
print(f"took {elapsed_time:.6f} seconds.")