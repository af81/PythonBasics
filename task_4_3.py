def roman_to_decimal(roman_letter):
    match roman_letter:
        case "I":
            print(f"Die römische Ziffer {roman_letter} entspricht der Zahl 1")
        case "V":
            print(f"Die römische Ziffer {roman_letter} entspricht der Zahl 5")
        case "X":
            print(f"Die römische Ziffer {roman_letter} entspricht der Zahl 10")
        case "L":
            print(f"Die römische Ziffer {roman_letter} entspricht der Zahl 50")
        case "C":
            print(f"Die römische Ziffer {roman_letter} entspricht der Zahl 100")
        case "D":
            print(f"Die römische Ziffer {roman_letter} entspricht der Zahl 500")
        case "M":
            print(f"Die römische Ziffer {roman_letter} entspricht der Zahl 1000")

ziffer = input("Gib eine römische Ziffer ein. z.B. I, V, X, L, C, D oder M: ")

roman_to_decimal(ziffer)
