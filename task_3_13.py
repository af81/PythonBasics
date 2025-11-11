treasures = []
game_on = True

# Funktion für Suche nach Gegenstand
def search_item(search_term):
    if search_term in treasures:
        print("Der Gegenstand ist in der Liste vorhanden.")
    else:
        print("Der Gegenstand befindet sich nicht in der Liste.")

# Funktion für das Entfernen eines Gegenstands
def delete_item(item):
    treasures.remove(item)
    print(f"{item} wurde erfolgreich aus der Liste entfernt.")

# Programmstart und Menü
print("*** Die Schatzkiste des Abenteurers ***\n")
print("Gib fünf Gegenstände ein, die du in der Höhle gefunden hast:")

for i in range(5):
    treasures.append(input(f"Item {i+1}: "))

print(treasures)

while(game_on):
    print("\nWas möchtest du nun tun?\n")
    print("[1] Neuen Gegenstand erfassen")
    print("[2] Nach Gegenstand suchen")
    print("[3] Gegenstand aus Liste löschen")
    print("[4] Liste anzeigen")
    print("[5] Programm beenden")

    action = input("Gib deine gewünschte Aktion ein: ")

    match action:
        case "1":
            new_item = input("Welchen Gegenstand möchtest du der Liste hinzufügen?: ")
            treasures.append(new_item)
            input("Drücke ENTER für weiter..")
        case "2":
            search_term = input("Gib den Namen eines Items ein, um zu sehen, ob es in der Liste enthalten ist: ")
            search_item(search_term)
            input("Drücke ENTER für weiter..")
        case "3":
            item = input("Möchtest du ein bestimmtes Item aus der List entfernen? [Namen eingeben]")
            delete_item(item)
            input("Drücke ENTER für weiter..")
        case "4":
            print(treasures)
            input("Drücke ENTER für weiter..")
        case "5":
            game_on = False
            print("Programm beendet.")
            break;
        case _:
            print("Keine gültige Eingabe.")
