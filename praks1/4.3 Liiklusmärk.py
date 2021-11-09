from tkinter import *
raam = Tk()
raam.title("Keelumärk")
tahvel = Canvas(raam, width = 700, height = 700 )
tahvel.create_oval(10, 10, 700, 700, fill = "red", outline = "red")
tahvel.create_rectangle(60, 290, 640, 410, fill = "white", outline = "white")
tahvel.pack()
raam.mainloop()