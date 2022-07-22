#Database File
import sqlite3
def create_db():
    conn=sqlite3.connect(database="ResultManagementSystem.db")
    cur=conn.cursor()
#Table Creation for Course Page
    cur.execute("Create table if not exists course(cid INTEGER primary key AutoIncrement,name text,duration text, charges text,description text)")
    conn.commit()
#Table Creation for Student Page
    cur.execute("Create table if not exists student(roll INTEGER primary key AutoIncrement,name text,email test,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    conn.commit()
#Table Creation for Result Page
    cur.execute("Create table if not exists result(rid INTEGER primary key AutoIncrement,roll text,name text, course text,marks_obtain text,full_marks text,percentage text)")
    conn.commit()
#Table Creation for Sign_Up Page
    cur.execute("Create table if not exists AllUsers(eid INTEGER primary key AutoIncrement,f_name text,l_namen text, contact text, email text, question text, answer text, password text,u_name text)")
    conn.commit()

    conn.close()

create_db()