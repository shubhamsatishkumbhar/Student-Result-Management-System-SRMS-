#Login System
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox,ttk
import sqlite3
import os
class Login:
    def __init__(self, home):
        self.home=home
        self.home.title("Login System")
        self.home.geometry("1400x700+0+0")
        #====BG IMage=====
        self.bg=ImageTk.PhotoImage(file="images/6.jpg")
        self.bg_image=Label(self.home,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.home,bg="white")
        Frame_login.place(x=500,y=100,height=550,width=500)

        # Login title
        title=Label(Frame_login,text="User Login",font=("Times New Roman",25,"bold"),fg="navy blue",bg="light gray").place(x=150,y=20)
        
        #Username and password lable
        lbl_user=Label(Frame_login,text="User Name",font=("Times New Roman",15,"bold"),fg="black",bg="light gray").place(x=45,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="white")
        self.txt_user.place(x=45,y=170,width=400,height=35)


        lbl_pass=Label(Frame_login,text="Password",font=("Times New Roman",15,"bold"),fg="black",bg="light gray").place(x=45,y=240)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="white")
        self.txt_pass.place(x=45,y=270,width=400,height=35)

        forget=Button(Frame_login,text="Forget Password?",cursor="hand2",command=self.forget_window,bg="white",fg="blue",font=("times new roman",15,"bold")).place(x=320,y=320)
        
        #Buttons
        signup=Button(Frame_login,text="Sign Up",cursor="hand2",command=self.register_window,bg="blue",fg="white",font=("times new roman",12,"bold")).place(x=220,y=480,height=40)

        login=Button(Frame_login,command=self.login_function,text="Login",cursor="hand2",bg="navy blue",fg="white",font=("times new roman",20,"bold")).place(x=210,y=370,width=100,height=50)

        lbl_create=Label(Frame_login,text="Create an account?",font=("Times New Roman",15,"bold"),fg="black",bg="light gray").place(x=170,y=450)

        #Checkbuttons
        UserType=Label(Frame_login,text="User : ", font=("times new roman", 15, "bold"), bg="light gray",fg="black").place(x=45,y=85)
        self.txt_UserType=ttk.Combobox (Frame_login,font=("times new roman",13), state="readonly",justify=CENTER) 
        self.txt_UserType['values']=("Select","Student","Admin" ) 
        self.txt_UserType.place(x=120, y=85,width=120,height=30)
        self.txt_UserType.current (0)
        # self.var_chk1 = IntVar()
        # self.var_chk2 = IntVar()
        
        # button1 = Checkbutton(Frame_login, text="Student",variable=self.var_chk1,onvalue=1, offvalue=0,font=("times new roman",20,"bold")).place(x=45,y=80,height=30,width=200)
        
        # button2 = Checkbutton(Frame_login, text="Admin",variable=self.var_chk2,onvalue=1, offvalue=0,font=("times new roman",20,"bold")).place(x=250,y=80,height=30,width=200)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_passwd.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_user.delete(0,END)   
