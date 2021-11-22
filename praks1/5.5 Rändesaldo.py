fail = open("sisseranne.txt", encoding="UTF-8")
sisseranne = []
for rida in fail:
    sisseranne.append(rida)
fail.close()
fail = open("valjaranne.txt", encoding="UTF-8")
valjaranne = []
for rida in fail:
    valjaranne.append(rida)
fail.close()
saldo = []
i = 0
while i < 10:
    saldo.append(int(sisseranne[i]) - int(valjaranne[i]))
    i += 1
print(saldo)
if max(saldo) > 0:
    print("Suurim positiivne rändesaldo oli " + str(i) + ". aastal." )
else:
    print("Positiivse rändesaldoga aastaid ei ole.")