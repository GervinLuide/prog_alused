def banner(reklaam):
    return reklaam.upper()
korda = int(input("Mitu korda soovite reklaamlaused kuvada? "))
reklaamlause = input("Sisestage reklaamlause: ")
i = 1
while i <= korda:
    print(banner(reklaamlause))
    i += 1