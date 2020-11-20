from tkinter import *


class QuestionChoice(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):

        # create label question with modes showing up
        self.label01 = Label(self, text="this is a question?", font="Helvetica 10 bold", anchor=W, width=150, height=2, bg="white")
        self.label01.grid(column=0, row=0, pady=0, ipady=0, ipadx=0)

        # create toggle button with modes showing up
        global togglegif1, togglegif2
        togglegif1 = PhotoImage(file="Frame 1.png")
        togglegif2 = PhotoImage(file="Frame 2.png")
        self.label02 = Label(self, image=togglegif1, anchor=E, width=30, height=10, bg="white")
        self.label02.image = togglegif1
        self.label02.grid(column=1, row=0, pady=0, ipady=0, ipadx=0)
        self.label02.bind('<Button-1>', self.clicked)
        self.label03 = Label(self, text="No", bg="white", width=10, height=0, font="Helvetica 10 bold")
        self.label03.grid(column=2, row=0, sticky=E, ipady=0, ipadx=0)

        # toggle event

    def clicked(self, event):
        if self.label03['text'] == "No":
            self.label03.configure(text="Yes")
            self.label02.configure(image=togglegif2)

        else:
            self.label03.configure(text="No")
            self.label02.configure(image=togglegif1)

    def reset(self):
        self.label03.configure(text="No")
        self.label02.configure(image=togglegif1)
