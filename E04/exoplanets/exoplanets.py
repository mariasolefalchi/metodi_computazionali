"""Per ogni richiesta che segue mostrare il grafico per i pianeti extrasolari e per quelli del Sistema Solore (opportunamente identificati).

Creare un secondo script python che:

legga il file ExoplanetsPars_2025.csv e crei il DataFrame pandas corrispondente;
    suggerimento: usare l'opzione comment='#'
stampi il nome delle colonne del DataFrame;
stampi un estratto del contenuto del DataFrame;
produca un grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale;
    suggerimento: usare pyplot.scatter;
produca un grafico con assi logaritmici della grandezza 
 in funzione del periodo orbitale;
: Orbit Semi-Major Axis
: Stellar Mass
produca un grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale distinguendo gli esopianeti per metodo di scoperta (Transit o Radial Velocity) con la corrispondente legenda (gli altri tipi di esopianeti non vanno considerate nel grafico);
    suggerimento: usare .loc per la serezione dei valori nel DataFrame;
    suggerimento: usare l'opzione alpha per la trasparenza;
produca l'istogramma sovrapposto della massa del pianeta distinguendo gli esopianeti per metodo di scoperta (Transit o Radial Velocity) con la corrispondente legenda con la relativa legenda;
    suggerimento: usare pyplot.hist definendo lo stesso numero di bin e lo stesso intervallo per l'asse x;
    suggerimento: usare l'opzione alpha per la trasparenza;
produca un grafico analogo al precedente per il logaritmo in base 10 della massa del pianeta. """


#############################################################################
# Cosa fa lo script:
#   1. legge il catalogo di esopianeti da un file CSV (con pandas)
#   2. definisce a mano i parametri dei pianeti del Sistema Solare (numpy)
#   3. produce tre grafici scatter separati (matplotlib)
#   4. produce una figura composita 2x2: scatter + istogrammi laterali
#############################################################################


# IMPORT DELLE LIBRERIE
import sys, os                      # moduli standard (qui non vengono usati)
import numpy as np                  # array numerici, funzioni matematiche (log10, ...)
import pandas as pd                 # DataFrame: tabelle di dati con colonne con nome

import matplotlib.pyplot as plt     # interfaccia "pyplot" per fare i grafici


# DATI INPUT
# LETTURA DEL FILE

#file locale nella stessa cartella dello script 
exofile = 'ExoplanetsPars_2025.csv'

# read_csv crea il DataFrame. comment='#' dice di IGNORARE le righe che
# iniziano con '#': il catalogo NASA ha un'intestazione di commenti che
# altrimenti verrebbe scambiata per dati.
exodf = pd.read_csv(exofile, comment='#')

# Stampa i nomi delle colonne (serve per sapere come si chiamano:
# pl_orbper, pl_bmassj, pl_orbsmax, st_mass, discoverymethod, ...)
print('Columns:', exodf.columns)
#print(lcdf)   # (riga commentata, e la variabile lcdf non esiste: residuo di un altro script)


# PARAMETRI PIANETI SISTEMA SOLARE 

# Array numpy scritti a mano, uno per grandezza, nell'ordine
# Mercurio, Venere, Terra, Marte, Giove, Saturno, Urano, Nettuno.

# Periodo orbitale in giorni
ss_orbper  = np.array([88, 225, 365, 687, 4333, 10759, 30687, 60190])
# Semiasse maggiore in AU
ss_orbsmax = np.array([0.47, 0.73, 1.02, 1.67, 5.45, 10.07, 20.09, 30.32])

# Massa in masse terrestri (la Terra vale 1)
ss_bmasse = np.array([0.06, 0.82, 1.0, 0.11, 317.89, 95.17, 14.56, 17.24])
# Conversione in masse di Giove: nel catalogo la colonna è pl_bmassj,
# quindi bisogna usare la stessa unità. 1 massa di Giove = 317.89 masse terrestri.
# La divisione è fatta elemento per elemento (broadcasting di numpy).
ss_bmassj = ss_bmasse / 317.89


################################### SCATTER PLOT #############################

# GRAFICO 1: massa del pianeta in funzione del periodo orbitale
# Crea la figura (12x6 pollici). fig = la "tela", ax = gli assi.
fig, ax = plt.subplots(figsize=(12, 6))

