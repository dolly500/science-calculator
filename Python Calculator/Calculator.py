from tkinter import*
import math
import parser
import tkinter.messagebox
from flask import Flask
app = Flask(__name__)

root = Tk()
root.title("Scientific Calculator")
root.config(background="grey")
root.resizable(width=False, height=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()
 
txtDisplay =  Entry(calc,font=('Times New Roman', 20, 'bold'), bg="powder blue", bd=30, width=29, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

def pad1():
    numberpad = "7"
    return numberpad
pad1

def new_func():
    numberpad = "789456123"
    return numberpad
new_func
numberpad = new_func()
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('Times New Roman', 20, 'bold'),bd = 4, text = numberpad[i]))
        btn[i].grid(row=j, column = k, pady=1)
        
        i = i + 1

#==========================#============================

btnClear = Button(calc, text=chr(67), width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =1, column =0, pady=1)
btnAllClear = Button(calc, text=chr(67) + chr(69), width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =1, column =1, pady=1)
btnSq = Button(calc, text=" √", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =1, column =2, pady=1)
btnAdd = Button(calc, text="+", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =1, column =3, pady=1)

btnSub = Button(calc, text="-", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =2, column =3, pady=1)
btnMult = Button(calc, text="*", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =3, column =3, pady=1)
btnDiv = Button(calc, text= chr(247), width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =4, column =3, pady=1)


btnZero = Button(calc, text="0", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =5, column =0, pady=1)
btnDot = Button(calc, text=".", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =5, column =1, pady=1)
btnPM = Button(calc, text=chr(177), width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =5, column =2, pady=1)
btnEquals = Button(calc, text= "=", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =5, column =3, pady=1)


#============Scientific Calculator============================================

btnPi = Button(calc, text="Pi", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =1, column =4, pady=1)
btnCos = Button(calc, text="Cos", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =1, column =5, pady=1)
btntan= Button(calc, text="tan", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =1, column =6, pady=1)
btnsin = Button(calc, text="sin", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =1, column =7, pady=1)

#==================================================================================

btn2pi = Button(calc, text="2pi", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =2, column =4, pady=1)
btnCosh = Button(calc, text="Cosh", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =2, column =5, pady=1)
btnTanh= Button(calc, text="Tanh", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =2, column =6, pady=1)
btnsinh = Button(calc, text= "sinh", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =2, column =7, pady=1)

#===============================================================================

btnlog = Button(calc, text="log", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =3, column =4, pady=1)
btnExp = Button(calc, text="Exp", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =3, column =5, pady=1)
btnMod = Button(calc, text="Mod", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =3, column =6, pady=1)
btnE = Button(calc, text="E", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =3, column =7, pady=1)

#===================================================================================

btnlog2 = Button(calc, text="log", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =4, column =4, pady=1)
btndeg = Button(calc, text="deg", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =4, column =5, pady=1)
btnacosh = Button(calc, text="acosh", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =4, column =6, pady=1)
btnasinh = Button(calc, text="asinh", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =4, column =7, pady=1)

#=================================================================================

btnlog10 = Button(calc, text="log10", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =5, column =4, pady=1)
btnCos = Button(calc, text="Cos", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =5, column =5, pady=1)
btnexpm1 = Button(calc, text="expm1", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =5, column =6, pady=1)
btn1gamma = Button(calc, text="1gamma", width = 6,  height=2, font=('Times New Roman', 20, 'bold'), bd=4, bg="powder blue").grid(row =5, column =7, pady=1)


#==========================Menu and function====================================

def iExit():
    iExit= tkinter.messagebox.askyesno("Scientific Calculator","Confirm if you want to Exit")
    if iExit > 0:
        root.destroy()
    return


def Scientific():
    root.resizable(width=False, height=False)
    if iExit == 1:
        root.focus()
    root.geometry("944x568+0+0")

def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "file", menu=filemenu)
filemenu.add_command(label = "Standard", command= Standard)
filemenu.add_command(label = "Scientific", command= Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command=iExit)

editmenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "Edit", menu=editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_command(label="Add")
editmenu.add_command(label="select")
editmenu.add_separator
editmenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "help", menu=helpmenu)
helpmenu.add_command(label = "View help")

root.configure(menu=menubar)
root.mainloop()
