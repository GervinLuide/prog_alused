from easygui import *
input1 = integerbox("Sisestage esimene täisarv lõigus 1-10:")
input2 = integerbox("Sisestage teine täisarv lõigus 1-10:")
nupud = ["+", "-", "*"]
vajuta = buttonbox("Valige tehe:", choices = nupud)
if vajuta == "+":
    summa = input1 + input2
elif vajuta == "-":
    summa = input1 - input2
elif vajuta == "*":
    summa = input1 * input2
msgbox("Tehte tulemus on: " + str(summa))
