from tkinter import *

root=Tk()
root.geometry("325x350")
root.title("My Tkinter Examples")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID",font=("Arial",11))
l_id.place(x=50,y=50)

e_id=Entry(root)
e_id.place(x=150,y=50)

l_fname=Label(root,text="First Name",font=("Arial",11))
l_fname.place(x=50,y=100)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

l_lname=Label(root,text="Last Name",font=("Arial",11))
l_lname.place(x=50,y=150)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

l_email=Label(root,text="Email",font=("Arial",11))
l_email.place(x=50,y=200)

e_email=Entry(root)
e_email.place(x=150,y=200)

l_mobile=Label(root,text="Mobile",font=("Arial",11))
l_mobile.place(x=50,y=250)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

def insert_data():
    print("Insert Data Button Clicked")

insert=Button(root ,text="Insert",bg="black",fg="white",font=("Arial",12),command=insert_data)
insert.place(x=10,y=300)

def search_data():
    print("Search Data Button Clicked")

insert=Button(root ,text="Search",bg="black",fg="white",font=("Arial",12),command=search_data)
insert.place(x=80,y=300)

def update_data():
    print("Update Data Button Clicked")

insert=Button(root ,text="Update",bg="black",fg="white",font=("Arial",12),command=update_data)
insert.place(x=160,y=300)

def delete_data():
    print("Delete Data Button Clicked")

insert=Button(root ,text="Delete",bg="black",fg="white",font=("Arial",12),command=delete_data)
insert.place(x=240,y=300)
