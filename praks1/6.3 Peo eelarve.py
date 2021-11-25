def eelarve(külaliste_arv):
    summa = 55 + külaliste_arv * 10
    return summa
inimesed = int(input("Mitu inimest on kutsutud? "))
tulemas = int(input("Mitu inimest tuleb? "))
print("Maksimaalne eelarve: " + str(eelarve(inimesed)))
print("Minimaalne eelarve: " + str(eelarve(tulemas)))