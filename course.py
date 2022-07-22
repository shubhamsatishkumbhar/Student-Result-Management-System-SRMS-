#Course Module
from tkinter import*
from PIL import Image,ImageTk  
from tkinter import ttk,messagebox
import sqlite3
class CourseClass:
    def __init__(self,home):
        self.home=home
        self.home.title("Student Result Management System")
        self.home.geometry("1200x500+80+170")
        self.home.config(bg="white")
        self.home.focus_force()

    #Title of Course
        title=Label(self.home,text="Manage Course",font=("times new roman",20,"bold"),bg="#CC3366",fg="white").place(x=0,y=0,relwidth=1,height=40)
    #Variables
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

    #Categories of Courses
        courseName = Label(self.home,text="Course Name",font=("times new roman",15,"bold"),bg="white").place(x=10,y=60)
        duration = Label(self.home,text="Duration",font=("times new roman",15,"bold"),bg="white").place(x=10,y=100)
        charges = Label(self.home,text="Charges",font=("times new roman",15,"bold"),bg="white").place(x=10,y=140)
        description = Label(self.home,text="Description",font=("times new roman",15,"bold"),bg="white").place(x=10,y=180)

    #Entry Fields
        self.courseName1 = Entry(self.home,textvariable=self.var_course,font=("times new roman",15,"bold"),bg="lightyellow")
        self.courseName1.place(x=150,y=60,width=200)

        duration1 = Entry(self.home,textvariable=self.var_duration,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        charges1 = Entry(self.home,textvariable=self.var_charges,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.description1 = Text(self.home,font=("times new roman",15,"bold"),bg="lightyellow")
        self.description1.place(x=150,y=180,width=500,height=150)

    # Buttons
        self.add_btn=Button(self.home,text="Save",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add)
        self.add_btn.place(x=150,y=400,width=120,height=50)
        self.update_btn=Button(self.home,text="Update",font=("times new roman",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.update)
        self.update_btn.place(x=290,y=400,width=120,height=50)
        self.delete_btn=Button(self.home,text="Delete",font=("times new roman",15,"bold"),bg="grey",fg="white",cursor="hand2",command=self.delete)
        self.delete_btn.place(x=430,y=400,width=120,height=50)
        self.clear_btn=Button(self.home,text="Clear",font=("times new roman",15,"bold"),bg="orange",fg="white",cursor="hand2",command=self.clear)
        self.clear_btn.place(x=570,y=400,width=120,height=50)

    #Search Panel
        self.var_search=StringVar()
        search_courseName = Label(self.home,text="Search By Course Name",font=("times new roman",15,"bold"),bg="white").place(x=690,y=60)
        search_courseName1 = Entry(self.home,textvariable=self.var_search,font=("times new roman",15,"bold"),bg="lightyellow").place(x=910,y=60,width=180)
        btn_search=Button(self.home,text="Search",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.search).place(x=1100,y=60,width=90,height=30)
        
    #Content
        self.C_Frame=Frame(self.home,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=360)

    #Table    
        #Scroll bar for table to view all headings
        scroly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrolx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        # Columns and headings and adding commands for the functioning of scroll bar   
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrolx.set,yscrollcommand=scroly.set)
        scrolx.pack(side=BOTTOM,fill=X)
        scroly.pack(side=RIGHT,fill=Y)
        scrolx.config(command=self.CourseTable.xview)
        scroly.config(command=self.CourseTable.yview)
    #Headings and Coloumns for the tables
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]="headings"
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)

        self.CourseTable.pack(fill=BOTH,expand=1)

        self.CourseTable.bind("<ButtonRelease-1>",self.get_data) #When you click on any cid row it will show details on their sections get_data function is defined below

        self.show()  #It is help to show details in table the function is defined at the bottom

        
#--------------database----------------------------------
#Adding name,duration, discription and showing pop messages on pc accordint to that

    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        
        self.var_search.set("")
        
        self.description1.delete('1.0',END)

        self.courseName1.config(state=NORMAL)

    def delete(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.home)
            else:
                cur.execute("Select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error, Select The Course From the List first",parent=self.home)
                else:
                    p=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.home)
                    if p==True:
                        cur.execute("Delete from course where name=? ",(self.var_course.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete","Course deleted Successfully",parent=self.home)
                        self.clear() #We are calling clear because we declare show in to that
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def get_data(self,event):
        self.courseName1.config(state="readonly")
        self.courseName1

        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        
        self.description1.delete('1.0',END)
        self.description1.insert(END,row[4])

# Adding Details and Saving
    def add(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.home)
            else:
                cur.execute("Select * from course where name=?",(self.var_course.get(),)) #Due to tupple we added , at last
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error, Course name already Present",parent=self.home)
                else:
                    cur.execute("Insert into course (name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.description1.get("1.0",END)
                    ) )
                    conn.commit()
                    messagebox.showinfo("Great","Course Added Successfully",parent=self.home)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    #Updating Details
    def update(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.home)
            else:
                cur.execute("Select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Course From List",parent=self.home)
                else:
                    cur.execute("Update course set duration=?,charges=?,description=? where name=? ",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.description1.get("1.0",END),
                        self.var_course.get()
                    ) )
                    conn.commit()
                    messagebox.showinfo("Great","Course Update Successfully",parent=self.home)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def show(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("Select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute(f"Select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__=="__main__":
    home=Tk()
    obj=CourseClass(home)
    home.mainloop()