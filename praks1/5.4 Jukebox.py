fail = input("Palun sisestage failinimi: (jukebox, 80ndad, eesti_muusika, edm)")
fail = fail + ".txt"
failid = open(fail, encoding="UTF-8")
print("Muusikapalade valik:")
i = 1
for laul in failid:
    print(i, ".", laul[:-1])
    i += 1
järjekorra_number = int(input("Valige laulu järjekorranumber: "))
failid.close()
failid = open(fail, encoding="UTF-8")
o = 1
for laul in failid:
    if o == järjekorra_number:
        print("Mängitav muusikapala on ", laul)
        break
    else:
        o += 1
failid.close()
    
