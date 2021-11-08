ringid = int(input("Sisesta ringide arv: "))
i = 1
porgandid = 0
porgand = 0
while i <= ringid:
    porgandid += i
    i += 1
    porgand += porgandid
print("Porgandite koguarv on " + str(porgand))