#Admin Dashboard
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk 
from course import CourseClass
from student import StudentClass
from result import ResultClass
from ViewResult import ViewClass
import sqlite3 
import os
class ResultManagementSystem:
    def __init__(self,home):
        self.home=home
        self.home.title("Student Result Management System")
        self.home.geometry("1450x700+0+0")
        self.home.config(bg="white")

        #Importing image logo (icons)
        self.logo=Image.open("images/logo.jpg")
        self.logo=self.logo.resize((90,35),Image.Resampling.LANCZOS)
        self.logo=ImageTk.PhotoImage(self.logo)

        #Title of project
        title=Label(self.home,text="Student Result Management",padx=10,compound=LEFT,image=self.logo,font=("times new roman",20,"bold"),bg="Navy Blue",fg="white").place(x=0,y=0,relwidth=1,height=50)

        # Menu 
        Frame = LabelFrame(self.home,text="Menu",font=("times new roman",15,"bold"),bg="white")
        Frame.place(x=10,y=70,width=1340,height=80)

        #SubMenu
        button_Course=Button(Frame,text="Course",font=("ties new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)

        button_Student=Button(Frame,text="Student",font=("ties new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)

        button_Result=Button(Frame,text="Result",font=("ties new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)

        button_View=Button(Frame,text="View Student Result",font=("ties new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add_view).place(x=680,y=5,width=200,height=40)

        button_Logout=Button(Frame,text="Logout",font=("ties new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)

        button_Exit=Button(Frame,text="Exit",font=("ties new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.exit).place(x=1120,y=5,width=200,height=40)

        # Content Window
        self.bgImage=Image.open("Images/7.jpg")
        self.bgImage=self.bgImage.resize((900,350),Image.Resampling.LANCZOS)
        self.bgImage=ImageTk.PhotoImage(self.bgImage)

        self.lbl_bg=Label(self.home,image=self.bgImage).place(x=400,y=180,width=940,height=350)

        # Update Details
        self.totalCourse=Label(self.home,text="Total Courses \n 0 ",font=("times new roman",20),bd=10,relief=RIDGE,bg="purple",fg="white")
        self.totalCourse.place(x=400,y=530,width=300,height=80)
        self.totalstudent=Label(self.home,text="Total Student \n 0 ",font=("times new roman",20),bd=10,relief=RIDGE,bg="orange",fg="white")
        self.totalstudent.place(x=720,y=530,width=300,height=80)

        self.totalresults=Label(self.home,text="Total Results \n 0 ",font=("times new roman",20),bd=10,relief=RIDGE,bg="coral",fg="white")
        self.totalresults.place(x=1040,y=530,width=300,height=80)

        #Footer
        footer=Label(self.home,text="Contact Me: \n  shubhamkumbhar45660@gmail.com",font=("times new roman",13,"bold"),bg="grey",fg="white").pack(side=BOTTOM,fill=X)

        self.update_details()

    #Adding function for bottom buttons(Total corses,students,results)
    def update_details(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("Select * from course")
            cr=cur.fetchall()
            self.totalCourse.config(text=f"Total Course\n[{str(len(cr))}]")
            self.totalCourse.after(200,self.update_details)

            cur.execute("Select * from student")
            cr=cur.fetchall()
            self.totalstudent.config(text=f"Total Students\n[{str(len(cr))}]")
                
            cur.execute("Select * from result")
            cr=cur.fetchall()
            self.totalresults.config(text=f"Total Results\n[{str(len(cr))}]")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    #Adding Sub-Menus for Functioning 
    def add_course(self):
        self.window1=Toplevel(self.home)
        self.obj1=CourseClass(self.window1)

    def add_student(self):
        self.window1=Toplevel(self.home)
        self.obj1=StudentClass(self.window1)
    
    def add_result(self):
        self.window1=Toplevel(self.home)
        self.obj1=ResultClass(self.window1)
    
    def add_view(self):
        self.window1=Toplevel(self.home)
        self.obj1=ViewClass(self.window1)

#Functioning of Exit and Logout Button
    def logout(self):
        op=messagebox.askyesno("Confirm Again","Do You really Want to Logout ?",parent=self.home)
        if op==True:
            self.home.destroy()
            os.system("Python Login.py")

    def exit(self):
        op=messagebox.askyesno("Confirm Again","Do You really Want to Exit ?",parent=self.home)
        if op==True:
            self.home.destroy()


if __name__=="__main__":
    home=Tk()
    obj=ResultManagementSystem(home)
    home.mainloop()