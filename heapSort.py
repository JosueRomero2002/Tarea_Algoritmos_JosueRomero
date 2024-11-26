# heapSort
import time


def balancearArbol(arreglo, n, i):
    Padre = i
    hijoIzquierdo = (2 * i) + 1
    hijoDerecho = (2 * i ) + 2

    if hijoIzquierdo < n and arreglo[hijoIzquierdo] > arreglo[Padre]:
        Padre = hijoIzquierdo


    if hijoDerecho < n and arreglo[hijoDerecho] > arreglo[Padre]:
        Padre = hijoDerecho




    if Padre != i:
        arreglo[i], arreglo[Padre] = arreglo[Padre], arreglo[i]
        balancearArbol(arreglo, n, Padre)
        


def heapSort(arreglo):

    n = len(arreglo)

    contadori = (n // 2) - 1 
    while contadori >= 0:
        balancearArbol(arreglo, n, contadori)
        contadori -=1

    

    for i in reversed(range(1, n)): #de n-1 hasta 1
        arreglo[0], arreglo[i] = arreglo[i], arreglo[0] 
        balancearArbol(arreglo, i, 0)
    
    return arreglo




with open("Arreglo10000.txt", "r") as file:
    contenido = file.read()
arregloLeido = eval(contenido) 
start_time = time.time()  
sortedArray = (heapSort(arregloLeido))
end_time = time.time() 


elapsed_time = end_time - start_time
print("Sorted array:", sortedArray)
print(f"took {elapsed_time:.6f} seconds.")