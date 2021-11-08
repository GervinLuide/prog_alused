from tkinter import *
raam = Tk()
raam.title("Sindi lipp")
tahvel = Canvas(raam, width = 600, height = 500)
tahvel.create_rectangle(0, 0, 600, 100, fill = "dark red" )
tahvel.create_rectangle(0, 100, 600, 400, fill = "blue")
tahvel.create_rectangle(0, 400, 600, 500, fill = "dark red")
tahvel.pack()
raam.mainloop()