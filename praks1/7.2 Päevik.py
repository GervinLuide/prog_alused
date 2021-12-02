from datetime import datetime
kuupäev_kellaeg = datetime.today()
fail = open("paevik.txt", "a", encoding="UTF-8")

sisestatudtekst = input("Sisestage sissekande tekst: ")
fail.write(str(kuupäev_kellaeg) + "\n")
fail.write(sisestatudtekst + "\n")
fail.close()