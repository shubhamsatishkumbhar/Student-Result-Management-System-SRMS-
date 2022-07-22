#Student Module
from os import name
from tkinter import*
from PIL import Image,ImageTk  
from tkinter import ttk,messagebox
import sqlite3
class StudentClass:
    def __init__(self,home):
        self.home=home
        self.home.title("Student Result Management System")
        self.home.geometry("1200x500+80+170")
        self.home.config(bg="white")
        self.home.focus_force()

    #Title of Course
        title=Label(self.home,text="Manage Student Details",font=("times new roman",20,"bold"),bg="#CC3366",fg="white").place(x=0,y=0,relwidth=1,height=40)
    #Variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_adm_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()

    #Categories of student details 1 side
        rollno = Label(self.home,text="Roll No.",font=("times new roman",15,"bold"),bg="white").place(x=10,y=60)
        name = Label(self.home,text="Name",font=("times new roman",15,"bold"),bg="white").place(x=10,y=100)
        email = Label(self.home,text="Email",font=("times new roman",15,"bold"),bg="white").place(x=10,y=140)
        gender = Label(self.home,text="Gender",font=("times new roman",15,"bold"),bg="white").place(x=10,y=180)

        state = Label(self.home,text="State",font=("times new roman",15,"bold"),bg="white").place(x=10,y=220)
        self.state1 = Entry(self.home,textvariable=self.var_state,font=("times new roman",15,"bold"),bg="lightyellow")
        self.state1.place(x=150,y=220,width=150)

        city = Label(self.home,text="City",font=("times new roman",15,"bold"),bg="white").place(x=330,y=220)
        self.city1 = Entry(self.home,textvariable=self.var_city,font=("times new roman",15,"bold"),bg="lightyellow")
        self.city1.place(x=380,y=220,width=110)

        pin = Label(self.home,text="Pin",font=("times new roman",15,"bold"),bg="white").place(x=510,y=220)
        self.pin1 = Entry(self.home,textvariable=self.var_pin,font=("times new roman",15,"bold"),bg="lightyellow")
        self.pin1.place(x=560,y=220,width=120)


        address = Label(self.home,text="Address",font=("times new roman",15,"bold"),bg="white").place(x=10,y=260)
          
    #Entry Fields 1
        self.rollno1 = Entry(self.home,textvariable=self.var_roll,font=("times new roman",15,"bold"),bg="lightyellow")
        self.rollno1.place(x=150,y=60,width=200)

        name1 = Entry(self.home,textvariable=self.var_name,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        email1 = Entry(self.home,textvariable=self.var_email,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)

        self.gender1 = ttk.Combobox(self.home,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("times new roman",15,"bold"),state="readonly",justify=CENTER)
        self.gender1.place(x=150,y=180,width=200)
        self.gender1.current(0)

    #Address
        self.address = Text(self.home,font=("times new roman",15,"bold"),bg="lightyellow")
        self.address.place(x=150,y=260,width=540,height=100)
    
    
    #Categories of student details 2 side
        dob = Label(self.home,text="D.O.B",font=("times new roman",15,"bold"),bg="white").place(x=360,y=60)
        contact = Label(self.home,text="Contact",font=("times new roman",15,"bold"),bg="white").place(x=360,y=100)
        admission = Label(self.home,text="Admission",font=("times new roman",15,"bold"),bg="white").place(x=360,y=140)
        course = Label(self.home,text="Course",font=("times new roman",15,"bold"),bg="white").place(x=360,y=180)

    #Entry Fields 2
        self.course_list=[]
        #Function call to update list
        self.fetch_course()

        self.dob1 = Entry(self.home,textvariable=self.var_dob,font=("times new roman",15,"bold"),bg="lightyellow")
        self.dob1.place(x=480,y=60,width=200)

        contact1 = Entry(self.home,textvariable=self.var_contact,font=("times new roman",15,"bold"),bg="lightyellow").place(x=480,y=100,width=200)
        admission1 = Entry(self.home,textvariable=self.var_adm_date,font=("times new roman",15,"bold"),bg="lightyellow").place(x=480,y=140,width=200)

        self.course1 = ttk.Combobox(self.home,textvariable=self.var_course,values=self.course_list,font=("times new roman",15,"bold"),state="readonly",justify=CENTER)
        self.course1.place(x=480,y=180,width=200)
        self.course1.set("Select")

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
        search_rollno = Label(self.home,text="Search By Roll No. ",font=("times new roman",15,"bold"),bg="white").place(x=720,y=60)
        search_rollno1 = Entry(self.home,textvariable=self.var_search,font=("times new roman",15,"bold"),bg="lightyellow").place(x=890,y=60,width=160,height=30)
        btn_search=Button(self.home,text="Search",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=100,height=30)
        
    #Content
        self.C_Frame=Frame(self.home,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=360)

    #Table    
        #Scroll bar for table to view all headings
        scroly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrolx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        # Columns and headings and adding commands for the functioning of scroll bar   
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrolx.set,yscrollcommand=scroly.set)
        scrolx.pack(side=BOTTOM,fill=X)
        scroly.pack(side=RIGHT,fill=Y)
        scrolx.config(command=self.CourseTable.xview)
        scroly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("roll",text="Roll No")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="Admission")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="PIN")
        self.CourseTable.heading("address",text="Address")

        self.CourseTable["show"]="headings"

        self.CourseTable.column("roll",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("email",width=100)
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("admission",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("pin",width=100)
        self.CourseTable.column("address",width=100)
        

        self.CourseTable.pack(fill=BOTH,expand=1)

        self.CourseTable.bind("<ButtonRelease-1>",self.get_data) #When you click on any cid row it will show details on their sections get_data function is defined below

        self.show()  #It is help to show details in table the function is defined at the bottom
        
        
        
#--------------database----------------------------------
#Adding name,duration, discription and showing pop messages on pc accordint to that

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_adm_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.address.delete("1.0",END)
        self.rollno1.config(state=NORMAL)

        self.var_search.set("")

    def delete(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_roll.get()=="" :
                messagebox.showerror("Error","Roll No should be required ",parent=self.home)
            else:
                cur.execute("Select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error, Select The Student From the List first",parent=self.home)
                else:
                    p=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.home)
                    if p==True:
                        cur.execute("Delete from student where roll=? ",(self.var_roll.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete","Student deleted Successfully",parent=self.home)
                        self.clear() #We are calling clear because we declare show in to that
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def get_data(self,event):
        self.rollno1.config(state="readonly")
        self.rollno1

        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]

        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_adm_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])

        self.address.delete("1.0",END)
        self.address.insert(END,row[11])
        

# Adding Details and Saving
    def add(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_roll.get()==""or self.var_name.get()=="" or self.var_email.get()=="" or self.var_course=="Select":
                messagebox.showerror("Error","Roll No., Student name, Email and Course must required",parent=self.home)
            else:
                cur.execute("Select * from student where roll=?",(self.var_roll.get(),)) #Due to tupple we added , at last
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error, Roll No. is already Present",parent=self.home)
                else:
                    cur.execute("Insert into student (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_adm_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),

                        self.address.get("1.0",END)
                    ) )
                    conn.commit()
                    messagebox.showinfo("Great","Student Added Successfully",parent=self.home)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    #Updating Details
    def update(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No should be required",parent=self.home)
            else:
                cur.execute("Select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Student From List",parent=self.home)
                else:
                    cur.execute("Update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where  roll=? ",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_adm_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),

                        self.address.get("1.0",END),
                        self.var_roll.get()
                    ) )
                    conn.commit()
                    messagebox.showinfo("Great","Student Update Successfully",parent=self.home)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def show(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("Select * from student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def fetch_course(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("Select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("Select * from student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row !=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record Found",parent=self.home)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__=="__main__":
    home=Tk()
    obj=StudentClass(home)
    home.mainloop()