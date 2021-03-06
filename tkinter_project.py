from tkinter import *
import sqlite3


root=Tk()

root.geometry('1500x1500')

root.title("Registeration Form")


l0=Label(root,text="Hello! Welcome to Space",width=30,bg="black",fg="silver",font=("Verdana 40 bold italic"))
l0.place(x=200,y=100)
l1=Label(root,text="Are you ready to enter the Magical World of Constellations? Come on!\n\n LETS GET STARTED\n",font=("Verdana 20 bold"))
l1.place(x=180,y=200)

FullName=StringVar()
Email=StringVar()
Age=StringVar()
var=StringVar()
c=StringVar()
var2=StringVar()

def database():
    name1=FullName.get()
    email=Email.get()
    age=Age.get()
    gender=var.get()
    city=c.get()
    guide=var2.get()
    conn=sqlite3.connect('Form1.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Detail (Fullname TEXT,Email TEXT,Age TEXT,Gender TEXT,City TEXT,Guide TEXT)')
    cursor.execute('insert into Detail (Fullname,Email,Age,Gender,City,Guide) values (?,?,?,?,?,?)',(name1,email,age,gender,city,guide,))
    conn.commit()


l2=Label(root,text="Full Name",font=("Verdana 20"))
l2.place(x=400,y=300)

e2=Entry(root,width=40,textvar=FullName)
e2.place(x=700,y=312)

l3=Label(root,text="Email",font=("Verdana 20"))
l3.place(x=400,y=360)

e3=Entry(root,width=40,textvar=Email)
e3.place(x=700,y=370)

l4=Label(root,text="Age",font=("Verdana 20"))
l4.place(x=400,y=415)

e4=Entry(root,width=15,textvar=Age)
e4.place(x=700,y=425)

l5=Label(root,text="Gender",font=("Verdana 20"))
l5.place(x=400,y=470)

var=StringVar()
Radiobutton(root,text="Male",padx=5, variable=var,value="male",font=("Verdana 13")).place(x=692,y=480)
Radiobutton(root,text="Female",variable=var,value="female",font=("Verdana 13")).place(x=791,y=480)
Radiobutton(root,text="Other",padx=20,variable=var,value="other",font="Verdana 13").place(x=887,y=480)

l6=Label(root,text="Your City",font=("Verdana 20"))
l6.place(x=400,y=525)
li1=['Chandigarh','Panchkula','Mohali','Zirakpur']
c=StringVar()
droplist=OptionMenu(root,c,*li1)
droplist.config(width=15,activebackground="light blue",font=("Verdana 11"))
c.set('Select your city')
droplist.place(x=700,y=530)

l7=Label(root,text="A guide required?",font=("Verdana 19"))
l7.place(x=400,y=580)

var2=IntVar()
Radiobutton(root,text="Yes",variable=var2,value="yes",font=("Verdana 13")).place(x=700,y=585)
Radiobutton(root,text="No",variable=var2,value="no",font=("Verdana 13")).place(x=780,y=585)

Button(root,text="Submit and go to the Payment Page",font=("Verdana 18"),fg='light pink',bg='black',command=database).place(x=480,y=670)


mainloop()