# Nuvola di esopianeti: x = periodo, y = massa (in M_Giove).
# alpha=0.3 -> punti semitrasparenti, così si vedono le zone dense.
plt.scatter(exodf['pl_orbper'], exodf['pl_bmassj'], alpha=0.3, color='gold', label='Exoplanets')
# Pianeti del Sistema Solare (opachi, grigi) sovrapposti ai precedenti
plt.scatter(ss_orbper, ss_bmassj, color='slategray', label='Solar System')

# Etichette degli assi (r'...' = raw string, $...$ = formula LaTeX)
plt.xlabel('Period [days]', fontsize=16)
plt.ylabel(r'Planet Mass [$m_J$]', fontsize=16)

# Assi logaritmici: periodi e masse coprono molti ordini di grandezza
plt.xscale('log')
plt.yscale('log')

# Dimensione dei numeri sugli assi e legenda (usa i 'label' dati negli scatter)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=16)

# Salva il grafico su file (PDF vettoriale e PNG) PRIMA di show(),
# altrimenti dopo show() la figura può risultare vuota.
plt.savefig('Exoplanets_ScatterPlot.pdf')
plt.savefig('Exoplanets_ScatterPlot.png')
# Mostra la finestra del grafico
plt.show()


# ---------------------------------------------------------------------------
# GRAFICO 2: grandezza costruita con semiasse maggiore e massa della stella
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6))

# y = a^2 / M_stella, calcolata direttamente sulle colonne del DataFrame
# (pandas lavora elemento per elemento su tutta la colonna).
# Per il Sistema Solare la massa della stella è 1 M_sole, quindi basta a^2.
# NB: dalla terza legge di Keplero la relazione "giusta" sarebbe a^3/M ~ P^2;
# qui si usa a^2/M, quindi la dipendenza dal periodo non è una retta di
# pendenza 1 ma di pendenza diversa (in scala log-log resta comunque una legge di potenza).
plt.scatter(exodf['pl_orbper'], (exodf['pl_orbsmax']**2) / exodf['st_mass'],
            alpha=0.3, color='gold', label='Exoplanets')
plt.scatter(ss_orbper, ss_orbsmax**2, color='slategray', label='Solar System')

