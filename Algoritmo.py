def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[-1]
        menor = [x for x in arr[0:-1] if x <= pivo]
        maior = [x for x in arr[0:-1] if x > pivo]
        
        return quick_sort(menor) + [pivo] + quick_sort(maior)

lista = input().split(" ")
lista = [int(x) for x in lista]
lista_ordenada = quick_sort(lista)
print(lista_ordenada)