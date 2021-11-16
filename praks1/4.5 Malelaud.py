from tkinter import *
raam = Tk()
raam.title("Malelaud")
tahvel = Canvas(raam, width = 800, height = 800)
i = 0
while i <= 600:
    j = 0
    while j <= 600:
        tahvel.create_rectangle(i, j, i + 100, j + 100, fill = "black")
        tahvel.create_rectangle(i + 100, j + 100, i + 200, j + 200, fill = "black")
        tahvel.create_rectangle(i, j + 100, i + 100, j + 200, fill = "white")
        tahvel.create_rectangle(i + 100, j, i + 200, j + 100, fill = "white")
        j += 200
    i += 200
tahvel.pack()
raam.mainloop()