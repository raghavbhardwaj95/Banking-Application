from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox
import sys

#=================================== Global Functions ====================================== 

def Connecting2Server():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",user="root",password="qwer@1234A",database="the_world_bank")
    except :
        print("An Error Occured.")
    return connection

def ExecutingQuery(connection, query, data=None):
    mycursor = connection.cursor()
    try:
        if data:
            mycursor.execute(query, data)
        else:
            mycursor.execute(query)
        connection.commit()
    except:
        print("An error occurred\nTry again")

def fetch_user(connection, username):
    """Fetch user details by username"""
    fetch_user_query = "SELECT * FROM users WHERE username = %s"
    cursor = connection.cursor()
    cursor.execute(fetch_user_query, (username,))
    result = cursor.fetchone()
    return result

def toggle_windows1_2():
    if sign_in_window.winfo_viewable():
        sign_in_window.withdraw()
        sign_up_window.deiconify()
    else:
        sign_up_window.withdraw()
        sign_in_window.deiconify()

def toggle_windows1_3():
    if sign_in_window.winfo_viewable():
        sign_in_window.withdraw()
        frgt_pswd_window.deiconify()
    else:
        frgt_pswd_window.withdraw()
        sign_in_window.deiconify()

def clear_all():
    email_entry.delete(0,END)
    username_entry.delete(0,END)
    pswd_entry2.delete(0,END)
    cnfm_pswd_entry2.delete(0,END)
    chk_box.set(0)

def connect2database():
    if (email_entry.get()=="" or username_entry.get()=="" or pswd_entry2.get()==""  or cnfm_pswd_entry2.get()==""):
        messagebox.showerror(title="ERROR",message="All Fields are Required.")
    elif(pswd_entry2.get()!=cnfm_pswd_entry2.get()):
        messagebox.showerror(title="ERROR",message="Password Mismatched.")
    elif(chk_box.get()==0):
        messagebox.showerror(title="ERROR",message="Kindly Accept our Terms & Conditions.")
    else:
        connect=Connecting2Server()
        query2="USE the_world_bank"
        ExecutingQuery(connect,query2)
        query3="create table if not exists users(Email varchar(50) not null, UserName varchar(50) primary key not null, password varchar(50) not null)"
        ExecutingQuery(connect,query3)
        
        usrnm_chk="select * from users where UserName=%s"
        mycursor = connect.cursor()
        mycursor.execute(usrnm_chk,(username_entry.get(),)) 
        address=mycursor.fetchone()
        if(address!=None):
            messagebox.showerror(title="ERROR",message="Username Already Exists.\nTry Again Later.")
        else:    
            query="insert into users(Email,UserName,password) values  (%s,%s,%s)"
            mycursor.execute(query,(email_entry.get(),username_entry.get(),pswd_entry2.get()))                         
            connect.commit()
            connect.close()
            messagebox.showinfo(title="Registeration Successful",message="Your Data was Registered Successfully.")
            clear_all()
            toggle_windows1_2()

def sign_in():
    if(username_entry1.get()=="" or password_entry1.get()==""):
        messagebox.showerror(title="ERROR",message="All Fields are Required.")
    else:
        try:
            connect=Connecting2Server()
        except:
            messagebox.showerror(title="ERROR",message="Connectivity Issue.\nTry Again Later.")
            return
        query1="USE the_world_bank"
        mycursor = connect.cursor()
        mycursor.execute(query1)
        chk_details="select * from users where UserName=%s and password=%s"
        mycursor.execute(chk_details,(username_entry1.get(),password_entry1.get()))
        address=mycursor.fetchone()
        if(address==None):
            messagebox.showerror(title="ERROR",message="Username or password incorrect.")
        else:
            main_win()

def change_pswd():
    if(username_entry2.get=="" or pswd_entry2.get()=="" or cnfm_pswd_entry2.get()==""):
        messagebox.showerror(title="ERROR",message="All Fields are Required.")
    elif(pswd_entry2.get()!=cnfm_pswd_entry2.get()):
        messagebox.showerror(title="ERROR",message="Password Mismatched.")
    else:
        connection=Connecting2Server()
        my_cursor=connection.cursor()
        query4="select * from users where username=%s"
        my_cursor.execute(query4,(username_entry2.get()))
        address1=my_cursor.fetchone()
        if(address1==None):
            messagebox.showerror(title="ERROR",message="Incorrt Username")
        else:
            query6="update users set password=%s where username=%s"
            my_cursor.execute(query6,(pswd_entry2.get(),username_entry2.get()))
            connection.commit()
            connection.close()
            messagebox.showinfo(title="Password Changed",message="Password Changed Succesfully\nLogin With New Password")
            toggle_windows1_3()

