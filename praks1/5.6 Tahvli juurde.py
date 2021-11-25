failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")

from datetime import *
kuupäev = (datetime.now().day)
i = 1
for nimi in fail:
    if i == kuupäev:
        print("Vastama tuleb: " + nimi)
        break
    else:
        i += 1