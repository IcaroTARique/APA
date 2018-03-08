#!/usr/bin/python3.5
import sys
#Compilar com --> Python3.5 insertionSort.py
#coding=UTF-8


lista = []
nome = sys.argv[1]
arq = open(nome, 'r')
#lista = ["a", "k", "b", "f", "z", "g", "d", "o"]

for line in arq:
    convertido = int(line)
    lista.append(convertido)
arq.close()
print(lista)
#print(lista)