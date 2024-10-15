import numpy as np
import scipy.stats as st
from scipy.special import gamma
import matplotlib.pyplot as plt
import sys
import os
# __file__ enthalt den Pfad der aktuellen Datei
# os.path.join() sorgt für den richtigen Umgang mit den (/) Zeichen.
# os.path.abspath gibt den Pfad Pfad zum Verzeichniss zurück in diesem Fall "src"
# sys.path.append() ist eine Liste von Verzeichnissen die Python durchsucht wenn import verwendet wird. 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lost_spc')))

from constants import d,c4
import error 
from storage import StorageSingleton

def shewart_R(X,X_new=None):
    error.error_Type1(X)
    error.error_Shape1(X,2,2)

    # storage
    storage_manager = StorageSingleton()
    values = storage_manager.get_store(X)

    # Zugriff auf spezifische Werte durch das Dictionary
    # Versucht, Werte aus dem 'values'-Dictionary abzurufen.
    # Falls 'values' leer oder None ist, wird der entsprechende Wert auf None gesetzt.
    R_bar = values.get('R_bar') if values else None
    A = values.get('A') if values else None
    m = values.get('m') if values else None
    d2 = values.get('d2') if values else None
    d3 = values.get('d3') if values else None
    R = values.get('R') if values else None

    R = X.max(axis=1)-X.min(axis=1) # Array der Spannweite
    R_bar = R.mean() # Mittelwert der Spannweite
    
    A= np.shape(X) # Dimensionen der Daten
    m  = A[1] # Anzahl der Spalten
    n = A[0] # Anzahl der Zeilen
    d2, d3 = d(m,sim_size=100000)

    L = (1-3*d3/d2)*R_bar # Tiefere Kontrollgrenze
    print(f"LCL = {L}")
    C = R_bar # Mittelwert
    print(f"C = {C}")
    U = (1+3*d3/d2)*R_bar # Obere Kontrollgrenze
    print(f"UCL = {U}")

    # Eingriffsgrenzen
    plt.hlines([U, C, L], 0, n+n+1, linestyles="dashed", colors="gray") # Macht Linien bei den Kontrollgrenzen und Mittelwert
    plt.hlines([(1+d3/d2)*R_bar, (1+2*d3/d2)*R_bar,(1-d3/d2)*R_bar ,(1-2*d3/d2)*R_bar],0, n+n+1, linestyles="dotted", colors="lightgray") # Macht Linien bei 1 und 2 Sigma
 
    
    x = np.linspace(1,n,n)
    plt.plot(x, R, "o-")

    if X_new is not None: # Wenn für X_new ein Array angegeben wird er geplottet
        # Neue Daten
        A_new = np.shape(X_new) # Dimension der neuen Datne
        n_new = A_new[0]  # Anzahl Zeilen der neuen Daten
        R_new =  X_new.max(axis=1)- X_new.min(axis=1) # Array der Spannweiten
        x_new = np.linspace(1,n_new,n_new)  # Neuer Intervall der Messwerte

        plt.vlines(n+0.5, L, U, colors="red") 
        plt.plot(x_new+n,R_new,"*-") # Plot der neuen Daten
    else: 
        plt.xlim((0,n+1))

    plt.title("$R$-Karte")
    plt.xlabel('Sample')
    plt.ylabel('$R$')
    plt.show()

