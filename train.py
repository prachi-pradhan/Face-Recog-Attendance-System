from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x780+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("helvetica",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        img_top=Image.open("images/facialrecognition.png")
        img_top=img_top.resize((1280,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1280,height=325)

        img_bottom=Image.open("images/facialrecognition.png")
        img_bottom=img_bottom.resize((1280,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1280,height=325)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier, cursor="hand2",font=("helvetica",30,"bold"),bg="white",fg="red")
        b1_1.place(x=0,y=380,width=1280,height=60)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
    
        #================= Train the classifier and save=====================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Resilt","Training datasets completed!!")

    


        

if __name__ == "__main__":
        root=Tk()
        obj=Train(root)
        root.mainloop()