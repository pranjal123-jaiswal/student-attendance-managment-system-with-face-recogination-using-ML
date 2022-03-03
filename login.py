from multiprocessing import parent_process
from tkinter import*
from cgitb import text
import string
from time import strftime
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from turtle import bgcolor
from PIL import ImageTk, Image
import tkinter  
from time import strftime  
from datetime import datetime    
from tkinter import filedialog

from numpy import place

from student import student
import os
from train import train
from face_recoginzation import Face_recogination
from attendence import attendence
from developer import developer
from help import help

from main import Face_Recogination_system

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1530x790+0+0")


        # ==== BG managment ==========

        # self.bg=PhotoImage(file="images\login.jpg")

        img4=Image.open(r"C:\Users\HP\Desktop\final year project\images\login.jpg")
        img4=img4.resize((1530,790),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=790) 

        # login frame

        frame_login=Frame(self.root,bg="white")
        frame_login.place(x=500,y=250,height=340,width=500)

        title=Label(frame_login,text="Login Here", font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=130,y=30)
        
        
        desc=Label(frame_login,text="Accountant Employee Login Area", font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=110,y=100)
        
        
        
        lbl_user=Label(frame_login,text="User Name", font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=110,y=140)
        self.text_user=ttk.Entry(frame_login, width=21,font=("times new roman",15,"bold"))
        self.text_user.place(x=110,y=170,width=350,height=35)



        lbl_pass=Label(frame_login,text="Password", font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=110,y=210)
        self.text_pass=ttk.Entry(frame_login, width=21,font=("times new roman",15,"bold"))
        self.text_pass.place(x=110,y=240 ,width=350,height=35)


        forget_btn=Button(frame_login,text="Forget Password",bg="white",cursor="hand2",bd=0,fg="#d77337",font=("times new roman",12)).place(x=110,y=280)
        
        login_btn=Button(self.root,text="Login",bg="#d77337",fg="white",command=self.login_function,cursor="hand2",font=("times new roman",20)).place(x=690,y=570,width=180,height=40)

    
    def login_function(self):
        if self.text_user.get()=="" or self.text_pass.get()=="":
            messagebox.showerror("Error","ALL fields are required",parent=self.root)   

        elif self.text_user.get()!=("pranjal") or self.text_pass.get()!="123456":
            messagebox.showerror("Error","Invalid username or password",parent=self.root)

        else:
            messagebox.showinfo("Welcome",f"welcome {self.text_user.get()}\n Your password: {self.text_pass.get()}",parent=self.root)   
            self.new_window=Toplevel(self.root)
            self.app=Face_Recogination_system(self.new_window)
                    




root=Tk()
obj=login(root)
root.mainloop()    