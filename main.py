from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
import tkinter
import subprocess
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x780+0+0")
        self.root.title("Face Recognition System")


        #first img
        img=Image.open("/Users/prachipradhan/Developer/face_recognition_system/images/logo.jpeg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second img
        img1=Image.open("/Users/prachipradhan/Developer/face_recognition_system/images/logo.jpeg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third img
        img2=Image.open("/Users/prachipradhan/Developer/face_recognition_system/images/logo.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #bg img
        img3=Image.open("/Users/prachipradhan/Developer/face_recognition_system/images/bg.jpeg")
        img3=img3.resize((1280,720),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=-130,y=130,width=1530,height=720)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("helvetica",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #time
        def time():
            string=strftime('%H:%M:%S %p') #p is pm am
            lbl.config(text=string) #putting time in lbl
            lbl.after(1000,time) #after 1000 ms putting lbl in time

        lbl=Label(title_lbl,font=("times new roman",14,'bold'),background='black',foreground='white')
        lbl.place(x=200,y=0,width=110,height=50)
        time() #calling time



        #student button


    
        img4=Image.open("/Users/prachipradhan/Developer/face_recognition_system/images/student_details.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("helvetica",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face button
        img5=Image.open("/Users/prachipradhan/Developer/face_recognition_system/images/face_detector.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img, image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("helvetica",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attedance face button
        img6=Image.open("/Users/prachipradhan/Developer/face_recognition_system/images/attendace.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendace",cursor="hand2",command=self.attendance_data,font=("helvetica",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=800,y=300,width=220,height=40)

       #Help face button
        img7=Image.open("/Users/prachipradhan/Developer/face_recognition_system/images/helpdesk.png")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img, image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("helvetica",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=1100,y=300,width=220,height=40)


       #Train face button
        img8=Image.open("/Users/prachipradhan/Developer/face_recognition_system/images/train.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("helvetica",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=200,y=580,width=220,height=40)

       #Photos button
        img9=Image.open("/Users/prachipradhan/Developer/face_recognition_system/images/photos.png")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("helvetica",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=500,y=580,width=220,height=40)

       #Dev button
        img10=Image.open("images/dev.png")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img, image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("helvetica",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=800,y=580,width=220,height=40)

       #Exit button
        img11=Image.open("images/exit.png")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img, image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("helvetica",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
         os.system('open data')

    def iExit(self):
         self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project?")
         if self.iExit>0:
              self.root.destroy()
         else:
              return





    #===============Function buttons================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
         








 
             




if __name__ == "__main__":
        root=Tk()
        obj=Face_Recognition_System(root)
        root.mainloop()





