nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): "))
ule_kiirus = tegelik_kiirus - lubatud_kiirus
trahv = ule_kiirus * 3
trahv_min = min(190, trahv)
print(nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv_min) + " eurot.")