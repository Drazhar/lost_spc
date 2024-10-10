import numpy as np
import scipy.stats as st
from scipy.special import gamma
import matplotlib.pyplot as plt

def shewart_R(X,X_new):
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
 
    plt.vlines(n+0.5, L, U, colors="red") 
 
    x = np.linspace(1,n,n)
    plt.plot(x, R, "o-")
    
    # Neue Daten
    A_new = np.shape(X_new) # Dimension der neuen Datne
    n_new = A_new[0]  # Anzahl Zeilen der neuen Daten
    R_new =  X_new.max(axis=1)- X_new.min(axis=1) # Array der Spannweiten
    x_new = np.linspace(1,n_new,n_new)  # Neuer Intervall der Messwerte

    plt.plot(x_new+n,R_new,"*-") # Plot der neuen Daten
    plt.title("$R$-Karte")
    plt.xlabel('Sample')
    plt.ylabel('$R$')
    plt.xlim([0,n+n_new+1]) # Setzt das Limit der x-Achse
    plt.show()

def shewart_x(X,X_new):
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
 
    plt.vlines(n+0.5, L, U, colors="red") 
 
    x = np.linspace(1,n,n)
    plt.plot(x, X_bar, "o-") 

    # Neue Daten
    A_new = np.shape(X_new) # Dimension der neuen Datne
    n_new = A_new[0]  # Anzahl Zeilen der neuen Daten
    X_bar_new = X_new.mean(axis=1)
    x_new = np.linspace(1,n_new,n_new) 
    plt.plot(x_new+n,X_bar_new,"*-")

    plt.title("$x$-Karte")
    plt.xlabel('Sample')
    plt.ylabel('$x_{i_{mean}}$')
    plt.xlim([0,n+n_new+1])
    plt.show()

def shewart_s(X,X_new):
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
 
    plt.vlines(n+0.5, L, U, colors="red") # Rote vertikale Linie nach n+0.5 in x-Richtung
 
    x = np.linspace(1,n,n)
    plt.plot(x, s, "o-") 

    # Neue Daten
    A_new = np.shape(X_new) # Dimension der neuen Datne
    n_new = A_new[0]  # Anzahl Zeilen der neuen Daten
    s_new = X_new.std(axis=1,ddof=1)
    x_new = np.linspace(1,n_new,n_new) 
    plt.plot(x_new+n,s_new,"*-")

    plt.title("$s$-Karte")
    plt.xlabel('Sample')
    plt.ylabel('$s$')
    plt.xlim([0,n+n+1])
    plt.show()

def shewart_ind(X,m):
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

def ranges(X):
    R = X.max(axis=1)-X.min(axis=1) # Array der Spannweite
    R_bar = R.mean() # Mittelwert der Spannweite
    print(f"Spannweiten: {R}, Mittelwert der Spannweiten: {R_bar}")

def mean(X):
    X_bar = X.mean(axis=1) # Mittlwert jeder Zeile
    X_bar_bar  = X_bar.mean() # Mittelwert der Mittelwerte
    print(f"Mittelwerte: {X_bar}, Mittelwert der Mittelwerte: {X_bar_bar}")

def std(X):
    s = X.std(axis=1,ddof=1) # Standartabweichung der einzelnen Spalten  
    s_bar = s.mean() # Mittelwert der Standartabweichung
    print(f"Standartabweichungen: {s}, Mittelwert der Standartabweichungen: {s_bar}")

def limits_R(X):
    R = X.max(axis=1)-X.min(axis=1) # Array der Spannweite
    R_bar = R.mean() # Mittelwert der Spannweite
    
    A= np.shape(X) # Dimensionen der Daten
    m  = A[1] # Anzahl der Spalten
    n = A[0] # Anzahl der Zeilen
    d2, d3 = d(m, 100000)

    L3 = (1-3*d3/d2)*R_bar # Tiefere Kontrollgrenze 3
    L2 = (1-2*d3/d2)*R_bar # Tiefere Kontrollgrenze 2
    L1 = (1-d3/d2)*R_bar # Tiefere Kontrollgrenze 1
    C = R_bar # Mittelwert
    U1 = (1+d3/d2)*R_bar # Obere Kontrollgrenze 1
    U2 = (1+2*d3/d2)*R_bar # Obere Kontrollgrenze 2
    U3 = (1+3*d3/d2)*R_bar # Obere Kontrollgrenze 3
    
    # Tabellarische Ausgabe mit f-Strings
    table = f"""
    +---------------------+---------+
    | Kontrollgrenze      | Wert    |
    +---------------------+---------+
    | L3                  | {L3:.2f} |
    | L2                  | {L2:.2f} |
    | L1                  | {L1:.2f} |
    | C                   | {C:.2f}  |
    | U1                  | {U1:.2f} |
    | U2                  | {U2:.2f} |
    | U3                  | {U3:.2f} |
    +---------------------+---------+
    """
    print(table)

