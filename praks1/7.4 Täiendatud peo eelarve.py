failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")

def eelarve(külalistearv):
    eelarve = 55 + külalistearv * 10
    return eelarve
tulevad = 0
kokku = 0

for rida in fail:
    for nimi in rida:
        if nimi == "+":
            tulevad += 1
        kokku += 1
        break

print("Kutsutud on ", kokku, "inimest")
print(tulevad, "inimest tuleb")
print("Maksimaalne eelarve: ", str(eelarve(kokku)))
print("Minimaalne eelarve: ", str(eelarve(tulevad)))
