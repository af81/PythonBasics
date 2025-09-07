# Potenzieren, Divison & Modulo

preis_riegel = 3.20
guthaben = 20

anzahl_riegel = int(guthaben // preis_riegel)
restgeld = guthaben % preis_riegel
restgeld_5_rappen = round(restgeld / 5, 2) * 5      # Rundet Restgeld auf 5-Rappen-Beträge

print(f"Mit {guthaben} Fr. kannst du {anzahl_riegel} Riegel zum Preis von {preis_riegel} Fr. kaufen.")
print(f"Das Restgeld beträgt {restgeld_5_rappen} Fr.")
