#creo un file python contenente due funzioni, ognuna con un argomento n

import sys,os
import numpy as np
import math


#somma dei primi n numeri naturali

def somma_naturali(n):
    totale = 0
    for i in range(1, n+1):
        totale += i
    return totale

#somma delle radici dei primi n numeri naturali

def somma_radici(n):
    totale = 0
    for i in range(1, n+1):
        totale += math.sqrt(i)
    return totale

#Una funzione che restituisce sia la somma sia il prodotto dei primi n numeri naturali (quindi due valori in uscita).

def somma_e_prodotto(n):
    somma = 0
    prodotto = 1    #Il prodotto deve partire da 1 e il ciclo da 1: se partissi da 0, il prodotto sarebbe sempre 0.
    for i in range(1, n+1):
        somma +=i
        prodotto *= i
    return somma, prodotto


#Una funzione che calcola la somma ∑ᵢ₌₀ⁿ iᵅ, cioè 0^α + 1^α + 2^α + ... + n^α, dove α è un argomento opzionale con valore di default 1.

def somma_potenze(n, alpha=1):   #alpha è di default 1 dalla consegna dell'esercizio
    totale = 0
    for i in range(0, n+1): #la sommatoria parte da 0, come indica i=0 nella formula
       totale += i**alpha
    return totale