plt.xlabel('Period [days]', fontsize=16)
plt.ylabel(r'$R_{max}^2/m_{\star}$ [$m_{\odot}^2/days$]', fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.savefig('Exoplanets_ScatterPlot_StMass.pdf')
plt.savefig('Exoplanets_ScatterPlot_StMass.png')
plt.show()


# SCATTER PLOT CON SELEZIONE 

# ---------------------------------------------------------------------------
# GRAFICO 3: come il grafico 1, ma distinguendo il metodo di scoperta
# ---------------------------------------------------------------------------
# (il commento originale "Flusso vs. Tempo" è un residuo: qui è massa vs periodo)
fig, ax = plt.subplots(figsize=(12, 6))

# df.loc[condizione, 'colonna'] seleziona le righe che soddisfano la condizione
# e restituisce solo quella colonna.
#   exodf['discoverymethod']=='Transit'  -> serie di True/False (maschera booleana)
#   .loc[maschera, 'pl_orbper']          -> periodi dei soli pianeti scoperti per transito
# Il colore non è specificato: matplotlib usa il ciclo di colori di default.
plt.scatter(exodf.loc[exodf['discoverymethod'] == 'Transit', 'pl_orbper'],
            exodf.loc[exodf['discoverymethod'] == 'Transit', 'pl_bmassj'],
            alpha=0.3, label='Transit')
# Stessa cosa per i pianeti scoperti con velocità radiali
plt.scatter(exodf.loc[exodf['discoverymethod'] == 'Radial Velocity', 'pl_orbper'],
            exodf.loc[exodf['discoverymethod'] == 'Radial Velocity', 'pl_bmassj'],
            alpha=0.3, label='Radial Velocity')
# Sistema Solare
plt.scatter(ss_orbper, ss_bmassj, color='slategray', label='Solar System')

plt.xlabel('Period [days]', fontsize=16)
plt.ylabel(r'Planet Mass [$m_J$]', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=14)
plt.savefig('Exoplanets_ScatterPlot_Selezione.pdf')
plt.savefig('Exoplanets_ScatterPlot_Selezione.png')
plt.show()


#SCATTER PLOT CON ISTOGRAMMI  

# ---------------------------------------------------------------------------
# FIGURA COMPOSITA 2x2
#
#   [0,0] istogramma del periodo   |  [0,1] vuoto
#   [1,0] scatter massa vs periodo |  [1,1] istogramma della massa (orizzontale)
#
# Qui si lavora in log10 "a mano" (np.log10) invece di usare assi log:
# gli assi mostrano quindi direttamente il logaritmo delle grandezze.
# ---------------------------------------------------------------------------

# Crea la figura vuota
fig = plt.figure(figsize=(12, 11))

# Griglia 2x2 senza spazi tra i riquadri (hspace=0, wspace=0)
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
# gs.subplots crea i 4 assi:
#   sharex='col' -> i riquadri della stessa colonna condividono l'asse x
#   sharey='row' -> i riquadri della stessa riga condividono l'asse y
# Così lo scatter e gli istogrammi risultano perfettamente allineati.
# ax è un array 2x2: si accede con ax[riga, colonna].
ax = gs.subplots(sharex='col', sharey='row')

# --- Riquadro in basso a sinistra: scatter log(massa) vs log(periodo) ---
ax[1,0].scatter(np.log10(exodf.loc[exodf['discoverymethod'] == 'Transit', 'pl_orbper']),
                np.log10(exodf.loc[exodf['discoverymethod'] == 'Transit', 'pl_bmassj']),
                color='limegreen', alpha=0.3, label='Transit')
ax[1,0].scatter(np.log10(exodf.loc[exodf['discoverymethod'] == 'Radial Velocity', 'pl_orbper']),
                np.log10(exodf.loc[exodf['discoverymethod'] == 'Radial Velocity', 'pl_bmassj']),
                color='darkorange', alpha=0.3, label='Radial Velocity')
ax[1,0].scatter(np.log10(ss_orbper), np.log10(ss_bmassj), color='slategray', label='Solar System')

# Con più riquadri si usano i metodi dell'oggetto ax (set_xlabel, ...)
# al posto delle funzioni plt.xlabel, che agirebbero solo sull'ultimo asse.
ax[1,0].tick_params(axis='both', which='major', labelsize=14)
ax[1,0].set_xlabel('log(Period [days])', fontsize=16)
ax[1,0].set_ylabel(r'log(Planet Mass [$m_J$])', fontsize=16)
ax[1,0].legend(fontsize=16)


# --- Riquadro in alto a sinistra: istogramma di log(periodo) ---
# bins=50 e range=(-2, 5): stesso numero di bin e stesso intervallo per
# i due metodi, così le barre hanno la stessa larghezza e sono confrontabili.
# alpha=0.5 permette di vedere la sovrapposizione.
ax[0,0].hist(np.log10(exodf.loc[exodf['discoverymethod'] == 'Transit', 'pl_orbper']),
             bins=50, range=(-2, 5), color='limegreen', alpha=0.5, label='Transit')
ax[0,0].hist(np.log10(exodf.loc[exodf['discoverymethod'] == 'Radial Velocity', 'pl_orbper']),
             bins=50, range=(-2, 5), color='darkorange', alpha=0.5, label='Radial Velocity')
ax[0,0].tick_params(axis='both', which='major', labelsize=14)
ax[0,0].set_ylabel(r'Number of planets', fontsize=16)
ax[0,0].legend(fontsize=16)


# --- Riquadro in basso a destra: istogramma di log(massa), disposto in verticale ---
# orientation='horizontal' ruota l'istogramma: le barre si sviluppano lungo x
# e i bin sono lungo y, così l'asse y coincide con quello dello scatter
# (condiviso per riga) e le masse si leggono allineate.
ax[1,1].hist(np.log10(exodf.loc[exodf['discoverymethod'] == 'Transit', 'pl_bmassj']),
             bins=50, range=(-4, 4), color='limegreen', alpha=0.5,
             orientation='horizontal', label='Transit')
ax[1,1].hist(np.log10(exodf.loc[exodf['discoverymethod'] == 'Radial Velocity', 'pl_bmassj']),
             bins=50, range=(-4, 4), color='darkorange', alpha=0.5,
             orientation='horizontal', label='Radial Velocity')

ax[1,1].tick_params(axis='both', which='major', labelsize=14)
ax[1,1].set_xlabel('Number of planets', fontsize=16)
ax[1,1].legend(fontsize=16)

# --- Riquadro in alto a destra: non serve, quindi si nascondono gli assi ---
ax[0,1].axis('off')

# Salvataggio e visualizzazione della figura composita
plt.savefig('Exoplanets_Period_vs_Mass_Detection.pdf')
plt.savefig('Exoplanets_Period_vs_Mass_Detection.png')
plt.show()