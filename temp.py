# -*- coding: utf-8 -*-

"""
Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları
birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi,
non-scalar verilerden de oluşabilir. Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""
liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def duzlestir(listem):
    if len(listem) == 0:
        return listem
    if isinstance(listem[0], list):
        return duzlestir(listem[0]) + duzlestir(listem[1:])
    return listem[:1] + duzlestir(listem[1:])


print(duzlestir(liste))

"""Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
 Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da 
 tersine döndürün. Örnek olarak:
     input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
    """
    
def tersine(birliste):
        
    for eleman in range(len(birliste)):
      
        birliste.reverse()
        if isinstance(birliste[eleman], list):
            birliste[eleman].reverse()
           
           
    return birliste
       
   
        
inp = [[1, 2], [3, 4], [5, 6, 7]]        
print(tersine(inp))