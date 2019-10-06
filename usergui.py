import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import datetime


mydb=mysql.connector.connect(host="localhost",user="root",passwd="",
                             database="sagar")
mycursor=mydb.cursor()                             

win=tk.Tk()
win.title('Book Ticket')

heading=ttk.Label(win,text="Book your ticket here...")
heading.grid(row=0,column=1)

name_label=ttk.Label(win,text="Enter your name ")
name_label.grid(row=1,column=0,sticky=tk.W)

name=tk.StringVar()
name_box=ttk.Entry(win,width=16,textvariable=name)
name_box.grid(row=1,column=1)
name_box.focus()

age_label=ttk.Label(win,text="Enter your age : ")
age_label.grid(row=2,column=0,sticky=tk.W)

age=tk.StringVar()
age_box=ttk.Entry(win,width=16,textvariable=age)
age_box.grid(row=2,column=1)
age_box.focus()


gender_label=ttk.Label(win,text="Select your gender: ")
gender_label.grid(row=3,column=0,sticky=tk.W)

gender=tk.StringVar()
gender_box=ttk.Combobox(win,width=16,textvariable=gender,state='readonly')
gender_box['values']=('Male','Female','Other')
gender_box.current(0)
gender_box.grid(row=3,column=1)
gender_box.focus()

address_label=ttk.Label(win,text="Enter your address: ")
address_label.grid(row=4,column=0,sticky=tk.W)

address=tk.StringVar()
address_box=ttk.Entry(win,width=16,textvariable=address)
address_box.grid(row=4,column=1)
address_box.focus()

no_label=ttk.Label(win,text="Enter your train number : ")
no_label.grid(row=5,column=0,sticky=tk.W)

no=tk.StringVar()
no_box=ttk.Entry(win,width=16,textvariable=no)
no_box.grid(row=5,column=1)
no_box.focus()

def action():
    name1=name.get()
    age1=age.get()
    gender1=gender.get()
    address1=address.get()
    no1=no.get()
    mycursor.execute("SELECT * FROM train_status where Number="+no1)
    temp3 =mycursor.fetchall()
    seat=temp3[0][1]
    seat=seat-1
    booking=1
    print(seat,no1)
    sql="update train_status set Seats=%s where Number=%s"
    val=(seat,no1)  
    mycursor.execute(sql,val)
    mydb.commit()  
    print(name1,age1,gender1,address1,no1)

    now = datetime.date(2019,5,3)
    sql = "INSERT INTO passenger(name,age,sex,address,date,train_no,status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val=  (name1,age1,gender1,address1,now,no1,"confirmed")
    mycursor.execute(sql,val)
    mydb.commit() 

    mycursor.execute("SELECT * FROM passenger where train_no="+no1)
    temp4 =mycursor.fetchall()
    mydb.commit() 
    win.withdraw()
    messagebox.showinfo("Status", "Congrats!Booking Confirmed\nYour booking id is : "+str(temp4[0][6]))
    win.deiconify()
     
    
    

submit_button=ttk.Button(win,text="Book",command=action)
submit_button.grid(row=6,column=0)

win.mainloop()