def begruessung(name):
    if name == "Max":
        print("Hallo Max! Schön, dass du da bist.")
    else:
        print(f"Hallo {name}! Willkommen im Programm.")


name = input("Wie heisst du?: ")

begruessung(name)
