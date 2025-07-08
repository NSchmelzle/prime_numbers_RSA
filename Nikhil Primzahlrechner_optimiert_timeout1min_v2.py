import time

def primzahl_ueberpruefung(zahl, timeout):
    startzeit = time.time()
    bekannte_primzahlen = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    is_primzahl = True
    for primzahl in bekannte_primzahlen:
        if time.time() - startzeit > timeout:
            print("Berechnung abgebrochen (120s timeout)")
            return None
        if zahl % primzahl == 0 and zahl != primzahl:
            is_primzahl = False
            break

    if is_primzahl and zahl > bekannte_primzahlen[-1]:
        root1 = round(zahl ** 0.5)
        ungeradeTeilermenge1 = range(max(bekannte_primzahlen[-1] + 1, 3), round(root1) + 1, 2)
        for i in ungeradeTeilermenge1:
            if time.time() - startzeit > timeout:
                print("Berechnung abgebrochen (120s timeout)")
                return None
            if zahl % i == 0:
                is_primzahl = False
                break

    return is_primzahl

zahl = int(input("Alter, gib mal ne Zahl ein, von der du denkst, sie wäre eine Primzahl: "))
timeout = 120  # Timeout in Sekunden
result = primzahl_ueberpruefung(zahl, timeout)
if result is not None:
    if result and zahl > 1:
        print(zahl, "ist eine Primzahl Alter! Super!")
    else:
        print(zahl, "ist keine Primzahl Alter!")
