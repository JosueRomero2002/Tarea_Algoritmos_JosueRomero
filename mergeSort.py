# mergeSort
import time

def mergeSort(arreglo):
    puntoMedio = len(arreglo) // 2

    if(puntoMedio < 1):
        return arreglo

    arreglo =funcionMerge( mergeSort(arreglo[:puntoMedio]), mergeSort(arreglo[puntoMedio:]))
    
    return arreglo



def funcionMerge(izquierda, derecha):
    resultado = []
    i = j = 0

    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1


    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])


    return resultado



with open("Arreglo10000.txt", "r") as file:
    contenido = file.read()
arregloLeido = eval(contenido) 
start_time = time.time()  
sortedArray = (mergeSort(arregloLeido))
end_time = time.time() 


elapsed_time = end_time - start_time
print("Sorted array:", sortedArray)
print(f"took {elapsed_time:.6f} seconds.")