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
root.title("Lease Form")
root.geometry('810x450')
root.configure(bg="#DAF5FF")

def back():
    root.destroy()
    os.system("python main.py")

def func_root():
    client_number = client_number_entry.get()
    full_name = full_name_entry.get()
    monthly_rent = monthly_rent_entry.get()
    payment_method = payment_method_entry.get()
    deposit_paid = deposit_paid_entry.get()
    property_number = property_number_entry.get()
    # property_address = property_address_entry.get()
    rent_start = rent_start_entry.get()
    rent_finish = rent_finish_entry.get()
    duration = duration_entry.get()

    sql = "INSERT INTO lease_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (client_number,full_name,monthly_rent,payment_method,deposit_paid,property_number,rent_start,rent_finish,duration)

    sql2 = "DELETE FROM prop_registration WHERE p_no = %s"
    val2 = (property_number,)

    myc.execute(sql, val)
    mydb.commit()
    myc.execute(sql2,val2)
    mydb.commit()

    root.destroy()
    os.system("python main.py")

lease_form_head_label = Label(root, text="Lease Form", font=("Arial", 20, "bold"), bg="#DAF5FF", fg="#576CBC")
lease_form_head_label.place(x=310, y=15)

client_number_label=Label(root, text="Client Number", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=80)
full_name_label=Label(root, text="Full Name", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=120)

payment_details_label=Label(root, text="Enter payment details", bg="#DAF5FF", fg="#394867",font=("Arial", 14)).place(x=40, y=180)
monthly_rent_label=Label(root, text="Monthly Rent", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=230)
payment_method_label=Label(root, text="Payment Method", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=270)
deposit_paid_label=Label(root, text="Deposit Paid (Y or N)", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=310)

property_number_label=Label(root, text="Property Number", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=425, y=80)
property_address_label=Label(root, text="Property Address", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=425, y=120)
rent_start_label=Label(root, text="Rent Start", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=455, y=230)
rent_finish_label=Label(root, text="Rent Finish", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=455, y=270)
duration_label=Label(root, text="Duration", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=455, y=310)

client_number_entry = Entry(root, width=30)
client_number_entry.place(x=165, y=82)

full_name_entry = Entry(root, width=30)
full_name_entry.place(x=165, y=122)

monthly_rent_entry = Entry(root, width=25)
monthly_rent_entry.place(x=190, y=232)

payment_method_entry = Entry(root, width=25)
payment_method_entry.place(x=190, y=272)

deposit_paid_entry = Entry(root, width=3)
deposit_paid_entry.place(x=215, y=312)

property_number_entry = Entry(root, width=30)
property_number_entry.place(x=575, y=82)

property_address_entry = Entry(root, width=30)
property_address_entry.place(x=575, y=122)
# property_address_entry = Entry(root, width=50)
# property_address_entry.place(x=235, y=362)

rent_start_entry = Entry(root, width=30)
rent_start_entry.place(x=575, y=232)

rent_finish_entry = Entry(root, width=30)
rent_finish_entry.place(x=575, y=272)

duration_entry = Entry(root, width=30)
duration_entry.place(x=575, y=312)

submit_but=Button(root, text="Submit", width=10, bg="#3E54AC", fg="white",font=("Arial", 12), command=func_root).place(x=41, y=370)
back=Button(root, text="Back", width=10, bg="#595260", fg="white",font=("Arial", 12), command=back).place(x=660, y=370)

root.mainloop()