def eyeBtnWork():
    if (eye_button["image"] == str(closed_eye1)):
        eye_button.config(image=open_eye1)
        eye_button.image = open_eye1
        password_entry1.config(show="")
        password_entry1.show=""
    else:
        eye_button.config(image=closed_eye1)
        eye_button.image = closed_eye1
        password_entry1.config(show="*")
        password_entry1.show="*"

def signupEye01():
    if (button2_1["image"] == str(img2_1_)):
        button2_1.config(image=img2_2_)
        button2_1.image = img2_2_  
        pswd_entry2.config(show="")
        pswd_entry2.show=""
    else:
        button2_1.config(image=img2_1_)
        button2_1.image = img2_1_  
        pswd_entry2.config(show="*")
        pswd_entry2.show="*"

def signupEye02():
    if (button2_2["image"] == str(img2_1_)):
        button2_2.config(image=img2_2_)
        button2_2.image = img2_2_ 
        cnfm_pswd_entry2.config(show="")
        cnfm_pswd_entry2.show=""
    else:
        button2_2.config(image=img2_1_)
        button2_2.image = img2_1_ 
        cnfm_pswd_entry2.config(show="*")
        cnfm_pswd_entry2.show="*"

def resetEye01():
    if (reseteye1["image"] == str(img3_1_)):
        reseteye1.config(image=img3_2_)
        reseteye1.image = img3_2_
        pswd_entry3.config(show="")
        pswd_entry3.show=""
    else:
        reseteye1.config(image=img3_1_)
        reseteye1.image = img3_1_  
        pswd_entry3.config(show="*")
        pswd_entry3.show="*" 

def resetEye02():
    if (reseteye_2["image"] == str(img3_1_)):
        reseteye_2.config(image=img3_2_)
        reseteye_2.image = img3_2_ 
        cnfm_pswd_entry3.config(show="")
        cnfm_pswd_entry3.show=""
    else:
        reseteye_2.config(image=img3_1_)
        reseteye_2.image = img3_1_ 
        cnfm_pswd_entry3.config(show="*")
        cnfm_pswd_entry3.show="*" 
        
# ====================== Sign In Window ======================

sign_in_window=Tk()
sign_in_window.title("Sign In")
sign_in_window.geometry("1000x700+220+15")
sign_in_window.resizable(height=False,width=False)

img1=Image.open("bg.png")
resizedImg1=img1.resize((1000,700))
BgImg1=ImageTk.PhotoImage(resizedImg1)

BgLbl1=Label(sign_in_window,image=BgImg1)
BgLbl1.grid(row=0,column=0)

logo1=Image.open("logoo.png")
resized_logo1=logo1.resize((200,150))
icon1=ImageTk.PhotoImage(resized_logo1)
logo_label1=Label(sign_in_window,image=icon1,bd=False)
logo_label1.place(x=660,y=110)


username_label=Label(sign_in_window,text="Username",font=("yu gothic ui",11),bg="white")
username_label.place(x=600,y=270)
username_entry1=Entry(sign_in_window,bg="whitesmoke",font=("yu gothic ui",10,"bold"),bd=0)
username_entry1.place(x=600,y=295,height=30,width=300)

password_label=Label(sign_in_window,text="Password",font=("yu gothic ui",11),bg="white")
password_label.place(x=600,y=350)
password_entry1=Entry(sign_in_window,bg="whitesmoke",font=("yu gothic ui",10,"bold"),bd=0,show="*")
password_entry1.place(x=600,y=375,height=30,width=300)

closed_eye1=ImageTk.PhotoImage(file="closed-eye.jpg")
open_eye1=ImageTk.PhotoImage(file="open-eye.jpg")

eye_button = Button(sign_in_window, image=closed_eye1,command=eyeBtnWork,bg="white",bd=False,activebackground="white",cursor="hand2")
eye_button.place(x=873,y=377)

