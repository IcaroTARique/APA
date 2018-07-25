#!/usr/bin/python3.6
#coding: utf-8
import sys
import time

class ordenaLista():
    def __init__(self,lista):
        self.lista = lista

    def leArquivo(self, nome):
        arq = open(nome, 'r')
        i = 0
        for line in arq:
            convertido = int(line)
            if i == 0:
                pass
            else:
                lista.append(convertido)
            i = i + 1
        arq.close()
        return lista

    def exibeLista(self):
        count = 0
        for i in range(len(self.lista)):
            print (self.lista[i],"\t ||\t" , end="")
            count += 1
            if count == 9:
                print("\n")
                count = 0

    def selectionSort (self):
        #for que movimenta o primeiro item de comparação
        for i in range(0, len(self.lista)):
            #definimos que o menor da lista é o inicial e depois vai modificando
            menor = self.lista[i]
            #for que movimenta o segundo item de comparação
            #OBS.: Sempre faz o for até o final, por isso o custo de O(n²)
            #tanto para melhor quanto para pior caso.
            for j in range (i,len(self.lista)):
                #compara se o "menor" é maior que o "atual do segundo for"
                if menor > self.lista[j]:
                    #Se "menor" for maior, colocamos o "atual do segundo for"
                    #na variável "menor"
                    menor = self.lista[j]
                    #Criamos o auxiliar para quando acabar o for atual podermos
                    #efetuar a troca
                    aux = j
            #Verifica se o item da lista[i] é diferente de menor, para não trocar
            #na ultima comparação
            if self.lista[i] != menor:
                #Executa a troca de posições
                aux2 = self.lista[i]
                self.lista[i] = menor
                self.lista[aux] = aux2

### MAIN ###
lista = []

objLista = ordenaLista(lista)
objLista.leArquivo(sys.argv[1])
objLista.exibeLista()
print("\n------------------------------------------- ORDENADO -------------------------------------------")

inicio = time.time()
objLista.selectionSort()
fim = time.time()
objLista.exibeLista()
print("\n",fim - inicio, " segundos")