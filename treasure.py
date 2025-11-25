# Variablen
app_running = True;
items = []

# Funktionen
def show_items():
    if len(items) == 0:
                print("Die Liste ist leer.")
    else:
        for item in items:
            print(item)

# Begrüssung
print("*** Die Schatzkiste des Abenteurers 👑 ***")

while app_running:
    # Hauptmenü
    print("Menü: ")
    print("[1] Liste anzeigen.")
    print("[2] Item hinzufügen.")
    print("[3] Item löschen.")
    print("[4] Item suchen.")
    print("[5] Programm beenden.")
    auswahl = input("Was möchtest du tun? [1-5]: ")

    # Actions
    match auswahl:
        case "1":
            show_items()
        case "2":
            new_item = input("Gib ein neues Item ein: ")
            items.append(new_item)
            show_items()
        case "3":
            print("Liste anzeigen")
        case "4":
            print("Liste anzeigen")
        case "5":
            app_running = False
            print("Programm beendet.")
        case _:
            print("Ungültige Auswahl. Bitte gib eine Ziffer von 1 bis 5 ein...")
