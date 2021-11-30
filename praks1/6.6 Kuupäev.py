def kuu_nimi(kuu_järjekorranumber):
    kuud = ["jaanuar", "veebruar", "märts", "april", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[int(kuu_järjekorranumber) -1]

def kuupäev_sõnena(kuupäev):
    kuupäevad = kuupäev.split(".")
    kuupäev = kuupäevad[0] + "." + kuu_nimi(kuupäevad[1]) + " " + kuupäevad[2] + ". a"
    return kuupäev

kuupäev = str(input("Sisestage kuupäev kujul DD.MM.YYYY: "))
print(str(kuupäev_sõnena(kuupäev)))