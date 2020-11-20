# GUI
from tkinter import *
from tkinter import messagebox

from FlowchartDecision.Questions import QuestionChoice
from schemdraw import flow, schemdraw

# actual flowchart is stored here
class Flowchart(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # create a flowchart
        flow1 = PhotoImage(file="bannerimage.png")
        flow2 = PhotoImage(file="Itron.png")
        self.label1 = Label(self, image=flow1, anchor=CENTER, width=1600, height=600, bg="white")
        self.label1.image = flow1
        self.label2 = Label(self, image=flow2, anchor=CENTER, width=1600, height=600, bg="white")
        self.label2.image = flow2


# creation of banner title image
class Banner(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # create a banner image
        photo = PhotoImage(file="Itron.png")
        self.label01 = Label(self, image=photo, anchor=CENTER, width=620, height=120, bg="white")
        self.label01.image = photo
        self.label01.pack()


# creation of analyzer button and actions
class Analyzer(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # create button analyzer question with modes showing up
        self.btn1 = Button(self, text="Analyze", font="Helvetica 10 bold", command=self.clicked1, width=25)
        self.btn1.grid(column=0, row=0, padx=150)
        self.btn2 = Button(self, text="Start Over", font="Helvetica 10 bold", command=self.clicked2, width=25)
        self.btn2.grid(column=10, row=0, padx=150)
        self.labelnote = Label(self, bg="white", text='For a new scenario, please click "Start Over" to refresh first',
                          anchor=E,font='Helvetica 10 bold')
        self.labelnote.grid(column=10, row=2, padx=150)
        self.labelnote = Label(self, bg="white", text='Email ray.sang@itron.com for additional assistance',anchor=E,font='Helvetica 8')
        self.labelnote.grid(column=10, row=3, padx=150)

    # to add accounting decision scenarios here
    def clicked1(self):
        # populate flowchart

        # populate decision F  reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "No" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "No" and \
                question323.label03['text'] == "Yes" and \
                question3231.label03['text'] == "Yes" and \
                question314.label03['text'] == "Yes":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = \
                d3_2_2.params['fill'] = d3_2_3.params['fill'] = d3_2_3_1.params['fill'] = d3_1_4.params['fill'] = "pink"
            F.params['fill'] = "pink"
        # populate decision G reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "No" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "No" and \
                question323.label03['text'] == "Yes" and \
                question3231.label03['text'] == "Yes" and \
                question314.label03['text'] == "No":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = \
                d3_2_2.params['fill'] = d3_2_3.params['fill'] = d3_2_3_1.params['fill'] = d3_1_4.params['fill'] = "pink"
            G.params['fill'] = "pink"
        # populate decision J reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "No" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "No" and \
                question323.label03['text'] == "Yes" and \
                question3231.label03['text'] == "No":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params['fill'] = \
            d3_2_3.params['fill'] = d3_2_3_1.params['fill'] = "pink"
            J.params['fill'] = "pink"
        # populate decision L reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "No" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "No" and \
                question324.label03['text'] == "Yes" and \
                question313_3241.label03['text'] == "No":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params['fill'] = \
            d3_2_4.params['fill'] = d3_2_4_1.params['fill'] = "pink"
            L.params['fill'] = "pink"
        # populate decision K reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "No" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "No" and \
                question324.label03['text'] == "Yes" and \
                question313_3241.label03['text'] == "Yes":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params['fill'] = \
            d3_2_4.params['fill'] = d3_2_4_1.params['fill'] = "pink"
            K.params['fill'] = "pink"
        # populate decision M reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "No" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "No" and \
                question325.label03['text'] == "Yes":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params['fill'] = \
            d3_2_5.params['fill'] = "pink"
            M.params['fill'] = "pink"
        # populate decision N reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "No" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "No" and \
                question326.label03['text'] == "Yes":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params['fill'] = \
            d3_2_6.params['fill'] = "pink"
            N.params['fill'] = "pink"
        # populate decision O reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "No" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "No" and \
                question4.label03['text'] == "Yes":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params[
                'fill'] = "pink"
            O.params['fill'] = "pink"
        # populate decision I reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "No" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "No" and \
                question323.label03['text'] == "No" and \
                question324.label03['text'] == "No" and \
                question325.label03['text'] == "No" and \
                question326.label03['text'] == "No":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params[
                'fill'] = "pink"
            I.params['fill'] = "pink"
            O.params['fill'] = "pink"
        # populate decision H reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "No" and \
                question311_321.label03['text'] == "No":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = "pink"
            H.params['fill'] = "pink"
        # populate decision C reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "Yes" and \
                question311_321.label03['text'] == "No":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_1_1.params['fill'] = "pink"
            C.params['fill'] = "pink"
        # populate decision D reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "Yes" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "No" and \
                question313_3241.label03['text'] == "Yes":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_1_1.params['fill'] = d3_1_2.params['fill'] = d3_1_3.params['fill'] = "pink"
            D.params['fill'] = "pink"
        # populate decision E reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "Yes" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "No" and \
                question313_3241.label03['text'] == "No":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_1_1.params['fill'] = d3_1_2.params['fill'] = d3_1_3.params['fill'] = "pink"
            E.params['fill'] = "pink"
        # populate decision F on the customer route reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "Yes" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "Yes" and \
                question314.label03['text'] == "Yes":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_1_1.params['fill'] = d3_1_2.params['fill'] = d3_1_4.params['fill'] = "pink"
            F.params['fill'] = "pink"
        # populate decision G on the customer route reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "No" and \
                question3.label03['text'] == "Yes" and \
                question311_321.label03['text'] == "Yes" and \
                question312_322.label03['text'] == "Yes" and \
                question314.label03['text'] == "No":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_1_1.params['fill'] = d3_1_2.params['fill'] = d3_1_4.params['fill'] = "pink"
            G.params['fill'] = "pink"
        # populate decision B reviewed - pass
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "Yes" and \
                question21.label03['text'] == "Yes":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d2_1.params['fill'] = "pink"
            B.params['fill'] = "pink"

        # populate decision A checkgood reviewed - pass
        if question1.label03['text'] == "Yes":
            # new fill
            d1.params['fill'] = A.params['fill'] = "pink"

        # populate decision 2.1 back to 3
        if question1.label03['text'] == "No" and \
                question2.label03['text'] == "Yes" and \
                question21.label03['text'] == "No":
            # new fill
            d1.params['fill'] = d2.params['fill'] = d2_1.params['fill'] = "pink"
            # populate decision F 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "No" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "No" and \
                    question323.label03['text'] == "Yes" and \
                    question3231.label03['text'] == "Yes" and \
                    question314.label03['text'] == "Yes":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = \
                    d3_2_2.params['fill'] = d3_2_3.params['fill'] = d3_2_3_1.params['fill'] = d3_1_4.params[
                    'fill'] = "pink"
                F.params['fill'] = "pink"
            # populate decision G 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "No" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "No" and \
                    question323.label03['text'] == "Yes" and \
                    question3231.label03['text'] == "Yes" and \
                    question314.label03['text'] == "No":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = \
                    d3_2_2.params['fill'] = d3_2_3.params['fill'] = d3_2_3_1.params['fill'] = d3_1_4.params[
                    'fill'] = "pink"
                G.params['fill'] = "pink"
            # populate decision J 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "No" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "No" and \
                    question323.label03['text'] == "Yes" and \
                    question3231.label03['text'] == "No":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params[
                    'fill'] = \
                    d3_2_3.params['fill'] = d3_2_3_1.params['fill'] = "pink"
                J.params['fill'] = "pink"
            # populate decision L 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "No" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "No" and \
                    question324.label03['text'] == "Yes" and \
                    question313_3241.label03['text'] == "No":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params[
                    'fill'] = \
                    d3_2_4.params['fill'] = d3_2_4_1.params['fill'] = "pink"
                L.params['fill'] = "pink"
            # populate decision K 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "No" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "No" and \
                    question324.label03['text'] == "Yes" and \
                    question313_3241.label03['text'] == "Yes":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params[
                    'fill'] = \
                    d3_2_4.params['fill'] = d3_2_4_1.params['fill'] = "pink"
                K.params['fill'] = "pink"
            # populate decision M 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "No" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "No" and \
                    question325.label03['text'] == "Yes":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params[
                    'fill'] = \
                    d3_2_5.params['fill'] = "pink"
                M.params['fill'] = "pink"
            # populate decision N 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "No" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "No" and \
                    question326.label03['text'] == "Yes":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params[
                    'fill'] = \
                    d3_2_6.params['fill'] = "pink"
                N.params['fill'] = "pink"
            # populate decision O 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "No" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "No" and \
                    question4.label03['text'] == "Yes":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params[
                    'fill'] = "pink"
                O.params['fill'] = "pink"
            # populate decision I 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "No" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "No" and \
                    question323.label03['text'] == "No" and \
                    question324.label03['text'] == "No" and \
                    question325.label03['text'] == "No" and \
                    question326.label03['text'] == "No":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = d3_2_2.params[
                    'fill'] = "pink"
                I.params['fill'] = "pink"
                O.params['fill'] = "pink"
            # populate decision H 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "No" and \
                    question311_321.label03['text'] == "No":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_2_1.params['fill'] = "pink"
                H.params['fill'] = "pink"
            # populate decision C 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "Yes" and \
                    question311_321.label03['text'] == "No":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_1_1.params['fill'] = "pink"
                C.params['fill'] = "pink"
            # populate decision D 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "Yes" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "No" and \
                    question313_3241.label03['text'] == "Yes":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_1_1.params['fill'] = d3_1_2.params[
                    'fill'] = d3_1_3.params['fill'] = "pink"
                D.params['fill'] = "pink"
            # populate decision E 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "Yes" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "No" and \
                    question313_3241.label03['text'] == "No":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_1_1.params['fill'] = d3_1_2.params[
                    'fill'] = d3_1_3.params['fill'] = "pink"
                E.params['fill'] = "pink"
            # populate decision F on the customer route 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "Yes" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "Yes" and \
                    question314.label03['text'] == "Yes":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_1_1.params['fill'] = d3_1_2.params[
                    'fill'] = d3_1_4.params['fill'] = "pink"
                F.params['fill'] = "pink"
            # populate decision G on the customer route 2.1 back to 3 reviewed - pass
            if question1.label03['text'] == "No" and \
                    question3.label03['text'] == "Yes" and \
                    question311_321.label03['text'] == "Yes" and \
                    question312_322.label03['text'] == "Yes" and \
                    question314.label03['text'] == "No":
                # new fill
                d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d3_1_1.params['fill'] = d3_1_2.params[
                    'fill'] = d3_1_4.params['fill'] = "pink"
                G.params['fill'] = "pink"

        # action to draw
        d.draw()

    def clicked2(self):
        # reset questions
        question1.reset()
        question2.reset()
        question21.reset()
        question3.reset()
        question311_321.reset()
        question312_322.reset()
        question313_3241.reset()
        question314.reset()
        question323.reset()
        question3231.reset()
        question324.reset()
        question325.reset()
        question326.reset()
        question4.reset()
        # reset fill
        d1.params['fill'] = d2.params['fill'] = d3.params['fill'] = d2_1.params['fill'] = \
            d3_1_1.params['fill'] = d3_1_2.params['fill'] = d3_1_3.params['fill'] = d3_1_4.params['fill'] \
            = d3_2_1.params['fill'] = d3_2_2.params['fill'] = d3_2_3.params['fill'] = d3_2_3_1.params['fill'] \
            = d3_2_4.params['fill'] = d3_2_4_1.params['fill'] = d3_2_5.params['fill'] = d3_2_6.params['fill'] = \
            A.params['fill'] = B.params['fill'] = C.params['fill'] = D.params['fill'] = \
            E.params['fill'] = F.params['fill'] = G.params['fill'] = H.params['fill'] = \
            I.params['fill'] = J.params['fill'] = K.params['fill'] = L.params['fill'] = \
            M.params['fill'] = N.params['fill'] = O.params['fill'] = "None"

class LowerBanner(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # create a banner image
        photo = PhotoImage(file="bannerimage.png")
        # create a blank separater between the lower banner image and the questions
        self.label00 = Label(self, anchor=CENTER, width=1400, height=1, bg="white")
        self.label00.pack()
        # create the lower banner image
        self.label01 = Label(self, image=photo, anchor=CENTER, width=1400, height=200, bg="white")
        self.label01.image = photo
        self.label01.pack()


# main
if __name__ == "__main__":
    root = Tk()
    root.geometry("1400x920+60+10")
    root.title("Performance Issue Decision Maker")
    root["bg"] = "white"
    root.resizable(width=False, height=False)

    # add a banner
    banner = Banner(root)
    banner["bg"] = "white"

    # add questions 1 from QuestionChoice class
    question1 = QuestionChoice(root)
    question1.label01['text'] = "1. Is the issue part of an existing litigation or collection issue Itron has?"
    question1["bg"] = "white"

    # add questions 2 from QuestionChoice class
    question2 = QuestionChoice(root)
    question2.label01[
        'text'] = "2. Is the issue solely due to third-party goods and/or services Itron sold on behalf of our partners?"
    question2["bg"] = "white"

    # add questions 3 from QuestionChoice class
    question21 = QuestionChoice(root)
    question21.label01['text'] = "2.1. Can Itron pass through the entire issue to our 3rd party goods/services partner?"
    question21["bg"] = "white"

    # add questions 4 from QuestionChoice class
    question3 = QuestionChoice(root)
    question3.label01[
        'text'] = "3. Is the customer solely at fault for the performance issue or the performance issue is at least partly due to Itron performance? Y for customer's sole fault / N for Itron's liability"
    question3["bg"] = "white"

    # add questions 5 from QuestionChoice class
    question311_321 = QuestionChoice(root)
    question311_321.label01['text'] = "3.1.1/3.2.1 Are we obligated to remediate the issue per contract?"
    question311_321["bg"] = "white"

    # add questions 6 from QuestionChoice class
    question312_322 = QuestionChoice(root)
    question312_322.label01['text'] = "3.1.2/3.2.2 Is it within the warranty period and under warranty coverage?"
    question312_322["bg"] = "white"

    # add questions 7 from QuestionChoice class
    question313_3241 = QuestionChoice(root)
    question313_3241.label01[
        'text'] = "3.1.3/3.2.4.1. Are we incurring additional costs that can be considered as abnormal waste?"
    question313_3241["bg"] = "white"

    # add questions 8 from QuestionChoice class
    question314 = QuestionChoice(root)
    question314.label01['text'] = "3.1.4. Do we have enough warranty accrued to cover this issue?"
    question314["bg"] = "white"

    # add questions 9 from QuestionChoice class
    question323 = QuestionChoice(root)
    question323.label01[
        'text'] = "3.2.3. If remediation is not a direct warranty, are we offering credits and/or cash payments on the existing contract?"
    question323["bg"] = "white"

    # add questions 10 from QuestionChoice class
    question3231 = QuestionChoice(root)
    question3231.label01[
        'text'] = "3.2.3.1. Are the credits/payments direct reimbursements to customer's repair costs?"
    question3231["bg"] = "white"

    # add questions 11 from QuestionChoice class
    question324 = QuestionChoice(root)
    question324.label01[
        'text'] = "3.2.4. If remediation is not a direct warranty, are we offering free goods and services by incurring additional costs?"
    question324["bg"] = "white"

    # add questions 12 from QuestionChoice class
    question325 = QuestionChoice(root)
    question325.label01[
        'text'] = "3.2.5. If remediation is not a direct warranty, are we offering additional discounts in the existing associated contract?"
    question325["bg"] = "white"

    # add questions 13 from QuestionChoice class
    question326 = QuestionChoice(root)
    question326.label01[
        'text'] = "3.2.6. If remediation is not a direct warranty, are we offering discounts, credits and/or other incentives in future contracts?"
    question326["bg"] = "white"

    # add questions 14 from QuestionChoice class
    question4 = QuestionChoice(root)
    question4.label01['text'] = "4. Are we offering forms of remediation not listed above?"
    question4["bg"] = "white"

    # add analyzer
    analyzer = Analyzer(root)
    analyzer["bg"] = "white"

    # add a lowerbanner
    lowerbanner = LowerBanner(root)
    banner["bg"] = "white"

    # draw the base chart
    d = schemdraw.Drawing(fontsize=6.5, lw=1.2)
    b = d.add(flow.Start(w=4.5, h=5, label='Performance issue\naccrual decision'))
    d.add(flow.Line('down', xy=b.S, l=d.unit))
    d1 = d.add(flow.Decision(w=7, h=10, E='YES', S='NO',
                             label='1. Is it\npart of an existing\n litigationor collection\n issue Itron has?'))
    d.add(flow.Line(l=d.unit))
    d2 = d.add(flow.Decision(w=7, h=14, E='YES', S='NO',
                             label='2. Is it\nsolely due to third-party\ngoods and/or services Itron\nsold on behalf of our\npartners?'))
    d.add(flow.Line('down', l=d.unit))
    d3 = d.add(flow.Decision(w=7, h=14,
                             label='3. Is the\ncustomer solely at\nfault for the performance issue\nor the performance issue is at\nleast partly due to Itron\nperformance?'))

    d.add(flow.Line('right', xy=d1.E, l=d.unit / 2))
    A = d.add(flow.Box(w=5, h=5.5, label='A.Please consult Legal and\nRevenue Deal Desk', anchor='W'))
    d.add(flow.Line('right', xy=d2.E, l=d.unit * 1))
    d2_1 = d.add(
        flow.Decision(w=5, h=10, E='YES', S='NO', label='2.1 Can Itron\npass through the issue\nto our partner?',
                      anchor='W'))
    d.add(flow.Line('right', xy=d2_1.E, l=d.unit / 2))
    B = d.add(flow.Box(w=5, h=5.5, label='B.No action is required\nfrom Accounting', anchor='W'))
    d.add(flow.Line('down', xy=d2_1.S, toy=d3.E))
    d.add(flow.Arrow('left', tox=d3.E))

    d.add(flow.Line('down', xy=d3.S, l=d.unit * 3.5))
    d.add(flow.Line('right', l=d.unit * 1))
    d3_1_1 = d.add(flow.Decision(w=7, h=9, E='YES', N='NO', W='Yes - 3.1 CUSTOMER',
                                 label='3.1.1 Are we\nobligated to remediate\nper contract?', anchor='W'))
    d.add(flow.Line('up', xy=d3_1_1.N, l=d.unit))
    C = d.add(flow.Box(w=5, h=5.5, label='C.Account for remediation as\na contract modification', anchor='S'))
    d.add(flow.Line('right', xy=d3_1_1.E, l=d.unit * 1))
    d3_1_2 = d.add(flow.Decision(w=7, h=9.5, E='YES', N='NO',
                                 label='3.1.2 Is it within\nthe warranty period and under\nwarranty coverage?',
                                 anchor='W'))
    d.add(flow.Line("up", xy=d3_1_2.N, l=d.unit))
    d3_1_3 = d.add(flow.Decision(w=7, h=10.5, E='NO', N='YES',
                                 label='3.1.3 Are we\nincurring additional costs\nthat can be considered\nabnormal waste?',
                                 anchor='S'))
    d.add(flow.Line('up', xy=d3_1_3.N, l=d.unit))
    D = d.add(flow.Box(w=5, h=5.5, label='D.Treat such costs as costs\nof nonquality', anchor='S'))
    d.add(flow.Line('right', xy=d3_1_3.E, l=d.unit / 2))
    E = d.add(
        flow.Box(w=7, h=8, label='E.Treat free goods and services\nretroactively as a VC back\nto contract inception',
                 anchor='W'))

    d.add(flow.Line('right', xy=d3_1_2.E, l=d.unit / 2))
    d3_1_4 = d.add(flow.Decision(w=7, h=9, N='YES', E='NO',
                                 label='3.1.4 Do we have\nenough warranty accrued to\ncover this issue?', anchor='W'))
    d.add(flow.Line('up', xy=d3_1_4.N, l=d.unit))
    d.add(flow.Line('right', l=d.unit * 2))
    F = d.add(flow.Box(w=6, h=6.5, W='YES',
                       label='F.No additional accrual is equired when asset is\ncredited out, debit Warranty Liability',
                       anchor='W'))

    d.add(flow.Line('right', xy=d3_1_4.E, l=d.unit))
    G = d.add(
        flow.Box(w=6, h=6.5, W='NO', label='G.Request for a warranty accrual increase\n or a special warranty reserve',
                 anchor='W'))

    d.add(flow.Line('down', xy=d3.S, l=d.unit * 9))
    d.add(flow.Line('right', l=d.unit * 1))
    d3_2_1 = d.add(flow.Decision(w=7, h=9, E='YES', S='NO', W='No - 3.2 ITRON',
                                 label='3.2.1 Are we\nobligated to remediate\nper contract?', anchor='W'))
    d.add(flow.Line('down', l=d.unit))
    H = d.add(flow.Box(w=5.5, h=10,
                       label='H.Confirm with Legal and Revenue\nDeal Desk. Normally, if it is due\nto our performance, Itron is\nobligated to remediate',
                       anchor='N'))

    d.add(flow.Line('right', xy=d3_2_1.E, l=d.unit * 1))
    d3_2_2 = d.add(flow.Decision(w=7, h=9, E='YES', S='NO',
                                 label='3.2.2 Is it within\nthe warranty period and under\nwarranty coverage?',
                                 anchor='W'))
    d.add(flow.Line('down', xy=d3_2_2.S, l=d.unit))
    box1 = d.add(flow.box(w=9, h=68))
    d.add(flow.Line('right', xy=d3_2_2.E, tox=d3_1_4.S))
    d.add(flow.Arrow('up', toy=d3_1_4.S))

    d.add(flow.Line('down', xy=d3_2_2.S, l=d.unit * 2.5))
    d3_2_3 = d.add(flow.Decision(w=7, h=14, W='NO', E='YES',
                                 label='3.2.3 If remediation\nis not a direct warranty,\nare we offering credits and/or\ncash payments on the existing\ncontract?'))
    d.add(flow.Line('down', xy=d3_2_3.S, l=d.unit / 2))
    d3_2_4 = d.add(flow.Decision(w=7, h=14, W='NO', E='YES',
                                 label='3.2.4 If remediation\nis not a direct warranty,\nare we offering free goods and\nservices by incurring additional\ncosts?'))
    d.add(flow.Line('down', xy=d3_2_4.S, l=d.unit / 2))
    d3_2_5 = d.add(flow.Decision(w=7, h=14, W='NO', E='YES',
                                 label='3.2.5 If remediation\nis not a direct warranty,\nare we offering additional discounts\nin the existing associated\ncontract?'))
    d.add(flow.Line('down', xy=d3_2_5.S, l=d.unit / 2))
    d3_2_6 = d.add(flow.Decision(w=7, h=14, W='NO', E='YES',
                                 label='3.2.6 If remediation\nis not a direct warranty,\nare we offering discounts, credits,\nand/or other incentives in future\ncontracts?'))
    d.add(flow.Line('left', xy=d3_2_3.W, l=d.unit * 2))
    d.add(flow.Line('down', l=d.unit * 7.5))
    d.add(flow.Line('left', xy=d3_2_4.W, l=d.unit * 1.5))

    d.add(flow.Line('down', l=d.unit * 2.3))
    d.add(flow.Line('left', xy=d3_2_5.W, l=d.unit * 1.5))
    d.add(flow.Line('up', l=d.unit * 1.9))
    d.add(flow.Line('left', xy=d3_2_6.W, l=d.unit * 2))
    d.add(flow.Line('up', l=d.unit * 7))
    I = d.add(flow.Box(w=6, h=3, label='I.No further action required from these categories.', anchor='S'))

    d.add(flow.Line('right', xy=d3_2_3.E, l=d.unit / 2))
    d3_2_3_1 = d.add(flow.Decision(w=7, h=10, N='YES', E='NO',
                                   label='3.2.3.1 Are the\ncredits/payments direct\nreimbursements to customer repair\ncosts?',
                                   anchor='W'))
    d.add(flow.Line('right', xy=d3_2_3_1.E, l=d.unit / 2))
    J = d.add(flow.Box(w=4, h=5, label='J. Account for the\ncredits/payments as a VC', anchor='W'))
    d.add(flow.Line('up', xy=d3_2_3_1.N, toy=d3_2_2.E))
    d.add(flow.Line('left', l=d.unit / 1.2))

    d.add(flow.Line('right', xy=d3_2_4.E, l=d.unit / 1))
    d3_2_4_1 = d.add(flow.Decision(w=6, h=12, N='YES', S='NO',
                                   label='3.2.4.1 Are we\nincurring additional costs that\ncan be considered as abnormal\nwaste?',
                                   anchor='W'))
    d.add(flow.Line('up', xy=d3_2_4_1.N, l=d.unit))
    d.add(flow.Line('right', l=d.unit * 1.5))
    K = d.add(flow.Box(w=4, h=6, label='K. Treat such costs as costs of\nnonquality', anchor='W'))

    d.add(flow.Line('down', xy=d3_2_4_1.S, l=d.unit))
    d.add(flow.Line('right', l=d.unit * 1.5))
    L = d.add(flow.Box(w=4, h=8,
                       label='L. Treat free goods and services\nretrospectively as a VC back to\ncontract inception',
                       anchor='W'))

    d.add(flow.Line('right', xy=d3_2_5.E, l=d.unit / 2))
    M = d.add(flow.Box(w=6, h=6, label='M.Treat the discounts retrospectively\nas a VC back to contract inception',
                       anchor='W'))

    d.add(flow.Line('right', xy=d3_2_6.E, l=d.unit / 2))
    N = d.add(flow.Box(w=6, h=6, label='N.Please consult Revenue\nDeal Desk', anchor='W'))

    d.add(flow.Line('down', xy=d3_2_6.S, l=d.unit * 2))
    O = d.add(flow.Box(w=4.5, h=8,
                       label='O.If we are offering forms of\nremdediation not listed above, please\nconsult Revenue Deal Desk'))
    # main loop
    root.mainloop()
