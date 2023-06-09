from tkinter import *
import os

root = Tk()
root.title("Staff Onboarding")
root.geometry('850x495')
root.configure(bg="#DAF5FF")

import mysql.connector
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
    staff_number = staff_number_entry.get()
    full_name = full_name_entry.get()
    sex = sex_entry.get()
    dob = dob_entry.get()
    position = position_entry.get()
    salary = salary_entry.get()
    branch_number = branch_number_entry.get()
    # branch_address = branch_address_entry.get()
    # telephone_number_staff = telephone_number_entry.get()
    supervisor_name = supervisor_name_entry.get()
    manager_start = manager_start_entry.get()
    manager_bonus = manager_bonus_entry.get()
    sql = "INSERT INTO staff VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    val = (staff_number, full_name, sex, dob, position, salary, branch_number, supervisor_name, manager_start, manager_bonus)
    myc.execute(sql,val)
    mydb.commit()

    root.destroy()
    os.system("python main.py")
    
staff_onboarding_head_label = Label(root, text="Staff Onboarding Form", font=("Arial", 20, "bold"), bg="#DAF5FF", fg="#576CBC")
staff_onboarding_head_label.place(x=255, y=15)

staff_number_label=Label(root, text="Staff Number", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=80)
full_name_label=Label(root, text="Full Name", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=120)
sex_label=Label(root, text="Sex", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=160)
dob_label=Label(root, text="DOB", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=165, y=160)

position_label=Label(root, text="Position", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=220)
salary_label=Label(root, text="salary", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=260)

enter_details_label=Label(root, text="Enter details where applicable",bg="#DAF5FF", fg="#394867",font=("Arial", 14)).place(x=40, y=320)
supervisor_name_label=Label(root, text="Supervisor Name", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=40, y=365)
manager_start_date_label=Label(root, text="Start Date", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=485, y=325)
manager_bonus_label=Label(root, text="Bonus", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=508, y=365)

branch_number_label=Label(root, text="Branch Number", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=430, y=80)
branch_address_label=Label(root, text="Branch Address", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=430, y=120)
telephone_number_label=Label(root, text="Telephone Number", bg="#DAF5FF", fg="#394867",font=("Arial", 13)).place(x=430, y=160)

staff_number_entry = Entry(root, width=30)
staff_number_entry.place(x=160, y=82)

full_name_entry = Entry(root, width=30)
full_name_entry.place(x=160, y=122)

sex_entry = Entry(root, width=3)
sex_entry.place(x=80, y=162)

dob_entry = Entry(root, width=20)
dob_entry.place(x=220, y=162)

position_entry = Entry(root, width=30)
position_entry.place(x=160, y=222)

salary_entry = Entry(root, width=30)
salary_entry.place(x=160, y=262)
# branch_address_entry = Entry(root, width=60)
# branch_address_entry.place(x=190, y=352)

# telephone_number_entry = Entry(root, width=60)
# telephone_number_entry.place(x=190, y=392)

branch_number_entry = Entry(root, width=30)
branch_number_entry.place(x=595, y=82)

branch_address_entry = Entry(root, width=30)
branch_address_entry.place(x=595, y=122)

telephone_number_entry = Entry(root, width=30)
telephone_number_entry.place(x=595, y=162)

supervisor_name_entry = Entry(root, width=25)
supervisor_name_entry.place(x=190, y=368)

manager_start_entry = Entry(root, width=30)
manager_start_entry.place(x=594, y=327)

manager_bonus_entry = Entry(root, width=30)
manager_bonus_entry.place(x=594, y=367)


submit_but=Button(root, text="Submit", width=10, bg="#3E54AC", fg="white",font=("Arial", 12), command=func_root).place(x=41, y=425)
back=Button(root, text="Back", width=10, bg="#595260", fg="white",font=("Arial", 12), command=back).place(x=677, y=425)

root.mainloop()