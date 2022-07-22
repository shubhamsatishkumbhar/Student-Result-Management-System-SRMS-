#View Result
from tkinter import*
from PIL import Image,ImageTk  
from tkinter import ttk,messagebox
import sqlite3
class ViewClass:
    def __init__(self,home):
        self.home=home
        self.home.title("Student Result Management System")
        self.home.geometry("1200x500+80+170")
        self.home.config(bg="white")
        self.home.focus_force()

    #Title of result
        title=Label(self.home,text="View Student Results",font=("times new roman",20,"bold"),bg="purple",fg="white").place(x=0,y=0,relwidth=1,height=50)

    #Search
        self.var_search=StringVar()
        self.var_id=""

        lbl_select = Label(self.home,text="Select By Roll No.",font=("times new roman",20,"bold"),bg="white").place(x=280,y=100)
        txt_select = Entry(self.home,textvariable=self.var_search,font=("times new roman",20),bg="lightyellow").place(x=520,y=100,width=150)

        btn_search=Button(self.home,text="Search",font=("times new roman",15,"bold"),bg="lightblue",fg="black",cursor="hand2",command=self.search).place(x=680,y=100,width=100,height=35)

        btn_clear=Button(self.home,text="Clear",font=("times new roman",15,"bold"),bg="lightgreen",fg="black",cursor="hand2",command=self.clear).place(x=800,y=100,width=100,height=35)

        lbl_roll = Label(self.home,text="Roll No.",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name = Label(self.home,text="Name",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course = Label(self.home,text="Course",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks = Label(self.home,text="Marks Obtained",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_full = Label(self.home,text="Total Marks",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_percentage = Label(self.home,text="Percentage",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        self.roll = Label(self.home,font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name = Label(self.home,font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course = Label(self.home,font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.marks = Label(self.home,font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150,height=50)
        self.full = Label(self.home,font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.full.place(x=750,y=280,width=150,height=50)
        self.percentage = Label(self.home,font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.percentage.place(x=900,y=280,width=150,height=50)

        #Delete button
        btn_delete=Button(self.home,text="Delete",font=("times new roman",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=500,y=350,width=150,height=35)


    #------------------------------
    def search(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.home)
            else:
                cur.execute("Select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row !=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.percentage.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record Found",parent=self.home) 
               
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")

    def delete(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_id=="":
                messagebox.showerror("Error","search Student Result First",parent=self.home)
            else:
                cur.execute("Select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.home)
                else:
                    p=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.home)
                    if p==True:
                        cur.execute("Delete from result where rid=? ",(self.var_id,))
                        conn.commit()
                        messagebox.showinfo("Delete","Result deleted Successfully",parent=self.home)
                        self.clear() #We are calling clear because we declare show in to that
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    
if __name__=="__main__":
    home=Tk()
    obj=ViewClass(home)
    home.mainloop()