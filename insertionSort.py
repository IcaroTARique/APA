#!/usr/bin/python3.5
#PARA RODAR O PROGRAMA  ./insertionSort.py
import sys
#coding=UTF-8

def insertionSort(lista, tamanho):

    for i in range (1,len(lista),1):
        menor = i
        #for j in range(0, i, -1): <== (FOR DANDO ERRO DESCONHECIDO)
        j = i - 1
        while j >= 0:
            if lista[menor] <lista[j]:

                aux = lista[menor]
                lista[menor] = lista[j]
                lista[j] = aux
            else:
                break
            #print (lista)
            j = j - 1
            menor = menor -1


#lista = [2,5,6,3,1,4]
#lista = [54,26,93,17,77,31,44,55,20]
#lista = ["a", "k", "b", "f", "z", "g", "d", "o"]
#print(lista)
#insertionSort(lista, len(lista))
#print(lista)

lista = []
nome = 'num.1000.1.in'
nome = sys.argv[1]
arq = open(nome, 'r')
#lista = ["a", "k", "b", "f", "z", "g", "d", "o"]
i = 0
for line in arq:
    convertido = int(line)
    lista.append(convertido)
    i = i + 1
arq.close()
insertionSort(lista, len(lista))
print(lista)