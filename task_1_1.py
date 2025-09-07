# Einfache Ein- und Ausgabe

# Eingabe des Namens
print("Wie heisst du?")
name = input("Gib deinen Namen ein: ")

# Ausgabe einer Begrüssung
print(f"Hallo {name}! Schön, dass du da bist")  # Alternativ: print("Hallo " + name + "! Schön, dass du da bist")

# Eingabe zweier Zahlen
print("Lass uns zwei Zahlen addieren.")
zahl1 = input("Gib die erste Zahl ein: ")
zahl2 = input("Gib die zweite Zahl ein: ")

# Umwanldung der Eingaben in Zahlen und Berechnung der Summe
summe = float(zahl1) + float(zahl2)  # Umwandlung

# Ausgabe der Summe
print(f"Die Summe von {zahl1} und {zahl2} ist {summe}.")
