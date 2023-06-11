from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import numpy as np
import os


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x780+0+0")
        self.root.title("Face Recognition")

        title_lbl=Label(self.root,text="DEVELOPER",font=("helvetica",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        img_top=Image.open("images/dev.jpg")
        img_top=img_top.resize((1280,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1280,height=720)

        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=750,y=10,width=500,height=600)


        img_top1=Image.open("images/prachi.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #Dev info
        dev_label=Label(main_frame,text="Hello, my name is Prachi.",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I'm a 4th year BTech CSE student",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=40)




        img2=Image.open("images/code.jpeg")
        img2=img2.resize((500,390),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)




     










if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()