def shewart_x(X,X_new=None):
    error.error_Type1(X)
    error.error_Shape1(X,2,2)
    
    X_bar = X.mean(axis=1) # Mittlwert jeder Zeile
    X_bar_bar  = X_bar.mean() # Mittelwert der Mittelwerte
    R = X.max(axis = 1) - X.min(axis = 1) # Spannweite
    R_bar = R.mean() # Mittelwert der Spannweite

    A= np.shape(X) # Dimensionen der Daten
    m  = A[1] # Anzahl der Spalten
    n = A[0] # Anzahl der Zeilen
    d2, d3 = d(m, 100000)

    L = (X_bar_bar-3/(d2*np.sqrt(m))*R_bar) # Tiefere Kontrollgrenze
    print(f"LCL = {L}")
    C = X_bar_bar # Mittelwert
    print(f"C = {C}")
    U = (X_bar_bar+3/(d2*np.sqrt(m))*R_bar) # Obere Kontrollgrenze
    print(f"UCL = {U}")

    # Eingriffsgrenzen
    plt.hlines([U, C, L], 0, n+n+1, linestyles="dashed", colors="gray") # Macht Linien bei den Kontrollgrenzen und Mittelwert
    plt.hlines([(X_bar_bar+1/(d2*np.sqrt(m))*R_bar), (X_bar_bar+2/(d2*np.sqrt(m))*R_bar),(X_bar_bar-1/(d2*np.sqrt(m))*R_bar) ,(X_bar_bar-2/(d2*np.sqrt(m))*R_bar)],0, n+n+1, linestyles="dotted", colors="lightgray") # Macht Linien bei 1 und 2 Sigma
    
    x = np.linspace(1,n,n)
    plt.plot(x, X_bar, "o-") 

    if X_new is not None: # Wenn für X_new ein Array angegeben wird er geplottet

        plt.vlines(n+0.5, L, U, colors="red") 

        # Neue Daten
        A_new = np.shape(X_new) # Dimension der neuen Datne
        n_new = A_new[0]  # Anzahl Zeilen der neuen Daten
        X_bar_new = X_new.mean(axis=1)
        x_new = np.linspace(1,n_new,n_new) 
        plt.plot(x_new+n,X_bar_new,"*-")
    else: 
        plt.xlim((0,n+1))

    plt.title("$x$-Karte")
    plt.xlabel('Sample')
    plt.ylabel('$x_{i_{mean}}$')
    plt.show()

def shewart_s(X,X_new=None):
    error.error_Type1(X)
    error.error_Shape1(X,2,2)
    
    s = X.std(axis=1,ddof=1) # Standartabweichung der einzelnen Spalten  
    s_bar = s.mean() # Mittelwert der Standartabweichung
    R = X.max(axis = 1) - X.min(axis = 1) # Spannweite
    R_bar = R.mean() # Mittelwert der Spannweite

    A= np.shape(X) # Dimensionen der Daten
    m  = A[1] # Anzahl der Spalten
    n = A[0] # Anzahl der Zeilen
    d2, d3 = d(m, 100000)

    C4 =  gamma(m / 2) / gamma((m - 1) / 2) * np.sqrt(2 / (m - 1)) # Konstante

    L = s_bar-3*np.sqrt(1-C4**2)/C4*s_bar # Tiefere Kontrollgrenze
    print(f"LCL = {L}")
    C = s_bar # Mittelwert
    print(f"C = {C}")
    U = s_bar+3*np.sqrt(1-C4**2)/C4*s_bar # Obere Kontrollgrenze
    print(f"UCL = {U}")

    plt.hlines([U, C, L], 0, n+n+1, linestyles="dashed", colors="gray") # Macht Linien bei den Kontrollgrenzen und Mittelwert
    plt.hlines([s_bar+np.sqrt(1-C4**2)/C4*s_bar, s_bar+2*np.sqrt(1-C4**2)/C4*s_bar,s_bar-np.sqrt(1-C4**2)/C4*s_bar,s_bar-2*np.sqrt(1-C4**2)/C4*s_bar],0, n+n+1, linestyles="dotted", colors="lightgray") # Macht Linien bei 1 und 2 Sigma
    
   
 
    x = np.linspace(1,n,n)
    plt.plot(x, s, "o-") 

    if X_new is not None: # Wenn für X_new ein Array angegeben wird er geplottet
        plt.vlines(n+0.5, L, U, colors="red") # Rote vertikale Linie nach n+0.5 in x-Richtung
        # Neue Daten
        A_new = np.shape(X_new) # Dimension der neuen Daten
        n_new = A_new[0]  # Anzahl Zeilen der neuen Daten
        s_new = X_new.std(axis=1,ddof=1)
        x_new = np.linspace(1,n_new,n_new) 
        plt.plot(x_new+n,s_new,"*-")
    else: 
        plt.xlim((0,n+1))

    plt.title("$s$-Karte")
    plt.xlabel('Sample')
    plt.ylabel('$s$')
    plt.show()

