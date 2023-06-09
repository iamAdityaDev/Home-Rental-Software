from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import mysql.connector

root = Tk()
root.title("Provide Comments")
root.geometry('1100x440')
root.configure(bg="#DAF5FF")

mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='asusrog',
    database='home_rental'
)

myc = mydb.cursor()

# Fetch data from the comments table
myc.execute('SELECT * FROM comments')
rows = myc.fetchall()

comment_head_label = Label(root, text="View Comments", font=("Arial", 20, "bold"), bg="#DAF5FF", fg="#576CBC")
comment_head_label.place(x=420, y=15)

# Create the ttk.Treeview widget
table = ttk.Treeview(root, columns=('Client Number', 'Property Number', 'Name', 'Date', 'Comment'), show='headings')
table.heading('Client Number', text='Client Number')
table.heading('Property Number', text='Property Number')
table.heading('Name', text='Name')
table.heading('Date', text='Date')
table.heading('Comment', text='Comment')

# Insert each row of data into the ttk.Treeview widget
for row in rows:
    table.insert('', 'end', values=row)

table.place(x=45, y=100)

def back():
    root.destroy()
    os.system("python provide_comments.py")

back=Button(root, text="Back", width=10, bg="#595260", fg="white",font=("Arial", 12), command=back).place(x=480, y=380)

root.mainloop()
