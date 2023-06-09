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

root = Tk()
root.title("View Listed Properties")
root.geometry('700x520')
root.configure(bg="#DAF5FF")

def back():
    root.destroy()
    os.system("python main.py")

def populate_table():
    myc = mydb.cursor()
    branch_no = branch_no_entry.get()

    sql = "SELECT * FROM STAFF WHERE branch_number = %s"
    val = (branch_no,)
    myc.execute(sql, val)
    result = myc.fetchall()
    for row in result:
        table.insert('', 'end', values=row)
    mydb.commit()


Staff_list_head_label = Label(root, text="Staff List", font=("Arial", 20, "bold"), bg="#DAF5FF", fg="#576CBC")
Staff_list_head_label.place(x=295, y=20)

branch_no_label = Label(root, text="Branch No",bg="#DAF5FF", fg="#394867",font=("Arial", 13))
branch_no_label.place(x=45, y=80)

branch_no_entry = Entry(root, width=30)
branch_no_entry.place(x=145, y=82)

table = ttk.Treeview(root, columns=('Staff Number', 'Name', 'Position'), show='headings')
table.heading('Staff Number', text='Staff Number')
table.heading('Name', text='Name')
table.heading('Position', text='Position')

table.place(x=45, y=200)

submit_but = Button(root, text="Submit", width=10, bg="#3E54AC", fg="white",font=("Arial", 12), command=populate_table)
submit_but.place(x=47, y=130)
back=Button(root, text="Back", width=10, bg="#595260", fg="white",font=("Arial", 12), command=back).place(x=305, y=450)

root.mainloop()