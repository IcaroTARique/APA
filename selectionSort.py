#!/usr/bin/python3.5
#PARA RODAR O PROGRAMA  ./selectionSort.py
import sys
#coding=UTF-8

#Função que chama o algorítmo de ordenação
def selectionSort(lista, tamanho):

    #for que movimenta o primeiro item de comparação
    for i in range(0, len(lista), 1):
        #definimos que o menor da lista é o inicial e depois vai modificando
        menor = lista[i]
        #for que movimenta o segundo item de comparação
        #OBS.: Sempre faz o for até o final, por isso o custo de O(n²)
        #tanto para melhor quanto para pior caso.
        for j in range (i,len(lista), 1):
            #compara se o "menor" é maior que o "atual do segundo for"
            if menor > lista[j]:
                #Se "menor" for maior, colocamos o "atual do segundo for"
                #na variável "menor"
                menor = lista[j]
                #Criamos o auxiliar para quando acabar o for atual podermos
                #efetuar a troca
                aux = j
        #Verifica se o item da lista[i] é diferente de menor, para não trocar
        #na ultima comparação
        if lista[i] != menor:
            #Executa a troca de posições
            aux2 = lista[i]
            lista[i] = menor
            lista[aux] = aux2


#lista = [2,5,6,3,1,4]
#lista = [54,26,93,17,77,31,44,55,20]
#lista = ["a", "k", "b", "f", "z", "g", "d", "o"]
#print(lista)
#selectionSort(lista, len(lista))
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
selectionSort(lista, len(lista))
print(lista)