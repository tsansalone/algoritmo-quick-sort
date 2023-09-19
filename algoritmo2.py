import random

def partition(A, start, end):
    i = start-1 #ponteiro da esquerda
    j = end+1 #ponteiro da direita

    pivot = A[(start+end)//2] #lógica de escolha de pivo pode ser implementada aqui
    
    while True:
        i+=1
        while (A[i] < pivot):
            i+=1 #move o ponteiro da esquerda uma posição a direita
        j-=1
        while (A[j]> pivot):
            j-=1 #move o ponteiro da direita uma posição a esquerda 
        if i>=j:
            print(f"Array parcial: {A[start:end+1:1]} Pivo = {pivot}")
            return j #o pivo está na posição correta        
        A[i], A[j] = A[j], A[i] #inverte os elementos se A[i] e A[j] forem maiores que o pivo
        # print(f"Array A after partition: {A}")

def quickSort(A, start, end):
    if start < end:
        p = partition(A, start, end) # p é o pivo, e agora ele está na posição correta, itens menores a esquerda e itens maiores a direita

        quickSort(A, start, p) #ordena o lado esquerdo recursivamente
        quickSort(A, p+1, end) #ordena o lado direito recursivamente


A = random.sample(range(0, 50), 10)
print(f"Array original: {A}")
quickSort(A, 0, len(A)-1)
print(f"Array ordenado: {A}")
