from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import re


def reg_to_login(root):
    root.destroy()
    from login_copy import login_call
    login_call()


def register(root):
    # first name validation
    reg_error=""
    firstname = fn.get()
    if not (firstname.isalpha()):
        firstname = None
        reg_error += "#first name should not contain any special or numeric\n\n"
        fname_entry.delete(0, END)

    # lastname validation
    lastname = ln.get()
    if not lastname.isalpha():
        lastname = None
        reg_error += "#last name should not contain any special or numeric\n\n"
        lname_entry.delete(0, END)

    # email validations
    email = email2.get()
    pattern = "(@gmail.com|@yahoo.com|@outlook.com|@hotmail.com)$"
    if re.search(pattern, email):
        pass
    else:
        email = None
        reg_error += "#invalid mail id\n\n"
        email_entry.delete(0, END)
    # mobile number validations
    mobile_number = mb_no.get()
    pattern = "^[6-9]{1}[0-9]{9}$"
    if re.match(pattern, mobile_number) and len(mobile_number) == 10:
        mobile_number = int(mobile_number)
    else:
        mobile_number = None
        reg_error += "#mobile number is invalid \n\n"
        mb_no_entry.delete(0, END)
    # password validation
    password = passwd.get()
    if password.find(" ") == -1 and len(password) >= 8:
        pass
    else:
        password = None
        reg_error += "#password should be 8 in length\n\n"
        passwrd_entry.delete(0, END)

    # confirm password validation
    confirm_password = cpasswd.get()
    if password == confirm_password:
        pass
    else:
        confirm_password = None
        reg_error += "#confirm password should be match with password\n\n"
        cpasswrd_entry.delete(0, END)

    presence = "select * from registration_copy where mobile=%s or email=%s"
    presence_field = (mobile_number, email)
    user_exist = mycursor.execute(presence, presence_field)
    if (firstname != None) and (lastname != None) and email != None and password != None and confirm_password != None and mobile_number != None:
        if user_exist:
            # redirection to login page
            print("User already exists")
            messagebox.showerror(title="user exists", message=f"{firstname} already existed user. Try login")
            fname_entry.delete(0, END)
            lname_entry.delete(0, END)
            email_entry.delete(0, END)
            passwrd_entry.delete(0, END)
            cpasswrd_entry.delete(0, END)
            mb_no_entry.delete(0, END)
            reg_to_login(root)
        else:
            sql = "insert into registration_copy values (%s,%s,%s,%s,%s)"
            value = (firstname, lastname, password, email, mobile_number)
            mycursor.execute(sql, value)
            mydb.commit()
            print("user added successfully...!!!!!!!!")
            fname_entry.delete(0, END)
            lname_entry.delete(0, END)
            email_entry.delete(0, END)
            passwrd_entry.delete(0, END)
            cpasswrd_entry.delete(0, END)
            mb_no_entry.delete(0, END)
            messagebox.showinfo(title="Success", message=f"{firstname} your account created successfully")
            reg_to_login(root)
    else:
        messagebox.showerror(title="Invalid entries", message=reg_error)
        reg_error = ""


def reg_start(root):

    global mydb, mycursor
    mydb = pymysql.connect(host='localhost', user='root', password='root')
    mycursor = mydb.cursor()
    mycursor.execute('use e_commerce')
    root.geometry("500x600")
    root.state("zoomed")  # For Full screen
    root.title("AMAZON WEB SERVICES")

    global fn, ln, email2, passwd, cpasswd, mb_no, fname_entry, lname_entry, email_entry, passwrd_entry, cpasswrd_entry, mb_no_entry

    fn = StringVar()
    ln = StringVar()
    email2 = StringVar()
    passwd = StringVar()
    cpasswd = StringVar()
    mb_no = StringVar()

    frame = Frame(root, bg='white')  # A rectangular region used to group related widgets
    frame.place(x=600, y=150, width=360, height=500)  #

    reg = Label(frame, text="Create Account", font=("times as roman", 15, "bold"), bg="white")
    reg.place(x=20, y=20)
    back_login = Button(frame, text="Back",  width=5, command=lambda: reg_to_login(root), font=("times of roman ", 12), bd=2, relief="groove",
               fg="black", bg="orange").place(x=300, y=20)

    fname = Label(frame, text="First Name*", font=("times as roman", 12), bg="white")
    fname.place(x=20, y=50)

    fname_entry = ttk.Entry(frame, textvar=fn, width=50)
    fname_entry.place(x=20, y=80)
    lname = Label(frame, text="Last Name*", font=("times as roman", 12), bg="white")
    lname.place(x=20, y=110)

    lname_entry = ttk.Entry(frame, textvar=ln, width=50)
    lname_entry.place(x=20, y=140)

    email = Label(frame, text="Email*", font=("times as roman", 12), bg="white")
    email.place(x=20, y=170)

    email_entry = ttk.Entry(frame, textvar=email2, width=50)
    email_entry.place(x=20, y=200)

    lbl_mb_no = Label(frame, text="Mobile Number*", font=("times as roman", 12), bg="white")
    lbl_mb_no.place(x=20, y=230)

    mb_no_entry = ttk.Entry(frame, textvar=mb_no, width=50)
    mb_no_entry.place(x=20, y=260)

    passwrd = Label(frame, text="Password*", font=("times as roman", 12), bg="white")
    passwrd.place(x=20, y=290)

    passwrd_entry = ttk.Entry(frame, textvar=passwd, width=50, show="*")
    passwrd_entry.place(x=20, y=320)

    cpasswrd = Label(frame, text="Confirm Password*", font=("times as roman", 12), bg="white")
    cpasswrd.place(x=20, y=350)

    cpasswrd_entry = ttk.Entry(frame, textvar=cpasswd, width=50, show="*")
    cpasswrd_entry.place(x=20, y=380)

    b = Button(frame, text="Register", command=lambda: register(root), width=33, font=("times of roman ", 12), bd=2, relief="groove",
               fg="black", bg="orange").place(x=20, y=420)


def reg_call():
    root = Tk()
    reg_start(root)
    root.mainloop()


if __name__ == '__main__':
    from login_copy import database
    database()
    reg_call()