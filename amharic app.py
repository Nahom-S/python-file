from tkinter import *

me = Tk()
me.title("ልምምድ")

e = Entry(me, width=35, bg="blue", fg="yellow", borderwidth=5)
e.grid(row=0, column=1, columnspan=1, padx=40, pady=40)


def button1():
    try:
        x = e.get()
        e.delete(0, END)
        c = int(x) + 1
        e.insert(0, c)
    except:
        e.delete(0, END)
        e.insert(0, "ቁጥር ያስገቡ")


button1 = Button(me, text="አንድ ጨምር", bg="red", fg="green", padx=20, pady=10, command=button1)
button1.grid(row=1, column=1)
xx = Label(me, text="                                      አሁን እዚህ ቁጥር ላይ ነን------->", padx=30, pady=30)
xx.grid(row=0, column=0)
me.mainloop()
