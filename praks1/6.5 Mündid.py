def pronksikarva_summa(ts_järjend):
    summa = 0
    for mündid in ts_järjend:
        if int(mündid) <= 5:
            summa += int(mündid)
    return summa
faili_nimi = input("sisestage failinimi: ")
fail = open(faili_nimi, encoding="UTF-8")
print("Hoiupõrsasse läheb " + str(pronksikarva_summa(fail)) + " senti.")