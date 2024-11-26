# quickSort
import time


def quickSort(arreglo):

   
    n = len(arreglo)
    
    if(n<=1):
        return arreglo

    ultimoElemento = arreglo[-1]

    izquierda = [x for x in arreglo[:-1] if x < ultimoElemento]
    derecha = [x for x in arreglo[:-1] if x >= ultimoElemento]

    return quickSort(izquierda) + [ultimoElemento] + quickSort(derecha)


 

def funcionSwap(arreglo, i, j):
    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]





with open("Arreglo10000.txt", "r") as file:
    contenido = file.read()
arregloLeido = eval(contenido) 
start_time = time.time()  
sortedArray = (quickSort(arregloLeido))
end_time = time.time() 


elapsed_time = end_time - start_time
print("Sorted array:", sortedArray)
print(f"took {elapsed_time:.6f} seconds.")