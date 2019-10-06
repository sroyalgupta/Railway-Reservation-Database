import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import datetime
from subprocess import call

# root = tk.Tk()
# root.withdraw()
# messagebox.showinfo("Title", "a Tk MessageBox")

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",
                             database="sagar")
mycursor=mydb.cursor()                             

win=tk.Tk()
win.title('Railway REservation')
check_label=ttk.Label(win,text="Enter your booking id ")
check_label.grid(row=1,column=0,sticky=tk.W)

check=tk.StringVar()
check_box=ttk.Entry(win,width=16,textvariable=check)
check_box.grid(row=1,column=1)
check_box.focus()

def action():
    check1=check.get()
    print(type(check1))

    mycursor.execute('select * from passenger where user_id='+check1)
    temp=mycursor.fetchall()
    print(temp)
    temp1=temp[0][5]
    print(temp1)

    mycursor.execute("delete from passenger where user_id="+check1)
    mydb.commit()
    

    
    
    mycursor.execute('select * from train_status where Number='+str(temp1))
    temp2=mycursor.fetchall()
    temp3=temp2[0][1]
    temp3=temp3+1

    sql="update train_status set Seats=%s where Number=%s"
    val=(temp3,temp1)
    mycursor.execute(sql,val)
    mydb.commit()

    win.withdraw()
    messagebox.showinfo("Result", "your ticket has been cancelled....")
    win.deiconify()

submit_button=ttk.Button(win,text="Cancel",command=action)
submit_button.grid(row=2,column=0)

win.mainloop()