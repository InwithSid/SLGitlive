
from tkinter import *
from tkinter import ttk

main = Tk()
main.title("My Notebook App")
main.geometry('500x500+20+20')

rows = 0
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

nb = ttk.Notebook(main)
nb.grid(row=1, column=1, columnspan=50, rowspan=39, sticky="NSEW")

page1 = ttk.Frame(nb)
nb.add(page1, text="Home")

page2 = ttk.Frame(nb)
nb.add(page2, text="Page 1")

# lets create some objects on these pages

ent1pg1 = ttk.Entry(page1)
ent1pg1.pack()

bt1pg2 = ttk.Button(page2, text="Geeta")
bt1pg2.pack()


main.mainloop()
