kirja_suurus = float(input("Sisestage krija suurus: "))
pealkiri = input("Sisestage krija teema pealkiri: ")
fail = input("Kas kirjaga on kaasas fail? ")

if pealkiri == "" or fail == "jah" and kirja_suurus > 1:
    print ("kiri on spämm")
else:
    print("kiri ei ole spämm")