new_usr_lbl=Label(sign_in_window,text="New User?",bg="white",font=("open sans",10,"bold"))
new_usr_lbl.place(x=695,y=555)

signup_btn=Button(sign_in_window,text="Sign Up", command=toggle_windows1_2,fg="blue",font=("open sans",10,"bold","underline"),bg="white",bd=False,activebackground="white",activeforeground="blue",cursor="hand2")
signup_btn.place(x=765,y=555)

login=Button(sign_in_window,text="Sign In",command=sign_in,font=("arial",16),bg="mediumslateblue",fg="white",width=16,cursor="hand2",bd=0)
login.place(x=650,y=450)

forgot_pswd_btn=Button(sign_in_window,command=toggle_windows1_3,text="Forgot Password ?",font=("open sans",9,"bold"),bg="white",fg="red",activebackground="white",activeforeground="red",bd=False)
forgot_pswd_btn.place(x=790,y=410)

div_txt=f"{"OR":=^25}"
divider=Label(sign_in_window,text=div_txt,font=("bold",15),bg="white")
divider.place(x=600,y=510)

# ====================== Main Window ======================

connection = Connecting2Server()
def main_win():

# ====================== Main Window specific fuctions ======================

    def chk_blnc():
        blnc_window=Toplevel(main_window)
        blnc_window.title("Account Balance")
        blnc_window.geometry("400x400+500+200")
        blnc_window.config(bg="mistyrose")
        blnc_window.resizable(height=False,width=False)
        info=fetch_user(connection,username=f"{username_entry1.get()}")
        blnc=info[1]
        blnc_lbl=Label(blnc_window,text=f"Dear Customer Your Balance is :\n{blnc} Rs.",font=("yu gothic ui",18,"bold"),bg="mistyrose")
        blnc_lbl.place(x=25,y=150)

    def credit():
        def submit():
            usrnm=f"{username_entry1.get()}"
            fetch_user(connection,username=usrnm)
            query=f"update users set Balance = Balance +%s where UserName=%s"
            try:
                ExecutingQuery(connection,query,(moneyInput.get(),usrnm))
            except:
                print("Query Error Occured\n Try Again Later.")
            messagebox.showinfo(title="Added",message=f"Rs. {moneyInput.get()} have been added to Your Account.")
            credit_window.destroy()

        credit_window=Toplevel(main_window)
        credit_window.title("Transactions")
        credit_window.geometry("300x150+500+200")
        credit_window.config(bg="mistyrose")
        credit_window.resizable(height=False,width=False)
        moneyLabel=Label(credit_window,text="Enter The Amount",font=("arial",10),bg="mistyrose",fg="maroon")
        moneyLabel.place(x=100,y=25)
        moneyInput=Spinbox(credit_window,from_=0,to=10**5,increment=100)
        moneyInput.place(x=80,y=50,height=20,width=150)
        sbmt_btn=Button(credit_window,text="Submit",font=("yu gothic ui",10,"bold"),bg="maroon",fg="white",command=submit)
        sbmt_btn.place(x=80,y=80,height=30,width=150)
        
    def debit():
        def submit():
            try:
                value = int(moneyInput.get())
            except :
                print("Invalid input. Please enter a valid numeric value.")
            info=fetch_user(connection,username=f"{username_entry1.get()}")
            blnc=info[1]                
            if(value>blnc):
                messagebox.showerror(title="ERROR",message="Insufficient funds.")
                debit_window.destroy()
            else:

                usrnm=f"{username_entry1.get()}"
                fetch_user(connection,username=usrnm)
                query="update users set Balance = Balance - %s where UserName=%s"
                try:
                    ExecutingQuery(connection,query,(moneyInput.get(),usrnm))
                    debit_window.withdraw()
                    messagebox.showinfo(title="Money Withdrawn",message=f"Rs. {moneyInput.get()} have been withdrawn from Your Account.")
                except:
                    print("Query Error Occured\n Try Again Later.")

        debit_window=Toplevel(main_window)
        debit_window.title("Transactions")
        debit_window.geometry("300x150+500+200")
        debit_window.config(bg="mistyrose")
        debit_window.resizable(height=False,width=False)
        moneyLabel=Label(debit_window,text="Enter The Amount",font=("arial",10),bg="mistyrose",fg="maroon")
        moneyLabel.place(x=100,y=25)
        moneyInput=Spinbox(debit_window,from_=0,to=10**5,increment=100)
        moneyInput.place(x=80,y=50,height=20,width=150)
        sbmt_btn = Button(debit_window, text="Submit", font=("yu gothic ui", 10, "bold"), bg="maroon", fg="white", command=submit)
        sbmt_btn.place(x=80, y=80, height=30, width=150)

    def send():
        def submit():
            try:
                value = int(moneyInput.get())  # Retrieve the value from the Spinbox
            except :
                print("Invalid input. Please enter a valid numeric amount.")
                return
            info=fetch_user(connection,username=f"{username_entry1.get()}")
            blnc=info[1]
            if(value>blnc):
                messagebox.showerror(title="ERROR",message="Insufficient funds.")
                send_window.destroy()    
            else:
                user1=f"{username_entry1.get()}"
                sec_user=toInput.get()
                my_cursor=connection.cursor()
                usrnm_chk="select * from users where UserName=%s"
                my_cursor.execute(usrnm_chk,(toInput.get(),)) 
                address=my_cursor.fetchone()
                if(address==None):
                    messagebox.showerror(title="ERROR",message="Invalid Username.\nTry Again Later.")
                    send_window.destroy()
                else:                
                    amount=moneyInput.get()
                    query2="update users set Balance =  Balance - %s where UserName=%s"
                    try:
                        ExecutingQuery(connection,query2,(amount,user1))
                        query1="update users set Balance =  Balance + %s where UserName=%s"
                        try:
                            ExecutingQuery(connection,query1,(amount,toInput.get()))
                            messagebox.showinfo(title="Money Transfered",message=f"Rs. {moneyInput.get()} have been transfered from {user1} 's Account to {sec_user}.")
                            send_window.destroy() 
                        except:
                            print("Query-3 Error Occured\n Try Again Later.") 
                    except:
                        print("Query-2 Error Occured\n Try Again Later.")

        send_window=Toplevel(main_window)
        send_window.title("Transactions")
        send_window.geometry("300x220+500+200")
        send_window.config(bg="mistyrose")
        send_window.resizable(height=False,width=False)

        moneyLabel=Label(send_window,text="Enter The Amount To Transfer",font=("arial",10,"bold"),bg="mistyrose",fg="maroon")
        moneyLabel.place(x=60,y=25)
        moneyInput=Spinbox(send_window,from_=0,to=10**5,increment=10,font=("arial",10,))
        moneyInput.place(x=80,y=50,height=25,width=150)

        secUserLabel=Label(send_window,text="Reciever's Username",font=("arial",10,"bold"),bg="mistyrose",fg="maroon")  
        secUserLabel.place(x=85,y=100)
        toInput=Entry(send_window,font=("arial",10,))
        toInput.place(x=80,y=125,height=25,width=150)

        transfer_btn=Button(send_window,text="Send Money", font=("yu gothic ui", 10, "bold"), bg="maroon", fg="white", command=submit)
        transfer_btn.place(x=115,y=170)

    def exit():
        main_window.destroy()
        sys.exit()

    if (connection == None):
        print("Failed to connect to the database.")
    else:
        print("Connection Successful :)")
        main_window=Toplevel(sign_in_window)
        main_window.title("The World Bank")
        main_window.iconbitmap("gta6.ico")
        main_window.geometry("1000x700+220+15")
        main_window.resizable(height=False,width=False)
        main_window.config(bg="mistyrose")

        logo1=Image.open("lol.png")
        resized_logo1=logo1.resize((600,150))
        icon1=ImageTk.PhotoImage(resized_logo1)
        logo_label1=Label(main_window,image=icon1,bd=False,bg="mistyrose")
        logo_label1.place(x=220,y=50)

        wlcm_label=Label(main_window,text=f"Welcome , {username_entry1.get()} ",fg="maroon",font=("yu gothic ui",20,"bold"),bg="mistyrose")
        wlcm_label.place(x=400,y=240)

        services_lbl=Label(main_window,text="Services Currently Available,",font=("yu gothic ui",18),bg="mistyrose")
        services_lbl.place(x=370,y=290)

        chk_blnc1=Button(main_window,text="Check Balance",bg="maroon",fg="white",font=("yu gothic ui",12),activebackground="brown",activeforeground="white",
                        command=chk_blnc)
        chk_blnc1.place(x=70,y=580,height=50,width=200)

        add_money=Button(main_window,text="Add Money",bg="maroon",fg="white",font=("yu gothic ui",12),activebackground="brown",activeforeground="white",
                            command=credit)
        add_money.place(x=740,y=380,height=50,width=200)

        debit1=Button(main_window,text="Cash Withdraw",bg="maroon",fg="white",font=("yu gothic ui",12),activebackground="brown",activeforeground="white",
                        command=debit)
        debit1.place(x=70,y=380,height=50,width=200)
        
        sendMoneyBtn=Button(main_window,text="Send Money",font=("yu gothic ui",12),bg="maroon",fg="white",activebackground="brown",activeforeground="white",
                            command=send)
        sendMoneyBtn.place(x=740,y=580,height=50,width=200)

        credits_label=Label(main_window,text="Credits : Raghav Bhardwaj\n     9646227088",font=("bold",8),bg="mistyrose")
        credits_label.place(x=860,y=665)

        logo0=Image.open("fbi.png")
        resized_logo0=logo0.resize((200,200))
        icon0=ImageTk.PhotoImage(resized_logo0)
        logo_label0=Label(main_window,image=icon0,bd=False,bg="mistyrose")
        logo_label0.place(x=405,y=420)

        seq_lbl=Label(main_window,text="Secured By :",bg="mistyrose",font=("bold",8))
        seq_lbl.place(x=475,y=395)
        
        logo=Image.open("log-out.jpg")
        resized_logo=logo.resize((20,20))
        icon=ImageTk.PhotoImage(resized_logo)

        logut_Btn=Button(main_window,image=icon,bd=False,command=exit)
        logut_Btn.place(x=970,y=10)
        sign_in_window.withdraw()
        main_window.mainloop()
