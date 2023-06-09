from tkinter import *
import os
import mysql.connector

root = Tk()
root.title("Provide Comments")
root.geometry('500x440')
root.configure(bg="#DAF5FF")


mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='asusrog',
    database='home_rental'
)

myc = mydb.cursor()

def back():
    root.destroy()
    os.system("python main.py")

def func_root():
    sql = "INSERT INTO comments VALUES (%s, %s, %s, %s, %s)"
    val = (
    client_no_entry.get(),
    property_number_entry.get(),
    name_entry.get(),
    date_entry.get(),
    feedback_entry.get()

)
    myc.execute(sql,val)
    mydb.commit()
    root.destroy()
    os.system("python view_comments.py")

def views():
    root.destroy()
    os.system("python view_comments.py")

prop_register_head_label = Label(root, text="Comments Form", font=("Arial", 20, "bold"), bg="#DAF5FF", fg="#576CBC")
prop_register_head_label.place(x=120, y=15)

client_no_label=Label(root, text="Client Number", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=80)
property_number_label=Label(root, text="Property Number", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=120)
name_label=Label(root, text="Name", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=160)
date_label=Label(root, text="Date", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=200)
feedback_label=Label(root, text="Comment", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=240)

client_no_entry=Entry(root, width=30)
client_no_entry.place(x=190, y=82)

property_number_entry=Entry(root, width=30)
property_number_entry.place(x=190, y=122)

name_entry=Entry(root, width=30)
name_entry.place(x=190, y=162)

date_entry=Entry(root, width=30)
date_entry.place(x=190, y=202)

feedback_entry=Entry(root, width=30)
feedback_entry.place(x=190, y=242)

submit_but=Button(root, text="Submit", width=10, bg="#3E54AC", fg="white",font=("Arial", 12), command=func_root).place(x=42, y=365)
back=Button(root, text="Back", width=10, bg="#595260", fg="white",font=("Arial", 12), command=back).place(x=180, y=365)

view_but=Button(root, text="View Comments", width=15, bg="#3E54AC", fg="white",font=("Arial", 12), command=views).place(x=40, y=305)

root.mainloop()