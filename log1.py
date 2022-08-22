import tkinter
from tkinter import messagebox
from tkinter import *
root = tkinter.Tk()
root.title('Login Page')
root.geometry('600x600')
root.config(bg='purple')
title1 = Label(root,text='Sign in',font=('Arial',70),fg='White',bg='purple').pack()
username = Entry(root,width=20,font=('Arial',20))
password = Entry(root,width=20,font=('Arial',20))
username.pack(padx=50,pady=50)
password.pack(padx=50,pady=50)
def checkpass():
    user = username.get()
    paswd = password.get()
    deuser = ('Admin','admin','user')
    depass = ['Admin','admin','123']
    if user not in depass:
        messagebox.showinfo('information','username does not exist ')
    elif paswd not in  depass:
        messagebox.showinfo('information','Password wrong ')
    else:
        messagebox.showinfo('information','Login successfull ')
but = Button(root,text='Sign in',font=('Arial',20),bg='purple',fg='white',command=checkpass).pack(padx=60,pady=60)




root.mainloop()
