# BMI Berechnung
# Eingabe von Gewicht und Grösse
gewicht = input("Gib dein Gewicht in kg ein: ")
groesse = input("Gib deine Grösse in m ein: ")  # z.B. 1.75 für 1m75

# Umwandlung der Eingaben in Zahlen
gewicht = float(gewicht)
groesse = float(groesse)

# Berechnung des BMI
bmi = gewicht / (groesse ** 2)

# Ausgabe des BMI
print(f"Dein BMI ist {bmi:.2f}.")  # Ausgabe mit 2 Nachkommastellen
