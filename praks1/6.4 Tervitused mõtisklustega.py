def tervitus(järjekorranumber):
    i = 1
    while i <= järjekorranumber:
        print("täna " + str(i) + "kord tervitada, mõiskleb võõrustaja.")
        print("külaline: " + "'Tere, suur tänu kutse eest!'")
        print("võõrustaja: 'Tere!'")
        i += 1
külaliste_arv = int(input("Sisestage külaliste arv: "))
print(tervitus(külaliste_arv))
