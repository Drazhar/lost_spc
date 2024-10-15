import numpy as np

"""
Da bei einigen Klasse Redundanzen auftretten wurde diese Datei erstellt um sie zu minimieren.
Das Singelton-Muster:
- Es hat nur eine einzelne Instanz (In diesem Fall wahr aber nicht umbedingt notwendig).
- Es möglich global auf die Instanz zuzugreifen. 
- Es erstellt erst eine Instanz wenn sie das erste mal benötigt wird.
"""


class StorageSingleton: # neu Klasse bei Singleton existiert nur eine Instanz
    _instance = None # Variable zur speichern der Instanz wird am Anfang None gesetzt (_instance is privat!)

    def __new__(cls): # cls ist die Klasse selbst in dieser wird Untersucht.
        if cls._instance is None: # Wenn es nicht schon 
            cls._instance = super(StorageSingleton, cls).__new__(cls) # Es wird eine Instanz erstell und zurück gegeben
            cls._instance.storage = []  # Initialisiert die Instanz 
        return cls._instance

    def get_store(self, X):
        for i, p in enumerate(self.storage):  # Durchläuft die Unterlisten von storage
            if self.storage[i][0].shape == X.shape:  # Vergleich zuerst die shape um Valueerror zu vermeiden
                if np.array_equal(self.storage[i][0],X): # Vergleich nur wenn Form übereinstimmt
                    # Erstelle ein Dictionary zum Speichern der Werte
                    values = {
                    'R_bar': self.storage[i][1] if len(self.storage[i]) > 1 else None,
                    'X_bar': self.storage[i][2] if len(self.storage[i]) > 2 else None,
                    'X_bar_bar': self.storage[i][3] if len(self.storage[i]) > 3 else None,
                    'A': self.storage[i][4] if len(self.storage[i]) > 4 else None,
                    'm': self.storage[i][5] if len(self.storage[i]) > 5 else None,
                    'n': self.storage[i][6] if len(self.storage[i]) > 6 else None,
                    'd2': self.storage[i][7] if len(self.storage[i]) > 7 else None,
                    'd3': self.storage[i][8] if len(self.storage[i]) > 8 else None,
                    'R': self.storage[i][9] if len(self.storage[i]) > 9 else None
                }
                    #var_name = VariableNameInspector.get_variable_name(X)    
                    print(f"storage wurde erfolgreich aufgerufen!")
                    # Gibt ein Dictionary zurück, in dem nur die nicht-None-Werte enthalten sind
                    return {key: value for key, value in values.items() if value is not None}


    def save_store(self, X=None, R_bar=None, X_bar=None, X_bar_bar=None, A=None, m=None, n=None, d2=None, d3=None,R=None):
        for i,p in enumerate(self.storage): # geht die 1-10 Unterlisten von storage durch
            if self.storage[i][0].shape == X.shape:  # Vergleich zuerst die shape um ValueError zu vermeiden
                if np.array_equal(self.storage[i][0],X):
                    return # Beendet die Funktion nachdem ein Duplikat gefunden wurde.
        if len(self.storage) >= 10:  # Wenn die Liste der gespeicherten Einheiten länger als 10 ist, entferne die älteste
            self.storage.pop(0)
        #var_name = VariableNameInspector.get_variable_name(X)
        print(f"storage wurde erfolgreich gespeichert!")
        pack = [X, R_bar, X_bar, X_bar_bar, A, m, n, d2, d3, R]
        self.storage.append(pack)  # Append the packed parameters to the storage list


# alt 12.10.2024
"""
def get_store(X):
    if storage  is None:
        storage = [X=None,R_bar=None,X_bar=None,X_bar_bar=None,A=None,m=None,n=None,d2=None,d3=None]
    for i,p in enumerate(storage) :
        print(storage[i][0])

def save_store(X=None,R_bar=None,X_bar=None,X_bar_bar=None,A=None,m=None,n=None,d2=None,d3=None):
    if storage is None: # Wenn storage noch nicht existiert wird es erstellt
        storage = []
    elif len(storage) >= 10: # Wenn die Liste der gespeicherten Einheiten länger als 10 ist, entferne die älteste
        storage.pop(0)
    else:
        pack = [X,X_bar_bar,A,m,n,d2,d3] # Wird benötigt um zu überprüfen welche Parameter definiert sind 
        storage.append(pack)
"""              