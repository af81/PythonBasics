# Abfrage Benutzer
print("Welche Strecke möchtest du zurücklegen?")
distance = float(input("Gib die Distanz in Kilometern ein: "))

print("Wie schnell fährt dein Auto durchschnittlich?")
velocity = float(input("Gib die Geschwindigkeit in km/h ein: "))

print("Wie hoch ist der durchschnittliche Verbrauch deines Autos?")
consumption = float(input("Gib den Verbrauch in Litern pro 100 km ein: "))

# Berechnung der Zeit
time = distance / velocity * 60  # Zeit in Minuten
time_rounded = round(time, 2)

# Berechnung des Verbrauchs
fuel_used = (consumption / 100) * distance  # Verbrauch in Litern
fuel_used_rounded = round(fuel_used, 2)

# Ausgabe der Ergebnisse
print(f"Die Fahrt dauert {time_rounded} Minuten.")
print(f"Du verbrauchst {fuel_used_rounded} Liter Benzin.")
