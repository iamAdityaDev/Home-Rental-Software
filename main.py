from tkinter import *
import tkinter as tk
import os

root = tk.Tk()
root.title("Home")
root.geometry('720x460')
root.configure(bg="#DAF5FF")

def redirect_client_registration():
    root.destroy()
    os.system("python client_registration.py")


def redirect_property_registration():
    root.destroy()
    os.system("python property_registration.py")


def redirect_view_listed_properties():
    root.destroy()
    import view_listed_properties


def redirect_provide_comments():
    root.destroy()
    os.system("python provide_comments.py")


def redirect_staff_onboarding():
    root.destroy()
    os.system("python staff_onboarding.py")


def redirect_lease_form():
    root.destroy()
    os.system("python lease_form.py")

def view_client():
    root.destroy()
    import client_list

def view_staff():
    root.destroy()
    import staff_list



image = PhotoImage(file="final_logo.png")
resized_image = image.subsample(4)
image_label = Label(root, image=resized_image)
image_label.place(x=265, y=15)


staff_label=Label(root, text="Staff Section", bg="#DAF5FF", fg="#394867",font=("Arial", 14)).place(x=50, y=170)
client_label=Label(root, text="Client Section", bg="#DAF5FF", fg="#394867",font=("Arial", 14)).place(x=270, y=170)
owner_label=Label(root, text="Owner Section", bg="#DAF5FF", fg="#394867",font=("Arial", 14)).place(x=490, y=170)

client_registration = tk.Button(root, text="Client Registration",
                             bg="#3E54AC", fg="white", height="2", width=19,font=("Arial", 12), command=redirect_client_registration).place(x=270, y=210)

view_listed_properties = tk.Button(root, text="View Listed Properties",
                                bg="#3E54AC", fg="white", height="2", width=19,font=("Arial", 12), command=redirect_view_listed_properties).place(x=270, y=280)

provide_comments = tk.Button(root, text="Provide Comments", bg="#3E54AC",
                          fg="white", height="2", width=19,font=("Arial", 12), command=redirect_provide_comments).place(x=270, y=350)

staff_onboarding = tk.Button(root, text="Staff Onboarding", bg="#3E54AC",
                          fg="white", height="2", width=19,font=("Arial", 12), command=redirect_staff_onboarding).place(x=50, y=210)

View_staff = tk.Button(root, text="View Staff", bg="#3E54AC",
                          fg="white", height="2", width=19,font=("Arial", 12), command=view_staff).place(x=50, y=280)

lease_form =tk.Button(root, text="Lease Form", bg="#3E54AC",
                    fg="white", height="2", width=19,font=("Arial", 12), command=redirect_lease_form).place(x=50, y=350)

property_registration = tk.Button(root, text="Property Registration",
                               bg="#3E54AC", fg="white", height="2", width=19,font=("Arial", 12), command=redirect_property_registration).place(x=490, y=210)

View_client = tk.Button(root, text="View Client", bg="#3E54AC",
                          fg="white", height="2", width=19,font=("Arial", 12), command=view_client).place(x=490, y=280)


root.mainloop()
