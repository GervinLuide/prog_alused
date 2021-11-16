fail = open("rebased.txt", encoding="UTF-8")
aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))
aastad = 2011
for rida in fail:
    if aastad == aasta:
        print(aastad, " aastal oli vastuvõetuid ", rida )
        break
    aastad += 1
fail.close()
