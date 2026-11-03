"""

Esercizio 0 - Funzioni e Moduli
Creare il file python somme.py in cui vanno definite due funzioni:
una funzione che restituisca la somma dei primi n numeri naturali, con n da passare tramite un argomento;
una funzione che restituisca la somma delle radici dei primi n numeri naturali, con n da passare tramite un argomento.
Creare uno script python che importi il modulo somme appena creato e ne utilizzi le funzioni
Esaminare la cartella di lavoro


"""

#faccio uno script per utilizzare il modulo creato prima

import somme   #richiamo la funzione scrivendo somme.nome_funzione(...)

n = 10
print("Somma dei primi", n, "naturali:", somme.somma_naturali(n))
print("Somma delle radici dei primi", n, "naturali:", somme.somma_radici(n))
"""un alternativa puo essere importare direttamente le funzioni  from somme import somma_naturali, somma_radici print(somma_naturali(10)) print(somma_radici(10))"""


#nuove funzioni, funzione tutisco somma e prodotto
s,p = somme.somma_e_prodotto(n)
print("somma:", s, "prodotto:", p)

# funzione con somamtoria
print("somma potenze (alpha=1, default):", somme.somma_potenze(n))
print("Somma quadrati (alpha=2):", somme.somma_potenze(n, 2))
print("Somma cubi (alpha=3):", somme.somma_potenze(n, alpha=3))