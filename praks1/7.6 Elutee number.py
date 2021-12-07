def elutee(s):
    n = 0
    for i in s:
        if i != ".":
            n += int(i)
    if n < 10:
        return n
    else:
        return elutee(str(n))
    
fail = open("sunnikuupaevad.txt")
i = 1
while i <= 9:
    eluteee = open("eluteenumber" + str(i) + ".txt", "x")
    eluteee.close()
    i += 1
a = 1
for rida in fail:
    while eluteee(rida) != a:
        a += 1
    failinimi =  "eluteenumber" + str(a)
    failid = open(failinimi + ".txt", "i", encoding = "UTF-8")
    failid.write(rida + "\n")