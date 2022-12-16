from tkinter import *
import tkinter.messagebox
import tkinter.font as font

root1=Tk()
root1.geometry("420x220+0+0")
root1.title("Login Page")
name_inp= StringVar()
password_inp= StringVar()
fnt = font.Font(family="Helevitica", size=10, weight=font.BOLD)
fn = font.Font(family="ARIAL", size=15, weight=font.BOLD)
root1['bg']='powder blue'


def enter():
    if name_inp.get()=="Pa Pa" and password_inp.get()=="1270":
        root1.destroy()
        import  KITCHEN
    else:
        tkinter.messagebox.showinfo("Error","Authentification Failed")
        name_inp.set("")
        password_inp.set("")
def destroy():
    root1.destroy()
label=Label(root1,text="007'S ASSORTED KITCHEN",fg="steel blue",bd=10,anchor="w",bg='powder blue',font=fn)
label.grid(row=0,column=1)
label1=Label(root1,text="Username :",bg='powder blue',font=fnt)
label2=Label(root1,text="Pin :",bg='powder blue',font=fnt)


entry1=Entry(root1,textvariable=name_inp,relief=RIDGE,width=50)
entry2=Entry(root1,textvariable=password_inp,relief=RIDGE,width=50)
label1.grid(row=1,sticky=E)
label2.grid(row=2,sticky=E)
entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)
enter_btn=Button(root1,text="Enter",command=enter,font=fnt,bg='powder blue',fg="steel blue",relief=RIDGE)
enter_btn.grid(row=3,column=1)
ext=Button(root1,text="Exit",fg="steel blue",bg="powder blue",font=fnt,width=5,relief=RIDGE,command=lambda:destroy())
ext.grid(row=3,column=0)


root1.mainloop

