# Grundrechenarten

zahl1 = input("Gib eine erste Zahl ein: ")
zahl2 = input("Gib eine zweite Zahl ein: ")

summe = float(zahl1) + float(zahl2)
differenz = float(zahl1) - float(zahl2)
produkt = float(zahl1) - float(zahl2)
quotient = float(zahl1) / float(zahl2)

print("Die Addition dieser beiden Zahlen ergibt: ", round(summe, 2))
print("Die Subtraktion dieser beiden Zahlen ergibt: ", round(differenz, 2))
print("Die Multiplikation dieser beiden Zahlen ergibt: ", round(produkt, 2))
print("Die Division dieser beiden Zahlen ergibt: ", round(quotient, 2))


# Unterschied / und //

# In Python gibt es einen klaren Unterschied:
# / ist der Gleitkomma-Divisionsoperator, der immer ein Gleitkommaergebnis liefert (z.B. 10 / 3 ergibt 3.333...)
# // ist der Ganzzahl-Divisionsoperator (Floor Division), der das Ergebnis auf eine ganze Zahl abrundet, indem der Nachkommateil abgeschnitten wird (z.B. 10 // 3 ergibt 3).
