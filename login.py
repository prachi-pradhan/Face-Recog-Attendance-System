from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkmacosx import Button
import mysql.connector
from main import Face_Recognition_System
from subprocess import Popen


def main1():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def open_main_window(self):
    # Open main.py using subprocess
        Popen(["python3", "main.py"])
    # You can replace "python" with the appropriate command to run Python on your system

    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1280x780+0+0")

        self.bg=ImageTk.PhotoImage(file="/Users/prachipradhan/Desktop/login/bg.jpeg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=460,y=170,width=340,height=450)

        img1=Image.open("/Users/prachipradhan/Desktop/login/icon.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=580,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=120,y=100)        

        #label
        username=lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)

        #========Icon Images==========
        img2=Image.open("/Users/prachipradhan/Desktop/login/icon.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=500,y=323,width=25,height=25)

        img3=Image.open("/Users/prachipradhan/Desktop/login/pw.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=500,y=395,width=25,height=25)

        #LoginButton
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",borderwidth=0,borderless=1,command=self.login)
        loginbtn.place(x=110,y=300,width=120,height=35)

        #Registerbtn
        registerbtn = Button(frame, text="Register", font=("times new roman", 12, "bold"), command=self.register_window,fg="white",bg="black",borderless=1)
        registerbtn.place(x=90, y=350, width=160)

        #Forgotpassbtn
        registerbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",12,"bold"),fg="white",bg="black",borderless=1)
        registerbtn.place(x=90,y=370,width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        






    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome")
            self.open_main_window()  # Call the method to open main.py
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Alohomora7",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(

                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                        




                                                                            ))
            
            row=my_cursor.fetchone()
            if row is not None:  # Corrected condition
                messagebox.showinfo("Success", "Welcome")
                self.open_main_window()  # Call the method to open main.py
            else:
                messagebox.showerror("Error", "Invalid email and password")


#reset password

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Alohomora7",database="mydata")
            my_cursor=conn.cursor()
            qury=("select * from register  where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("Update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been successfully reset. Please try logging in again.",parent=self.root2)
                self.root2.destroy()





# forgot password window==============
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Pleae enter your email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Alohomora7",database="mydata")
            my_cursor=conn.cursor()
            query=("SELECT * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter valid email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Pasword",font=("times new roman",20,"bold"),fg="black",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Mother's Maiden Name","Your Pet's Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)

                




            


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1280x780+0+0")

        #==========variables==========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



        #=======bg img======
        self.bg=ImageTk.PhotoImage(file="/Users/prachipradhan/Desktop/login/bg.jpeg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #===left img===
        self.bg1=ImageTk.PhotoImage(file="/Users/prachipradhan/Desktop/login/ai.jpeg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=10,y=100,width=470,height=550)

        #=====Main Frame=====
        frame=Frame(self.root,bg="white")
        frame.place(x=470,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGITER HERE", font=("times new roman",25,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #====label and entry====

        #---row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #---row2
        contact=Label(frame,text="Contact Number",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #---row3

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Mother's Maiden Name","Your Pet's Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

         #---row4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15),show="*")
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15),show="*")
        self.txt_pswd.place(x=370,y=340,width=250)

        #====checkbutton=====
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree to the Terms and Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0,bg="white")
        self.checkbtn.place(x=50,y=380)

        #====buttons========
        img=Image.open("/Users/prachipradhan/Desktop/login/register-now.jpeg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white",command=self.register_data)
        b1.place(x=55,y=420,width=200)

        img1=Image.open("/Users/prachipradhan/Desktop/login/login.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white",command=self.return_login)
        b1.place(x=330,y=420,width=200)

    #==============Function declaration==================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are requried")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Passwords must match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree with the terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Alohomora7",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","This e-mail already exists, please try again")
            else:
                my_cursor.execute("INSERT INTO register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()
                                                                                     ))
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

    def return_login(self):
        self.root.destroy()


        

        
        
        

if __name__ == "__main__":
    main1()