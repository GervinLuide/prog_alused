ringide_arv = int(input("Sisestage ringide arv: " ))
ringide_arv += 1
porgandid = 0
for i in range(2, ringide_arv, 2):
    porgandid += i
print(porgandid)
