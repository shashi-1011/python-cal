import tkinter
from tkinter import *
from tkinter import messagebox
val=""
A=0
operator =""
def btn1_is_clicked():
    global val
    val = val +"1"
    data.set(val)


def btn2_is_clicked():
    global val
    val = val +"2"
    data.set(val)

def btn3_is_clicked():
    global val
    val = val +"3"
    data.set(val)

def btn4_is_clicked():
    global val
    val = val +"4"
    data.set(val)

def btn5_is_clicked():
    global val
    val = val +"5"
    data.set(val)

def btn6_is_clicked():
    global val
    val = val +"6"
    data.set(val)

def btn7_is_clicked():
    global val
    val = val +"7"
    data.set(val)

def btn8_is_clicked():
    global val
    val = val +"8"
    data.set(val)

def btn9_is_clicked():
    global val
    val = val +"9"
    data.set(val)

def btn0_is_clicked():
    global val
    val = val +"0"
    data.set(val)

def butnplus_clicked():
    global A
    global val
    global operator
    A = int(val)
    operator= "+"
    val = val + '+'
    data.set(val)

def butndiv_clicked():
    global A
    global val
    global operator
    A = int(val)
    operator=  "/"
    val = val + '/'
    data.set(val)

def butnminus_clicked():
    global A
    global val
    global operator
    A = int(val)
    operator= "-"
    val = val + '-'
    data.set(val)

def butnmul_clicked():
    global A
    global val
    global operator
    A = int(val)
    operator= "*"
    val = val + '*'
    data.set(val)

def c_pres():
    global A
    global val
    global operator
    val = ""
    A = ""
    operator = ""
    data.set(val)

def result():
    global A
    global val
    global operator
    val12 = val
    if operator == "+":
        x = int(val12.split("+")[1])
        c = A+x
        data.set(c)
        val = str(c)
    elif  operator == "-":
        x = int(val12.split("-")[1])
        c = A-x
        data.set(c)
        val = str(c)
    elif operator == "*":
        x = int(val12.split("*")[1])
        c = A*x
        data.set(c)
        val = str(c)
    elif operator == "/":
         x = int(val12.split("/")[1])
         if x ==0:
             messagebox.showerror("Error", 'sorry wronf input')
             A=""
             val=""
             data.set(val)
         else:
             c =int(A/x)
             data.set(c)
             





















root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("caluclator")
data = StringVar()
lbl =  Label(
    root,
    text="label",
    anchor=SE,
    font= ("verdana", 20),
    textvariable=data,
    background="#ffffff",
    fg="#000000",
)
lbl.pack( expand=True, fill="both")
btnrow1 = Frame(root)
btnrow1.pack(expand=True, fill="both",)

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both",)

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both",)

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both",)

btn1 = Button(
    btnrow1,
    text="1",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn1_is_clicked,
)
btn1.pack(side=LEFT, expand=True, fill="both",)

btn2 = Button(
    btnrow1,
    text="2",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn2_is_clicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)

btn3 = Button(
    btnrow1,
    text="3",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn3_is_clicked,

)
btn3.pack(side=LEFT, expand=True, fill="both",)

btnplus = Button(
    btnrow1,
    text="+",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command = butnplus_clicked,
    
)
btnplus.pack(side=LEFT, expand=True, fill="both",)


#row2
btn4 = Button(
    btnrow2,
    text="4",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn4_is_clicked,

)
btn4.pack(side=LEFT, expand=True, fill="both",)

btn5 = Button(
    btnrow2,
    text="5",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn5_is_clicked,

)
btn5.pack(side=LEFT, expand=True, fill="both",)

btn6 = Button(
    btnrow2,
    text="6",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn6_is_clicked,

)
btn6.pack(side=LEFT, expand=True, fill="both",)

btnminus = Button(
    btnrow2,
    text="-",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command = butnminus_clicked
)
btnminus.pack(side=LEFT, expand=True, fill="both",)

#row3
btn7 = Button(
    btnrow3,
    text="7",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn7_is_clicked,

)
btn7.pack(side=LEFT, expand=True, fill="both",)
btn8 = Button(
    btnrow3,
    text="8",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn8_is_clicked,

)
btn8.pack(side=LEFT, expand=True, fill="both",)

btn9 = Button(
    btnrow3,
    text="9",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn9_is_clicked,

)
btn9.pack(side=LEFT, expand=True, fill="both",)

btnmultiply = Button(
    btnrow3,
    text="*",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command= butnmul_clicked
)
btnmultiply.pack(side=LEFT, expand=True, fill="both",)

#row4
btnce = Button(
    btnrow4,
    text="CE",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=c_pres,
)
btnce.pack(side=LEFT, expand=True, fill="both",)

btn0 = Button(
    btnrow4,
    text="0",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn0_is_clicked,

)
btn0.pack(side=LEFT, expand=True, fill="both",)

btnequal = Button(
    btnrow4,
    text="=",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command= result,
)
btnequal.pack(side=LEFT, expand=True, fill="both",)

btndiv = Button(
    btnrow4,
    text="/",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=butndiv_clicked,
)
btndiv.pack(side=LEFT, expand=True, fill="both",)

root.mainloop()