# ====================== Sign Up Window ======================

sign_up_window = Toplevel(sign_in_window)
sign_up_window.title("Sign Up")
sign_up_window.geometry("1000x700+220+15")
sign_up_window.resizable(height=False,width=False)

BgLbl2=Label(sign_up_window,image=BgImg1)
BgLbl2.grid(row=0,column=0)

new_acc_lbl=Label(sign_up_window,text="Create a New Account",font=("yu gothic ui",22,"bold"),fg="darkblue",bg="white")
new_acc_lbl.place(x=605,y=120)

email_label=Label(sign_up_window,text="Email",font=("yu gothic ui",10),bg="white")
email_label.place(x=600,y=180)
email_entry=Entry(sign_up_window,bg="whitesmoke",font=("yu gothic ui",10,"bold"),bd=False)
email_entry.place(x=600,y=205,height=30,width=300)

username_label=Label(sign_up_window,text="Username",font=("yu gothic ui",10),bg="white")
username_label.place(x=600,y=240)
username_entry=Entry(sign_up_window,bg="whitesmoke",font=("yu gothic ui",10,"bold"),bd=False)
username_entry.place(x=600,y=260,height=30,width=300)

pswd_label=Label(sign_up_window,text="Password",font=("yu gothic ui",10),bg="white")
pswd_label.place(x=600,y=295)
pswd_entry2=Entry(sign_up_window,bg="whitesmoke",font=("yu gothic ui",10,"bold"),bd=False,show="*")
pswd_entry2.place(x=600,y=315,height=30,width=300)

