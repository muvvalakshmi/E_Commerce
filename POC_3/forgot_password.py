from tkinter import *
from win10toast import ToastNotifier
import random
from tkinter import messagebox
import pymysql


def forgot_to_login(root):
    root.destroy()
    from login_copy import login_call
    login_call()


def printt(root):
    btn_otp = Button(root, text="Validate User", width=10, bg="orange", fg="white", command=lambda :check_user(root)).place(x=790, y=280)


def check_user(root):
    global user
    user = fn.get()
    user_exist_query = "select * from registration_copy where email=%s"
    data = mycursor.execute(user_exist_query, user)

    if data:
        global ent_pwd
        global ent_otp
        global ent_confirm_pwd

        def otp_generate(root):
            global sys_gen_otp
            sys_gen_otp = str(random.randint(11111, 99999))
            notifier = ToastNotifier()
            notifier.show_toast("Your OTP is", sys_gen_otp, duration=10, threaded=True)

        New_Password = Label(root, text="New Password", width=20, font=("bold", 10))
        New_Password.place(x=613, y=330)
        ent_pwd = Entry(root, textvar=new_pwd, show="*")
        ent_pwd.place(x=790, y=330)
        Confirm_New_Password = Label(root, text="Confirm New Password", width=20, font=("bold", 10))
        Confirm_New_Password.place(x=613, y=370)
        ent_confirm_pwd = Entry(root, textvar=confirm_new_pwd, show="*")
        ent_confirm_pwd.place(x=790, y=370)
        btn_otp = Button(root, text="Get OTP", width=10, bg="orange", fg="white", command=lambda :otp_generate(root)).place(x=790, y=410)
        lbl_otp = Label(root, text="Enter OTP", width=20, font=("bold", 10))
        lbl_otp.place(x=613, y=450)
        ent_otp = Entry(root, textvar=user_otp)
        ent_otp.place(x=790, y=450)
        btn_otp = Button(root, text="Change Password", width=15, bg="orange", fg="white", command=lambda :valid(root)).place(x=790, y=490)
    else:
        ent_user_name.delete(0, END)
        messagebox.showerror("error", "User does not exist")


def valid(root):
    entry_otp = int(user_otp.get())
    password = new_pwd.get()

    if password.find(" ") == -1 and len(password) >= 8:
        pass
    else:
        password = None
        ent_pwd.delete(0, END)

    # confirm password validation
    confirm_password = confirm_new_pwd.get()
    if password == confirm_password:
        pass
    else:
        confirm_password = None
        ent_confirm_pwd.delete(0, END)
    if int(sys_gen_otp) == entry_otp:
        pass

    else:
        entry_otp = None
        ent_otp.delete(0, END)
        messagebox.showerror("Invalid")

    if password != None and  confirm_password != None and entry_otp != None:
        user = fn.get()
        query = "update registration_copy set password=%s where email =%s"
        data = (password, user)
        mycursor.execute(query, data)
        mydb.commit()
        messagebox.showinfo("Success", "Password changed successfully")
        ent_user_name.delete(0, END)
        ent_otp.delete(0, END)
        ent_confirm_pwd.delete(0, END)
        ent_pwd.delete(0, END)
        forgot_to_login(root)

    else:
        messagebox.showerror("Error", "Please check the fields")


def forgot_start(root):
    root.geometry("500x600")
    root.state("zoomed")  # For Full screen
    root.title("One-Click Pick Forgot Password")
    global fn, user_otp, new_pwd, confirm_new_pwd, ent_user_name
    fn = StringVar()
    user_otp = StringVar()
    new_pwd = StringVar()
    confirm_new_pwd = StringVar()

    global mydb,mycursor
    mydb = pymysql.connect(host='localhost', user='root', password='root')
    mycursor = mydb.cursor()
    mycursor.execute('use e_commerce')
    lbl_forgot_password = Label(root, text="Forgot Password", relief="solid", width=20, font=("arial", 19, "bold"))
    lbl_forgot_password.place(x=650, y=150)

    back_to_login = Button(root, text="Back", width=9, bg="orange", fg="white", command=lambda :forgot_to_login(root)).place(x=1000, y=160)

    lbl_user_name = Label(root, text="Username", width=20, font=("bold", 12))
    lbl_user_name.place(x=613, y=240)

    ent_user_name = Entry(root, textvar=fn)
    ent_user_name.place(x=790, y=240)

    printt(root)

def forgot_call():
    root = Tk()
    forgot_start(root)
    root.mainloop()

if __name__=='__main__':
    from login_copy import database
    database()
    forgot_call()