failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")
sisu = fail.read()
fail.close()
lause = sisu.upper().replace("Ä", "AE").replace("Õ", "OE").replace("Ö", "OE").replace("Ü", "UE")
print(lause)
 