cnfm_pswd_lbl=Label(sign_up_window,text="Confirm Password",font=("yu gothic ui",10),bg="white")
cnfm_pswd_lbl.place(x=600,y=350)
cnfm_pswd_entry2=Entry(sign_up_window,bg="whitesmoke",font=("yu gothic ui",10,"bold"),bd=False,show="*")
cnfm_pswd_entry2.place(x=600,y=370,height=30,width=300)

img2_1=Image.open("closed-eye.jpg")
img2_1_=ImageTk.PhotoImage(img2_1)
img2_2=Image.open("open-eye.jpg")
img2_2_=ImageTk.PhotoImage(img2_2)

button2_1=Button(sign_up_window,image=img2_1_,bg="white",bd=False,activebackground="white",cursor="hand2",command=signupEye01)
button2_1.place(x=872,y=317)

button2_2=Button(sign_up_window,image=img2_1_,bg="white",bd=False,activebackground="white",cursor="hand2",command=signupEye02)
button2_2.place(x=872,y=372)

chk_box=IntVar()
trms_chkbox=Checkbutton(sign_up_window,text="I agree to the terms & conditions",bg="white",activebackground="white",variable=chk_box)
trms_chkbox.place(x=600,y=420)

signup_btn=Button(sign_up_window,text="Sign Up",command=connect2database,font=("yu gothic ui",13,"bold"),fg="white",bg="mediumslateblue")
signup_btn.place(x=650,y=460,height=40,width=200)

