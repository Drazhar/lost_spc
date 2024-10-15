import numpy as np
import sys
import os
from scipy.special import gamma
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lost_spc')))
from constants import d
from table import table
import error as error 
from storage import StorageSingleton



def limits_R(X):
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

    if R is None:
        R = X.max(axis=1)-X.min(axis=1) # Array der Spannweite
    if R_bar is None:
        R_bar = R.mean() # Mittelwert der Spannweite
    if A is None:
        A= np.shape(X) # Dimensionen der Daten
    if m is None:
        m  = A[1] # Anzahl der Spalten
    if d2 is None: # Wenn d2 existiert muss d3 auch existieren
        d2, d3 = d(m, 100000)

    L3 = (1-3*d3/d2)*R_bar # Tiefere Kontrollgrenze 3
    L2 = (1-2*d3/d2)*R_bar # Tiefere Kontrollgrenze 2
    L1 = (1-d3/d2)*R_bar # Tiefere Kontrollgrenze 1
    C = R_bar # Mittelwert
    U1 = (1+d3/d2)*R_bar # Obere Kontrollgrenze 1
    U2 = (1+2*d3/d2)*R_bar # Obere Kontrollgrenze 2
    U3 = (1+3*d3/d2)*R_bar # Obere Kontrollgrenze 3
    
    table(L3,L2,L1,C,U1,U2,U3)

    storage_manager.save_store(X=X, R_bar=R_bar, A=A, R=R, d2=d2, d3=d3, m=m)

      
def limits_x(X):
    error.error_Type1(X)
    error.error_Shape1(X,2,2)
    
    # storage
    storage_manager = StorageSingleton()
    values = storage_manager.get_store(X)

    R_bar = values.get('R_bar') if values else None
    X_bar = values.get('X_bar') if values else None
    X_bar_bar = values.get('X_bar_bar') if values else None
    A = values.get('A') if values else None
    m = values.get('m') if values else None
    d2 = values.get('d2') if values else None
    d3 = values.get('d3') if values else None
    R = values.get('R') if values else None

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

    table(L3,L2,L1,C,U1,U2,U3)

    storage_manager.save_store(X=X, R_bar=R_bar, A=A, R=R, d2=d2, d3=d3, m=m,X_bar=X_bar,X_bar_bar=X_bar_bar)
   

def limits_s(X):
    error.error_Type1(X)
    error.error_Shape1(X,2,2)

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

    table(L3,L2,L1,C,U1,U2,U3)
   