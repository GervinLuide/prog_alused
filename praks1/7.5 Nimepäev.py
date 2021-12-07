from urllib.request import urlopen
kuu = input("Sisestage kuu: ")
failVeebis = urlopen("http://kodu.ut.ee/~eno/mooc/" + kuu)
baidid = failVeebis.read()
tekst = baidid.decode()
read_tekst = tekst.splitlines()
failVeebis.close()
paev = int(input("Sisestage päev: "))

i = 1
for rida in read_tekst:
    if i == paev:
        nimed = rida
        break
    i += 1
print("kuupäeval", ".", kuu, "on nimepäevad järgmiste nimedega inimestel", "\n" + nimed)