def elutee(s):
    n = 0
    for u in s:
        if u != ".":
            n += int(u)
    if n < 10:
        return n
    else:
        return elutee(str(n))
   
a = 1
while a <= 9:
    eluteee = open("eluteenumber" + str(a) + ".txt", "x")
    eluteee.close()
    a += 1
b = 1
fail = open("sunnikuupaevad.txt")
for rida in fail:
    while elutee(rida[:-1]) != b:
        b += 1
    failinimi =  "eluteenumber" + str(b)
    failid = open(failinimi + ".txt", "a", encoding = "UTF-8")
    failid.write(rida + "\n")
    failid.close()