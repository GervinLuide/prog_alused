vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu: ") .upper()
tüüp = int(input("Sisestage treeningu tüüp: "))

if (sugu == "M"):
    tervisetreening = 220 - vanus

if (sugu == "N"):
    tervisetreening = 206 - (vanus * 0.88)

if tüüp == 1:
    tervisetreening_min = round(tervisetreening * 0.5)
    tervisetreening_max = round(tervisetreening * 0.7)

elif tüüp == 2:
    tervisetreening_min = round(tervisetreening * 0.7)
    tervisetreening_max = round(tervisetreening * 0.80)
    
elif tüüp == 3:
    tervisetreening_min = round(tervisetreening * 0.8)
    tervisetreening_max = round(tervisetreening * 0.87)
    
print("Pulsisagedus peaks olema vahemikus " + str(tervisetreening_min) + " kui " + str(tervisetreening_max) + ".")
    
    
    
    
    
    