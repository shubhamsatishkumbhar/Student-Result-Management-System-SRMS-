
#Password,Contact and Email Verifications Code is used in Register.py in the function of (def register_data(self) in try and except part
#Password Verifications Code is used in login.py in the function og def forget_passwd(self) in try and except part

#Password
pass1 =input("Enter Password: ")
l,u,p,d=0,0,0,0
if len(pass1)>=8:
    for i in pass1:
        if(i.islower()):
            l+=1   
        elif(i.isupper()):
            u+=1 
        elif(i.isdigit()):
            d+=1 
        elif(i=='@'or i=='&'or i=='#' or i=='!' or i=='_'):
            p+=1 
    if(l>=1 and u>=1 and d>=1 and p>=1):
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Invalid Password")

    # else:
    #messagebox.showerror("Error","Password should have 8 characters ,atleast one upper case letter,atleast one lower case letter, atleast one numeric value and atleast one special character '@','&','#','!','_'",parent=self.home) 
    #             else:
    #                 messagebox.showerror("Error","Password should have 8 characters ,atleast one upper case letter,atleast one lower case letter, atleast one numeric value and atleast one special character '@','&','#','!','_'",parent=self.home)

#First Name and Last Name
FirstName = 'Shubham'
LastName= "kumbhar"
fn = 0
ln = 0
for i in FirstName:
    if i.isupper() or i.islower():
        fn+=1 
for i in LastName:
    if i.isupper() or i.islower():
        ln+=1 
if fn == len(FirstName) and ln == len(LastName):
    print("OK")
else:
    print("Error")


#Contact
# number =int(input("Enter Number: "))
# if len(number)==10:
#     print("Valid Number")
# else:
#     print("Invalid Number")

contact="1234567288"
s = 0
for i in contact:
    if i.isdigit():
        s+=1
if s==10:
    print("Continue")
else:
    print("error")

#Right Email address Verification
pass1 ="shubham@gmail.com"
k=pass1[-10:-1]
j=k+"m"
print(j)

if(j!="@gmail.com"):
    print("error")
else:
    print("Ok")