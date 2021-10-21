inimeste_arv = int(input("Sisestage inimeste arv: "))
bussi_kohtade_arv = int(input("Sisestage bussis kohtade arv: "))
mahajäänud = inimeste_arv % bussi_kohtade_arv
buss_arv = (inimeste_arv - mahajäänud) / bussi_kohtade_arv
print("Vaja läheb " + str(int(buss_arv)) + " bussi")
print("maha jääb " + str(mahajäänud) + " inimest")