def limits_x(X):
    X_bar = X.mean(axis=1) # Mittlwert jeder Zeile
    X_bar_bar  = X_bar.mean() # Mittelwert der Mittelwerte
    R = X.max(axis = 1) - X.min(axis = 1) # Spannweite
    R_bar = R.mean() # Mittelwert der Spannweite

    A= np.shape(X) # Dimensionen der Daten
    m  = A[1] # Anzahl der Spalten
    d2, d3 = d(m, 100000)

    L3 = (X_bar_bar-3/(d2*np.sqrt(m))*R_bar) # Tiefere Kontrollgrenze 3
    L2 = (X_bar_bar-2/(d2*np.sqrt(m))*R_bar) # Tiefere Kontrollgrenze 2
    L1 = (X_bar_bar-1/(d2*np.sqrt(m))*R_bar) # Tiefere Kontrollgrenze 1
    C = X_bar_bar # Mittelwert
    U1 = (X_bar_bar+1/(d2*np.sqrt(m))*R_bar) # Obere Kontrollgrenze 1
    U2 = (X_bar_bar+2/(d2*np.sqrt(m))*R_bar) # Obere Kontrollgrenze 2
    U3 = (X_bar_bar+3/(d2*np.sqrt(m))*R_bar) # Obere Kontrollgrenze 3

    
    # Tabellarische Ausgabe mit f-Strings
    table = f"""
    +---------------------+---------+
    | Kontrollgrenze      | Wert    |
    +---------------------+---------+
    | L3                  | {L3:.2f} |
    | L2                  | {L2:.2f} |
    | L1                  | {L1:.2f} |
    | C                   | {C:.2f}  |
    | U1                  | {U1:.2f} |
    | U2                  | {U2:.2f} |
    | U3                  | {U3:.2f} |
    +---------------------+---------+
    """
    print(table)

def limits_s(X):
    s = X.std(axis=1,ddof=1) # Standartabweichung der einzelnen Spalten  
    s_bar = s.mean() # Mittelwert der Standartabweichung

    A= np.shape(X) # Dimensionen der Daten
    m = A[1] # Anzahl der Spalten

    C4 =  gamma(m / 2) / gamma((m - 1) / 2) * np.sqrt(2 / (m - 1)) # Konstante

    L3 = s_bar-3*np.sqrt(1-C4**2)/C4*s_bar # Tiefere Kontrollgrenze 3
    L2 = s_bar-2*np.sqrt(1-C4**2)/C4*s_bar # Tiefere Kontrollgrenze 2
    L1 = s_bar-1*np.sqrt(1-C4**2)/C4*s_bar # Tiefere Kontrollgrenze 1
    C = s_bar # Mittelwert
    U1 = s_bar+1*np.sqrt(1-C4**2)/C4*s_bar # Obere Kontrollgrenze 1
    U2 = s_bar+2*np.sqrt(1-C4**2)/C4*s_bar # Obere Kontrollgrenze 2
    U3 = s_bar+3*np.sqrt(1-C4**2)/C4*s_bar # Obere Kontrollgrenze 3

    # Tabellarische Ausgabe mit f-Strings
    table = f"""
    +---------------------+---------+
    | Kontrollgrenze      | Wert    |
    +---------------------+---------+
    | L3                  | {L3:.2f} |
    | L2                  | {L2:.2f} |
    | L1                  | {L1:.2f} |
    | C                   | {C:.2f}  |
    | U1                  | {U1:.2f} |
    | U2                  | {U2:.2f} |
    | U3                  | {U3:.2f} |
    +---------------------+---------+
    """
    print(table)
    
def Schätzer_mu(X):
    X_bar = X.mean(axis=1) # Mittlwert jeder Zeile
    X_bar_bar  = X_bar.mean() # Mittelwert der Mittelwerte
    print(f"Der Erwartungwert mu0 ist {X_bar_bar}")

def Schätzer_sig(X):
    s = X.std(axis=1,ddof=1) # Standartabweichung der einzelnen Spalten  
    s_bar = s.mean() # Mittelwert der Standartabweichung

    A= np.shape(X) # Dimensionen der Daten
    m  = A[1] # Anzahl der Spalten

    C4 =  gamma(m / 2) / gamma((m - 1) / 2) * np.sqrt(2 / (m - 1)) # Konstante
    
    sigma = s_bar/C4 

    print(f"Der Schätzer Sigma_Dach ist {sigma} ")

def d(m, sim_size=100_000):
    X = st.norm.rvs(size=(sim_size, m))
    R_i = X.max(axis=1) - X.min(axis=1)
    d2 = np.mean(R_i)
    d3 = np.std(R_i, ddof=1)
    return d2, d3

def c4(m):
    return gamma(m / 2) / gamma((m - 1) / 2) * np.sqrt(2 / (m - 1))

def rolling(B,m):
    A = np.shape(B)
    rolling_diff = []
    for i in range(A[0]-m+1):
        rolling_diff.append(np.max(B[i:i+m])-np.min(B[i:i+m]))
    return rolling_diff