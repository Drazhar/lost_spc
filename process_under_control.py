def check_process_control(m, data, UCL, CL, LCL, UCL_x, C_x, LCL_x):
    # Berechne Spannweiten und Mittelwerte der Stichproben
    
    # Initialisiere Listen, um die Stichproben zu speichern, die außerhalb der Kontrollgrenzen liegen
    r_out_of_control = []
    x_out_of_control = []
    
    # Überprüfen, ob jede Stichprobe innerhalb der Grenzen liegt
    for i in range(len(spannweite)):
        # Für die R-Karte
        if spannweite[i] > UCL or spannweite[i] < LCL:
            r_out_of_control.append(i)  # Speichern der Stichprobe (Zeilennummer)

        # Für die x-Karte
        if mittelwerte[i] > UCL_x or mittelwerte[i] < LCL_x:
            x_out_of_control.append(i)  # Speichern der Stichprobe (Zeilennummer)
    
    # Ergebnis ausgeben
    if r_out_of_control:
        print(f"Die folgenden Stichproben sind auf der R-Karte ausser Kontrolle: {r_out_of_control}")
    else:
        print("Alle Stichproben sind auf der R-Karte unter Kontrolle.")

    if x_out_of_control:
        print(f"Die folgenden Stichproben sind auf der x-Karte ausser Kontrolle: {x_out_of_control}")
    else:
        print("Alle Stichproben sind auf der x-Karte unter Kontrolle.")