div_txt=f"{"OR":=^25}"
divider=Label(sign_up_window,text=div_txt,font=("bold",15),bg="white")
divider.place(x=600,y=510)

old_user_label=Label(sign_up_window,text="Existing User?",font=("yu gothic ui",10,"bold"),bg="white")
old_user_label.place(x=680,y=550)

sign_in_btn=Button(sign_up_window,text="Sign In", command=toggle_windows1_2,font=("yu gothic ui",10,"bold","underline"),bg="white",fg="blue",activebackground="white",activeforeground="blue",bd=False)
sign_in_btn.place(x=770,y=550)

sign_up_window.withdraw()
# ====================== Reset Password Window ======================

frgt_pswd_window=Toplevel(sign_in_window) 
frgt_pswd_window.title("Reset Password")
frgt_pswd_window.geometry("1000x700+220+15")
frgt_pswd_window.resizable(height=False,width=False)
BgLbl=Label(frgt_pswd_window,image=BgImg1)
BgLbl.grid(row=0,column=0)

img3_1=Image.open("closed-eye.jpg")
img3_1_=ImageTk.PhotoImage(img2_1)
img3_2=Image.open("open-eye.jpg")
img3_2_=ImageTk.PhotoImage(img2_2)

reset_pswd_lbl=Label(frgt_pswd_window,text="Reset Account Password",font=("yu gothic ui",22,"bold"),fg="darkblue",bg="white")
reset_pswd_lbl.place(x=590,y=120)

username_label2=Label(frgt_pswd_window,text="Username",font=("yu gothic ui",10),bg="white")
username_label2.place(x=600,y=200)
username_entry2=Entry(frgt_pswd_window,bg="whitesmoke",font=("yu gothic ui",10,"bold"),bd=False)
username_entry2.place(x=600,y=220,height=30,width=300)

pswd_label2=Label(frgt_pswd_window,text="Password",font=("yu gothic ui",10),bg="white")
pswd_label2.place(x=600,y=260)
pswd_entry3=Entry(frgt_pswd_window,bg="whitesmoke",font=("yu gothic ui",10,"bold"),bd=False,show="*")
pswd_entry3.place(x=600,y=280,height=30,width=300)

cnfm_pswd_lbl2=Label(frgt_pswd_window,text="Confirm Password",font=("yu gothic ui",10),bg="white")
cnfm_pswd_lbl2.place(x=600,y=320)
cnfm_pswd_entry3=Entry(frgt_pswd_window,bg="whitesmoke",font=("yu gothic ui",10,"bold"),bd=False,show="*")
cnfm_pswd_entry3.place(x=600,y=340,height=30,width=300)

reseteye1=Button(frgt_pswd_window,image=img3_1_,bg="white",bd=False,activebackground="white",cursor="hand2",command=resetEye01)
reseteye1.place(x=872,y=282)

reseteye_2=Button(frgt_pswd_window,image=img3_1_,bg="white",bd=False,activebackground="white",cursor="hand2",command=resetEye02)
reseteye_2.place(x=872,y=342)

reset_btn=Button(frgt_pswd_window,text="Reset Password",command=change_pswd,font=("yu gothic ui",13,"bold"),fg="white",bg="mediumslateblue")
reset_btn.place(x=650,y=400,height=40,width=200)

div_txt=f"{"OR":=^25}"
divider=Label(frgt_pswd_window,text=div_txt,font=("bold",15),bg="white")
divider.place(x=600,y=464)

signin_btn=Button(frgt_pswd_window,command=toggle_windows1_3,text="Back to Sign In",font=("yu gothic ui",13,"bold"),fg="white",bg="mediumslateblue")
signin_btn.place(x=650,y=520,height=40,width=200)
frgt_pswd_window.withdraw()

sign_in_window.mainloop()