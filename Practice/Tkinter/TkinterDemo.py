from tkinter import *

import mysql.connector
import tkinter.messagebox as msg


# connect -> process -> close
# compulsory the connection should be close
def create_conn():
    return mysql.connector.connect (
                host="localhost",
                user="root",
                password="",
                database="register_form_python"
            )
print(create_conn())


#Functions for buttons

#insert
def insert_data():
    #print("Insert Data Button Clicked")
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fileds Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()# helps to execute the query on sql / compulsory to write this else the databse not conncted with the app
        query="insert into student_data(fname,lname,email,mobile) values(%s,%s,%s,%s)" #sequence is important
        args=(e_fname.get() , e_lname.get() , e_email.get() , e_mobile.get())
        cursor.execute(query,args) # wherever there is a changes then commit the chnges and then compulsory close the connection
        conn.commit()
        conn.close()        
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo('Insert Status ','Data Inserted !!')

#search
def search_data():
    if e_id.get()=="":
        msg.showinfo("Search Status","ID is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()# helps to execute the query on sql / compulsory to write this else the databse not conncted with the app
        query="select * from student_data where id= %s" #sequence is important
        args=(e_id.get() ,)
        cursor.execute(query,args) # wherever there is a changes then commit the chnges and then compulsory close the connection
        #conn.commit()
        row=cursor.fetchall()
        if row:
            e_fname.insert(0,row[0][1])
            e_lname.insert(0,row[0][2])
            e_email.insert(0,row[0][3])
            e_mobile.insert(0,row[0][4])
        else:
            msg.showinfo("Search Status", "Id not Found")
        #print(row)        
        conn.close()

        #update
def update_data():
    #print("Update Data Button Clicked")
    if e_id.get()== "" or e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Update Status","All Fileds Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()# helps to execute the query on sql / compulsory to write this else the databse not conncted with the app
        query="UPDATE student_data SET fname=%s, lname=%s, email=%s, mobile=%s WHERE id =%s " #sequence is important
        args=(e_fname.get() , e_lname.get() , e_email.get() , e_mobile.get(),e_id.get())
        cursor.execute(query,args) # wherever there is a changes then commit the chnges and then compulsory close the connection
        conn.commit()
        conn.close() 
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo('Update Status ','Data Updated  !!')

#delete
def delete_data():
    if e_id.get()== "" :
        msg.showinfo("Delete Status","ID is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()# helps to execute the query on sql / compulsory to write this else the databse not conncted with the app
        query="delete from student_data WHERE id =%s " #sequence is important
        args=(e_id.get(),)
        cursor.execute(query,args) # wherever there is a changes then commit the chnges and then compulsory close the connection
        conn.commit()
        conn.close() 
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo('Delete Status ','Data deleted  !!')



#size of form app
root=Tk()
root.geometry("325x350")
root.title("My Tkinter Examples")
root.resizable(width=False,height=False)

#Register form

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

#Buttons

insert=Button(root ,text="Insert",bg="black",fg="white",font=("Arial",12),command=insert_data)
insert.place(x=10,y=300)

search=Button(root ,text="Search",bg="black",fg="white",font=("Arial",12),command=search_data)
search.place(x=80,y=300)

update=Button(root ,text="Update",bg="black",fg="white",font=("Arial",12),command=update_data)
update.place(x=160,y=300)

delete=Button(root ,text="Delete",bg="black",fg="white",font=("Arial",12),command=delete_data)
delete.place(x=240,y=300)
