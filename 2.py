from tkinter import *
import parser
import tkinter.messagebox
root = Tk()
root.title("calculator",)
#input
i=0
def getvariable(num):
    global i
    display.insert(i,num)
    i+=1
def clearall():
    display.delete(0,END)
def delete():
    str1=display.get()
    if(len(str1)>0):
        str2=str1[:-1]
        clearall()
        display.insert(0,str2)
def getoprtr(optr):
    global i
    len1=len(optr)
    display.insert(i,optr)
    i+=len1
def calculate():
    str1=display.get()
    try:
        a=parser.expr(str1).compile()
        result=eval(a)
        clearall()
        display.insert(0,result)
    except Exception:
        clearall()
        display.insert(0,"Error")

def factorial(n):
    fact = 1
    while (n > 0):
        fact = fact * n
        n = n - 1
    clearall()
    display.insert(0,fact)


#display panel
display=Entry(root)
display.grid(row=0,columnspan=6,sticky=W+E)
#BUTTONS
Button(root,text="AC",command=lambda : clearall()).grid(row=0,column=5)
Button(root,text="7",command=lambda : getvariable(7)).grid(row=1,column=0)
Button(root,text="8",command=lambda : getvariable(8)).grid(row=1,column=1)
Button(root,text="9",command=lambda : getvariable(9)).grid(row=1,column=2)
Button(root,text="/",command=lambda : getoprtr("/")).grid(row=1,column=3)
Button(root,text="pi",command=lambda : getoprtr("3.14")).grid(row=1,column=4)
Button(root,text="<-",command=lambda : delete()).grid(row=1,column=5)

Button(root,text="4",command=lambda : getvariable(4)).grid(row=2,column=0)
Button(root,text="5",command=lambda : getvariable(5)).grid(row=2,column=1)
Button(root,text="6",command=lambda : getvariable(6)).grid(row=2,column=2)
Button(root,text="*",command=lambda : getoprtr("*")).grid(row=2,column=3)
Button(root,text="%",command=lambda : getoprtr("%")).grid(row=2,column=4)
Button(root,text="x !",command=lambda :factorial(int(display.get()))).grid(row=2,column=5)

Button(root,text="1",command=lambda : getvariable(1)).grid(row=3,column=0)
Button(root,text="2",command=lambda : getvariable(2)).grid(row=3,column=1)
Button(root,text="3",command=lambda : getvariable(3)).grid(row=3,column=2)
Button(root,text="-",command=lambda : getoprtr("-")).grid(row=3,column=3)
Button(root,text=" ( ",command=lambda : getoprtr("(")).grid(row=3,column=4)
Button(root,text=" ) ",command=lambda : getoprtr(")")).grid(row=3,column=5)

Button(root,text=". ",command=lambda : getoprtr(".")).grid(row=4,column=0)
Button(root,text="0",command=lambda : getvariable(0)).grid(row=4,column=1)
Button(root,text="+",command=lambda : getoprtr("+")).grid(row=4,column=3)
Button(root,text="=",command=lambda : calculate()).grid(row=4,column=2)
Button(root,text=" e",command=lambda : getoprtr("2.71828")).grid(row=4,column=4)
Button(root,text="^2",command=lambda : getoprtr("**2")).grid(row=4,column=5)




root.mainloop()


