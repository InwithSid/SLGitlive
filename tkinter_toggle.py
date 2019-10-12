from tkinter import *
class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Set up frame
        container = Frame(self)
        container.pack(side='top', fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Welcome to GES")
        label.pack(padx=10, pady=10)

        bt1 = Button(self, text="to page 1", command=lambda: controller.show_frame(PageOne))
        bt1.pack()


class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Welcome to page 1")
        label.pack(padx=10, pady=10)

        bt3 = Button(self, text="to page 2", command=lambda: controller.show_frame(PageTwo))
        bt3.pack()


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Welcome to page 2")
        label.pack(padx=10, pady=10)

        bt2 = Button(self, text="to start page", command=lambda: controller.show_frame(StartPage))
        bt2.pack()

app = App()
app.mainloop()
