def tervitus(järjekorranumber):
    i = 1
    while i <= järjekorranumber:
        print("Võõrustaja: 'Tere!'")
        print("täna " + str(i) + ". kord tervitada, mõiskleb võõrustaja.")
        print("külaline: " + "'Tere, suur tänu kutse eest!'")
        i += 1
külaliste_arv = int(input("Sisestage külaliste arv: "))
print(tervitus(külaliste_arv))
