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

    def insertionSort (self):
        for i in range (1,len(self.lista)):
            menor = i
            j = i - 1
            while j >= 0:
                if self.lista[menor] < lista[j]:
                    aux = self.lista[menor]
                    self.lista[menor] = lista[j]
                    self.lista[j] = aux
                else:
                    break
                j = j - 1
                menor = menor -1

### MAIN ###
lista = []

objLista = ordenaLista(lista)
objLista.leArquivo(sys.argv[1])
objLista.exibeLista()
print("\n------------------------------------------- ORDENADO -------------------------------------------")

inicio = time.time()
objLista.insertionSort()
fim = time.time()
objLista.exibeLista()
print("\n",fim - inicio, " segundos")