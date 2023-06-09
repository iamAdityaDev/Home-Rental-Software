from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import mysql.connector
mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='asusrog',
    database='home_rental'
)

def back():
    root.destroy()
    os.system("python main.py")

def populate_table():
    myc = mydb.cursor()
    branch_no = branch_no_entry.get()

    sql = "SELECT client_no,name,registered_by,date_registered,type,max_rent FROM CLIENT_REGISTRATION WHERE branch_no = %s"
    val = (branch_no,)
    myc.execute(sql, val)
    result = myc.fetchall()
    for row in result:
        table.insert('', 'end', values=row)
    
    mydb.commit()

root = Tk()
root.title("View Listed Properties")
root.geometry('1290x520')
root.configure(bg="#DAF5FF")

view_client_label = Label(root, text="Client List", font=("Arial", 20, "bold"), bg="#DAF5FF", fg="#576CBC")
view_client_label.place(x=530, y=20)


branch_no_label = Label(root, text="Branch No",bg="#DAF5FF", fg="#394867",font=("Arial", 13))
branch_no_label.place(x=45, y=80)

branch_no_entry = Entry(root, width=30)
branch_no_entry.place(x=145, y=82)

table = ttk.Treeview(root, columns=('Client Number', 'Full Name', 'Registered By', 'Date Registered','Property Type', 'Max Rent'), show='headings')
table.heading('Client Number', text='Client Number')
table.heading('Full Name', text='Full Name')
table.heading('Registered By', text='Registered By')
table.heading('Date Registered', text='Date Registered')
table.heading('Property Type', text='Property Type')
table.heading('Max Rent', text='Max Rent')

table.place(x=45, y=200)

submit_but = Button(root, text="Submit", width=10, bg="#3E54AC", fg="white",font=("Arial", 12), command=populate_table)
submit_but.place(x=47, y=130)
back=Button(root, text="Back", width=10, bg="#595260", fg="white",font=("Arial", 12), command=back).place(x=550, y=450)

root.mainloop()
