import tkinter
from tkinter import*

root=Tk()
root.title("Calculator tutorial")
root.geometry("500x600")
root.configure(bg="#3b3b45")
root.resizable(False, False)

globalequation=""

def show(value):
    global globalequation
    globalequation+=value
    textlabel.config(text=globalequation)

def clear():
    global globalequation
    globalequation=""
    textlabel.config(text=globalequation)

def callculatethevalue():
    global globalequation
    realresult =""
    if globalequation!= "":
        try:
            realresult=eval(globalequation)
        except:
            realresult="error"
            globalequation=""
    textlabel.config(text=realresult)

textlabel = Label(root, text="", width=25, height=2, font=("arial", 30), fg="#fff", bg="#1f1f21")
textlabel.pack()

Button(root, width=3, height=1, text="C", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: clear()).place(x=20, y=110)
Button(root, width=3, height=1, text="%", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("%")).place(x=140, y=110)
Button(root, width=3, height=1, text="(", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("(")).place(x=260, y=110)
Button(root, width=3, height=1, text=")", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show(")")).place(x=380, y=110)

Button(root, width=3, height=1, text="7", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("7")).place(x=20, y=210)
Button(root, width=3, height=1, text="8", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("8")).place(x=140, y=210)
Button(root, width=3, height=1, text="9", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("9")).place(x=260, y=210)
Button(root, width=3, height=1, text="/", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("/")).place(x=380, y=210)

Button(root, width=3, height=1, text="4", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("4")).place(x=20, y=310)
Button(root, width=3, height=1, text="5", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("5")).place(x=140, y=310)
Button(root, width=3, height=1, text="6", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("6")).place(x=260, y=310)
Button(root, width=3, height=1, text="*", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("*")).place(x=380, y=310)

Button(root, width=3, height=1, text="1", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("1")).place(x=20, y=410)
Button(root, width=3, height=1, text="2", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("2")).place(x=140, y=410)
Button(root, width=3, height=1, text="3", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("3")).place(x=260, y=410)
Button(root, width=3, height=1, text="-", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("-")).place(x=380, y=410)

Button(root, width=3, height=1, text="0", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("0")).place(x=20, y=510)
Button(root, width=3, height=1, text=".", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show(".")).place(x=140, y=510)
Button(root, width=3, height=1, text="+", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: show("+")).place(x=260, y=510)
Button(root, width=3, height=1, text="=", font=("arial", 30, "bold"), fg="#fff", bg="#464673", command= lambda: callculatethevalue()).place(x=380, y=510)

root.mainloop()