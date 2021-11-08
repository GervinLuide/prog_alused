from random import randint
täringute_arv = int(input("Täringute arv: "))
i = 0
while i < täringute_arv:
    täringud = randint(1,6)
    i += 1
    print(str(täringud))