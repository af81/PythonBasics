# Zeitumrechnung in das metrische System
# Eingabe von Stunden, Minuten und Sekunden
stunden = input("Gib die Stunden ein: ")
minuten = input("Gib die Minuten ein: ")
sekunden = input("Gib die Sekunden ein: ")  # z.B. 30 für 30 Minuten

# Umwandlung der Eingaben in Zahlen
stunden = float(stunden)
minuten = float(minuten)
sekunden = float(sekunden)

# Umrechnung in das metrische System (Zehnersystem)
metrische_stunden = stunden + (minuten / 60) + (sekunden / 3600)

# Ausgabe der umgerechneten Zeit
print(f"Die umgerechnete Zeit im metrischen System ist {metrische_stunden:.2f} Stunden.")  # Ausgabe mit 2 Nachkommastellen