# Function for forgot password
    def forget_passwd(self):
        if self.cmb_quest.get()=="Select"or self.txt_answer.get()=="" or self.txt_new_passwd.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.home2)
        else:
            try:
                conn=sqlite3.connect(database="ResultManagementSystem.db")
                cur=conn.cursor()
                cur.execute("Select * from AllUsers where email=? and question=? and answer=?",(self.txt_user.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select the Correct security question and answer",parent=self.home2)
                    
                else: #Coding for Password Pattern
                    l,u,p,d=0,0,0,0
                    if len(self.txt_new_passwd.get())>=8:
                        for i in self.txt_new_passwd.get():
                            if(i.islower()):
                                l+=1

                            elif(i.isupper()):
                                u+=1 
                            elif(i.isdigit()):
                                d+=1 
                            elif(i=='@'or i=='&'or i=='#' or i=='!' or i=='_'):
                                p+=1 
                        if(l>=1 and u>=1 and d>=1 and p>=1):

                            cur.execute("update AllUsers set password=? where email=? ",(self.txt_new_passwd.get(),self.txt_user.get()))
                            conn.commit()
                            conn.close()
                            messagebox.showinfo("Success","Your Password has been Reset, Please Login with new password",parent=self.home2)
                            self.reset()
                            self.home2.destroy()
                        else:
                            messagebox.showerror("Error","Password should have 8 characters ,atleast one upper case letter,lower case letter,numeric value and special character '@','&','#','!','_'",parent=self.home2) 
                    else:
                        messagebox.showerror("Error","Password should have 8 characters ,atleast one upper case letter,lower case letter,numeric value and special character '@','&','#','!','_'",parent=self.home2)

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.home)

#Forget Password Window
    def forget_window(self):
        if self.txt_user.get()=="":
            messagebox.showerror("Error","Please enter email to reset your password",parent=self.home)
        else:
            try:
                conn=sqlite3.connect(database="ResultManagementSystem.db")
                cur=conn.cursor()
                cur.execute("Select * from AllUsers where email=?",(self.txt_user.get(),))#Selecting AllUsers Database i.e.(Those Who Sign Up)
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Enter Valid Email address to reset your password",parent=self.home)
                    
                else:
                    conn.close()
                    self.home2=Toplevel()
                    self.home2.title("Forget Password")
                    self.home2.geometry("400x400+500+150")
                    self.home2.focus_force()
                    self.home2.grab_set()
                #Title for Forget Interface
                    title=Label(self.home2,text="Forget Password",font=("Times New Roman",25),fg="red",bg="white").place(x=0,relwidth=1)
                #Contents in Forget Password Page
                    question=Label(self.home2, text="Security Question", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=50,y=100)
                    self.cmb_quest=ttk.Combobox (self.home2, font=("times new roman",13), state="readonly",justify=CENTER) 
                    self.cmb_quest['values']=("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name") 
                    self.cmb_quest.place(x=50, y=130,width=250)
                    self.cmb_quest.current (0)
        
                    answer=Label(self.home2, text="Answer", font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=50,y=180)
                    self.txt_answer=Entry(self.home2, font=("times new roman", 15),bg="lightgray")
                    self.txt_answer.place(x=50, y=210,width=250)

                    new_passwd=Label(self.home2, text="New Password", font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=50,y=260)
                    self.txt_new_passwd=Entry(self.home2, font=("times new roman", 15),bg="lightgray")
                    self.txt_new_passwd.place(x=50, y=290,width=250)

                    btn_change_passwd=Button(self.home2,text="Reset Password",command=self.forget_passwd,bg="Green",fg="White",font=("times new roman",15,"bold")).place(x=90,y=340)

                
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.home)

#By clicking on Sign-Up button going directly on sign-up page by destroying login page
    def register_window(self):
        self.home.destroy()
        import Register

#Function for Login Part   
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="" or self.txt_UserType.get()=="select":
            messagebox.showerror("Error","All fields are requires",parent=self.home)
        
        else:
            try:
                conn=sqlite3.connect(database="ResultManagementSystem.db")
                cur=conn.cursor()
                cur.execute("Select * from AllUsers where email=? and password=? and u_name=? ",(self.txt_user.get(),self.txt_pass.get(),self.txt_UserType.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username or Password or UserType",parent=self.home)
                    
                else:
                    if (self.txt_UserType.get()=="Student"):
                        messagebox.showinfo("Success",f"Welcome :- {self.txt_user.get()}",parent=self.home)
                        self.home.destroy()
                        os.system("python dashboardStudent.py")
                    else:
                        messagebox.showinfo("Success",f"Welcome :- {self.txt_user.get()}",parent=self.home)
                        self.home.destroy()
                        os.system("python dashboard.py")
                    conn.close()
     

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.home)
            

home=Tk()
obj=Login(home)
home.mainloop()