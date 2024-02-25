
from tkinter import  *
root = Tk()
math = ""
root.title("@x0ki")
MyEntry = Entry(root,width=30,borderwidth=10)
MyEntry.insert(0,"")
MyEntry.grid(column=0,row=0,columnspan=4,padx=10,pady=10)
e = MyEntry
def NumClick(num):
    current = e.get()
    e.delete(0 , END)
    e.insert(0 ,str(current) + str(num))

def clear():
    e.delete(0,END)

def equal():
    snum = e.get()
    secondnum = int(snum)
    e.delete(0,END)
    if "divide" in math:
        e.insert(0, fnum / secondnum)

    elif "addition" in math:
        e.insert(0, fnum + secondnum)

    elif "multi" in math:
        e.insert(0, fnum * secondnum)

    elif "minus" in math:
        e.insert(0, fnum - secondnum)




def divide():

    firstnum = e.get()
    global math
    global fnum
    fnum = int(firstnum)

    math = "divide"
    e.delete(0,END)


def minus():

    firstnum = e.get()
    global fnum
    global math
    fnum = int(firstnum)
    math = "minus"
    e.delete(0,END)

def by():

    firstnum = e.get()
    global fnum
    global math
    fnum = int(firstnum)
    math = "multi"
    e.delete(0,END)


def add():

    firstnum = e.get()
    global fnum
    global math
    fnum = int(firstnum)
    math = "addition"
    e.delete(0,END)

 #BUTTONS NAMES AND PLACES

BUTTON1=Button(root,text="1",padx=20,pady=10,fg="black",bg="purple",command=lambda : NumClick(1))
BUTTON2=Button(root,text="2",padx=20,pady=10,fg="black",bg="purple",command=lambda : NumClick(2))
BUTTON3=Button(root,padx=20,text="3",pady=10,fg="black",bg="purple",command=lambda : NumClick(3))
BUTTON4=Button(root,text="4",padx=20,pady=10,fg="black",bg="purple",command=lambda : NumClick(4))
BUTTON5=Button(root,text="5",padx=20,pady=10,fg="black",bg="purple",command=lambda : NumClick(5))
BUTTON6=Button(root,text="6",padx=20,pady=10,fg="black",bg="purple",command=lambda :NumClick(6))
BUTTON7=Button(root,text="7",padx=20,pady=10,fg="black",bg="purple",command=lambda :NumClick(7))
BUTTON8=Button(root,text="8",padx=20,pady=10,fg="black",bg="purple",command=lambda :NumClick(8))
BUTTON9=Button(root,text="9",padx=20,pady=10,fg="black",bg="purple",command=lambda :NumClick(9))
BUTTON0=Button(root,text="0",padx=47,pady=10,fg="black",bg="purple",command=lambda :NumClick(0))
BUTTONminus=Button(root,text="-",padx=20,pady=10,fg="black",bg="purple",command=minus)
BUTTONplus=Button(root,text="+",padx=20,pady=10,fg="black",bg="purple",command=add)
BUTTONdivide=Button(root,text="/",padx=20,pady=10,fg="black",bg="purple",command=divide)
BUTTONx=Button(root,text="X",padx=20,pady=10,fg="black",bg="purple",command=by)
BUTTONclear=Button(root,text="C",padx=75,pady=10,fg="black",bg="purple",command=clear)
BUTTONequal=Button(root,text="=",padx=48,pady=10,fg="black",bg="purple",command=equal)



BUTTON1.grid(column=0,row=4)
BUTTON2.grid(column=1,row=4)
BUTTON3.grid(column=2,row=4)

BUTTON4.grid(column=0,row=3)
BUTTON5.grid(column=1,row=3)
BUTTON6.grid(column=2,row=3)

BUTTON7.grid(column=0,row=2)
BUTTON8.grid(column=1,row=2)
BUTTON9.grid(column=2,row=2)
BUTTON0.grid(column=0,row=5,columnspan=2)

BUTTONplus.grid(column=3,row=4)
BUTTONminus.grid(column=3,row=3)
BUTTONx.grid(column=3,row=2)
BUTTONdivide.grid(column=3,row=1)
BUTTONclear.grid(column=0,row=1,columnspan=3)
BUTTONequal.grid(column=2,row=5,columnspan=2)

root.mainloop()
