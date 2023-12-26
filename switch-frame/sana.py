from tkinter import *
from tkinter import messagebox
root = Tk()

root.title("<login from>")
root.geometry("500x500")
root.configure(bg="#333333")
root.resizable(False,False)

first_frame = Frame(root)
first_frame.place(x=0, y=0, width=500, height=500)

second_frame = Frame(root)
second_frame.place(x=0, y=0, width=500, height=500)
 


name = "sana"
passpord = 12345
def toplevel(frame):
    print("yes")
    frame.tkraise()
    # print(txtnum1.get())
    # print(txtnum2.get())
    # if txtnum1.get() == "":
    #     messagebox.showwarning("empty", "username is empty")
    # elif len(txtnum2.get()) < 5:
    #     messagebox.showwarning("password len", "password len must bigger than 4") 
    # else:       
        
    
        
#---------------------- Frame One --------------------------------------------------------------- 
labelwelcome = Label(first_frame,text="Login",fg="red",bg="#333333",font=("Microsoft Yahei UI Light",25),)
labelwelcome.place(x=210,y=50)

labelnum1 = Label(first_frame,text="username :",bg="#333333",fg="red",font=15)
labelnum1.place(x=30,y=150)


labelnum2 = Label(first_frame,text="password :",bg="#333333",fg="red",font=15)
labelnum2.place(x=30,y=235)

usernameTextVar = StringVar()
txtnum1 = Entry(first_frame,textvariable=usernameTextVar,bg="white",font=("Microsoft Yahei UI Light",10),fg="black")

txtnum1.place(x=120,y=150,width=300)
passwordTextVar = StringVar()

txtnum2 = Entry(first_frame,textvariable=passwordTextVar,bg="white",font=("Microsoft Yahei UI Light",10),fg="black")
txtnum2.place(x=120,y=235,width=300)

btn = Button(second_frame,bg="red",fg="white",text="Login",font=("Microsoft Yahei UI Light",15),command=lambda:toplevel(second_frame))
btn.place(x=215,y=350)


#---------------------- Frame Second --------------------------------------------------------------- 

label1 = Label(second_frame,text="MORTAL KOMBAT",font=("Microsoft Yahei UI Light",13))
label1.place(x=50,y=150)

label2 = Label(second_frame,text="CRASH BANDKOT",font=("Microsoft Yahei UI Light",13))
label2.place(x=300,y=150)

label3 = Label(second_frame,text="THE WAR OF TANK",font=("Microsoft Yahei UI Light",13))
label3.place(x=50,y=300)

label4 = Label(second_frame,text="BATMAN ARKAM N",font=("Microsoft Yahei UI Light",13))
label4.place(x=300,y=300)

label5 = Label(second_frame,text="WELCOME",font=("Microsoft Yahei UI Light",20),fg="#12345f",bg="#f78346")
label5.place(x=175,y=60)


root.mainloop()