def shewart_ind(X,m=2): # m wird Standartmässig als 2 angesehen
    error.error_Type1(X)
    error.error_Shape1(X,1,m)
    
    MR = rolling(X,m)
    MR_i = np.abs(MR)
    MR_bar = MR_i.mean()
    
    # R-Teil:
    R = np.max(X)-np.min(X) # Array der Spannweite
    R_bar = R.mean() # Mittelwert der Spannweite

    # x-Teil:
    X_bar = np.mean(X) # Mittlwert jeder Zeile
    X_bar_bar  = X_bar.mean() # Mittelwert der Mittelwerte


    A= np.shape(X) # Dimensionen der Daten
    n = A[0]

    d2, d3 = d(m, 10000000)

    RL = (1-3*d3/d2)*MR_bar # Tiefere Kontrollgrenze
    print(f"RLCL = {RL}")
    RC = MR_bar # Mittelwert
    print(f"RC = {RC}")
    RU = (1+3*d3/d2)* MR_bar # Obere Kontrollgrenze
    print(f"RUCL = {RU}")   

    # Eingriffsgrenzen
    # R-Karte
    plt.figure()
    plt.hlines([RU, RC, RL], 0, n+n+1, linestyles="dashed", colors="gray") # Macht Linien bei den Kontrollgrenzen und Mittelwert
    plt.hlines([(1+d3/d2)*MR_bar, (1+2*d3/d2)*MR_bar,(1-d3/d2)*MR_bar ,(1-2*d3/d2)*MR_bar],0, n+n+1, linestyles="dotted", colors="lightgray") # Macht Linien bei 1 und 2 Sigma 
    
    x = np.linspace(1,n-m+1,n-m+1)
    plt.plot(x, MR_i, "o-")
    
    plt.title("$R$-Karte")
    plt.xlabel('Sample')
    plt.ylabel('$R$')
    plt.grid()
    plt.xlim([0,n-m+2]) # Setzt das Limit der x-Achse
    plt.show()
 
    # x-Karte
    XL = (X_bar_bar-3/(d2*np.sqrt(1))*MR_bar) # Tiefere Kontrollgrenze
    print(f"XLCL = {XL}")
    XC = X_bar_bar # Mittelwert
    print(f"XC = {XC}")
    XU = (X_bar_bar+3/(d2*np.sqrt(1))*MR_bar) # Obere Kontrollgrenze
    print(f"XUCL = {XU}")

    # Eingriffsgrenzen
    plt.hlines([XU, XC, XL], 0, n+n+1, linestyles="dashed", colors="gray") # Macht Linien bei den Kontrollgrenzen und Mittelwert
    plt.hlines([(X_bar_bar+1/(d2*np.sqrt(1))*MR_bar), (X_bar_bar+2/(d2*np.sqrt(1))*MR_bar),(X_bar_bar-1/(d2*np.sqrt(1))*MR_bar) ,(X_bar_bar-2/(d2*np.sqrt(1))*MR_bar)],0, n+n+1, linestyles="dotted", colors="lightgray") # Macht Linien bei 1 und 2 Sigma
 
    x = np.linspace(1,n,n)
    plt.plot(x, X, "o-") 

    plt.title("$x$-Karte")
    plt.xlabel('Sample')
    plt.ylabel('$x_{i_{mean}}$')
    plt.xlim([0,n+1])
    plt.grid()
    plt.show()

def rolling(B,m): # Macht einen rolling average über eine Gruppe der grösse m im Array B
    error.error_Type1(B)
    A = np.shape(B)
    rolling_diff = []
    for i in range(A[0]-m+1):
        rolling_diff.append(np.max(B[i:i+m])-np.min(B[i:i+m]))
    return rolling_diff