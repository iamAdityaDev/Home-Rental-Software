from tkinter import *
import os
import mysql.connector

root = Tk()
root.title("Property Registration")
root.geometry('873x440')
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
    sql = "INSERT INTO PROP_REGISTRATION VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (
    property_number_entry.get(),
    type_entry.get(),
    rooms_entry.get(),
    rent_entry.get(),
    address_entry.get(),
    owner_number_entry.get(),
    person_business_name_entry.get(),
    person_business_address_entry.get(),
    telephone_number_entry.get(),
    type_of_business_entry.get(),
    managed_by_staff_entry.get(),
    registered_branch_entry.get(),
    city_entry.get(),
)
    myc.execute(sql,val)
    mydb.commit()
    root.destroy()
    os.system("python main.py")

prop_register_head_label = Label(root, text="Property Registration Form", font=("Arial", 20, "bold"), bg="#DAF5FF", fg="#576CBC")
prop_register_head_label.place(x=245, y=15)


property_number_label=Label(root, text="Property Number", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=80)
type_label=Label(root, text="Type", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=120)
rooms_label=Label(root, text="Rooms", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=240, y=120)
rent_label=Label(root, text="Rent", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=160)
address_label=Label(root, text="Address", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=200)

owner_number_label=Label(root, text="Owner Number", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=430, y=80)
person_business_name_label=Label(root, text="Person/Business Name", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=430, y=120)
person_business_address_label=Label(root, text="Person/Business Address", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=430, y=160)
telephone_number_label=Label(root, text="Telephone Number", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=430, y=200)

# enter_details_label=Label(root, text="Enter details where applicable",font=("Arial", 11)).place(x=50, y=390)

type_of_business_label=Label(root, text="Type of Business", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=430, y=270)
managed_by_staff_label=Label(root, text="Managed By Staff", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=430, y=310)

registered_branch_label=Label(root, text="Registered Branch No", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=270)
city_label=Label(root, text="City", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=310)


property_number_entry=Entry(root, width=30)
property_number_entry.place(x=190, y=82)

type_entry=Entry(root, width=15)
type_entry.place(x=120, y=123)

rooms_entry=Entry(root, width=10)
rooms_entry.place(x=310, y=123)

rent_entry=Entry(root, width=15)
rent_entry.place(x=120, y=162)

address_entry=Entry(root, width=41)
address_entry.place(x=120, y=202)

owner_number_entry=Entry(root, width=30)
owner_number_entry.place(x=635, y=82)

person_business_name_entry=Entry(root, width=30)
person_business_name_entry.place(x=635, y=122)

person_business_address_entry=Entry(root, width=30)
person_business_address_entry.place(x=635, y=162)

telephone_number_entry=Entry(root, width=30)
telephone_number_entry.place(x=635, y=202)

type_of_business_entry=Entry(root, width=35)
type_of_business_entry.place(x=605, y=272)

managed_by_staff_entry=Entry(root, width=35)
managed_by_staff_entry.place(x=605, y=312)

registered_branch_entry=Entry(root, width=24)
registered_branch_entry.place(x=220, y=272)

city_entry=Entry(root, width=24)
city_entry.place(x=220, y=312)

submit_but=Button(root, text="Submit", width=10, bg="#3E54AC", fg="white",font=("Arial", 12), command=func_root).place(x=42, y=365)
back=Button(root, text="Back", width=10, bg="#595260", fg="white",font=("Arial", 12), command=back).place(x=720, y=365)


root.mainloop()