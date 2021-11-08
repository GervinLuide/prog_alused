from random import randint
õunasoovijaid = int(input("Mitu pöialpoissi tahab õuna? "))
õunad = 14
i = 0
while i < õunasoovijaid:
    i += 1
    r = randint(1,2)
    õunad = õunad - r
    print(str(r))
print("Lumivalgekesele jäi " + str(õunad))