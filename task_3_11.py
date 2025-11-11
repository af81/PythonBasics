numbers = []

for i in range(5):
    numbers.append(i + 1) # Fügt Zahlen von 1 bis 5 zur Liste

numbers[2] = 99 # Ersetzt das dritte Element mit 99

del(numbers[0]) # Löscht das erste Element der Liste

print(numbers)
