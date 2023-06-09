from tkinter import *
import os
import mysql.connector
mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='asusrog',
    database='home_rental'
)

myc = mydb.cursor()

root = Tk()
root.title("Client Registration")
root.geometry('770x430')

window = Canvas(root, width=770, height=430, bg="#DAF5FF")
window.pack()

def back():
    root.destroy()
    os.system("python main.py")

def func_window():
    client_number = client_number_entry.get()
    full_name = full_name_entry.get()
    property_type = type_entry.get()
    max_rent = max_rent_entry.get()
    branch_number = brach_number_entry.get()
    branch_address = branch_address_entry.get()
    registered_by = registered_by_entry.get()
    date_registered = date_registered_entry.get()

    sql = "INSERT INTO CLIENT_REGISTRATION VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (client_number, full_name, property_type, max_rent, branch_number, branch_address, registered_by, date_registered)
    myc.execute(sql, val)
    mydb.commit()
    root.destroy()
    os.system("python main.py")


client_registration_heading_label = Label(window, text="Client Registration Form", font=("Arial", 20, "bold"), bg="#DAF5FF", fg="#576CBC")
client_registration_heading_label.place(x=220, y=30)

client_number_label=Label(window, text="Client Number", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=100)
full_name_label=Label(window, text="Full Name", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=140)
property_requirements_label=Label(window, text="Enter Property Requirements", bg="#DAF5FF", fg="#394867",font=("Arial", 14)).place(x=40, y=195)
type_label=Label(window, text="Type", bg="#DAF5FF", fg="#394867",font=("Arial", 12)).place(x=40, y=250)
max_rent_label=Label(window, text="Max Rent", bg="#DAF5FF", fg="#394867",font=("Arial", 12)).place(x=40, y=290)
branch_number_label=Label(window, text="Branch Number", bg="#DAF5FF", fg="#394867",font=("Arial", 12)).place(x=390, y=100)
branch_address_label=Label(window, text="Branch Address", bg="#DAF5FF", fg="#394867",font=("Arial", 12)).place(x=390, y=140)
registered_by_label=Label(window, text="Registered By", bg="#DAF5FF", fg="#394867",font=("Arial", 12)).place(x=390, y=250)
date_registered_label=Label(window, text="Date Registered", bg="#DAF5FF", fg="#394867",font=("Arial", 12)).place(x=390, y=290)

client_number_entry = Entry(window, width=30)
client_number_entry.place(x=160, y=102)

full_name_entry = Entry(window, width=30)
full_name_entry.place(x=160, y=142)

type_entry = Entry(window, width=30)
type_entry.place(x=140, y=252)

max_rent_entry = Entry(window, width=30)
max_rent_entry.place(x=140, y=292)

brach_number_entry = Entry(window, width=30)
brach_number_entry.place(x=520, y=102)

branch_address_entry = Entry(window, width=30)
branch_address_entry.place(x=520, y=142)

registered_by_entry = Entry(window, width=27)
registered_by_entry.place(x=530, y=252)

date_registered_entry = Entry(window, width=27)
date_registered_entry.place(x=530, y=292)


submit_but=Button(window, text="Submit", width=12,height=1, bg="#3E54AC", fg="white",font=("Arial", 12), command=func_window).place(x=40, y=352)
back=Button(window, text="Back", width=9, bg="#595260", fg="white",font=("Arial", 12), command=back).place(x=603, y=352)
window.mainloop()