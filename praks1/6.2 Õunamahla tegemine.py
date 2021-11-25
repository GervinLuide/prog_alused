def mahlapakkide_arv(ounte_kogus):
    mahlapakkidearv = ounte_kogus * 0.4/3
    return round(mahlapakkidearv)
kogus = float(input("Mitu kilogrammi õunu on? "))
print(mahlapakkide_arv(kogus))