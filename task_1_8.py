# Logische Operatoren

number = int(input("Please enter a number between -200 and +200: "))

# Check 1
check1 = (number >= 10 and number <= 20)                    # 10 =< number <= 20 auch möglich
print(f"Your number is between 10 and 20: {check1}")

# Check 2
check2 = (number < 0 or number > 100)
print(f"Your number is smaller than 0 or bigger than 100: {check2}")

# Bei and müssen beide Seiten der Aussage true sein, damit die ganze Aussage true ist
# Bei or muss mindestens eine Seite der Aussage true sein, damit die ganze Aussage true ist
