fail = open("konto.txt", encoding="UTF-8")
for arv in fail:
    if float(arv) > 0:
        print(arv[:-1])
fail.close()