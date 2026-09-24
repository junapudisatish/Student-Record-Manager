import re

students=[]

#Adding student data
def add_student():
    try:
        student_id=int(input("Enter student id :"))
        name=input("enter student name :")
        age=int(input("Enter student age :"))
        email=input("Enter student email :")
        if not valid_email(email):
            raise ValueError("Invalid Email!")

        student=[student_id,name,age,email]
        students.append(student)

        print("Student record Added successfully")
    except ValueError as e:
        print("Error:",e)

#checking email is valid or not
def valid_email(email):
    check=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(check,email):
        return True
    else:
        return False

#Saving the data
def save_student():
    try:
        if not students:
            print("No student data to save:")
            return

        p=open("students.txt","a")
        for student in students:
            p.write(f"{student[0]},{student[1]},{student[2]},{student[3]}\n")
        print("Student data saved successfully!")
        students.clear()
        p.close()

    except Exception as e:
        print("Error saving the file:",e)
    
#Reading the student data from file            
def read_student():
    try:
        p=open("students.txt","r")
        data=p.readlines()
        if not data:
            print("No student records find!")
            return

        print("\n==== Student Record ====")

        for line in data:
            student_id,name,age,email=line.strip().split(",")

            print("Student ID :",student_id)
            print("Name :",name)
            print("Age :",age)
            print("Email :",email)
            print("---------------------------")
        
        p.close()

    except FileNotFoundError:
        print("File not foound! please save data first.")

    except Exception as e:
        print("Error while reading data:",e)
    


#Main
while True:

    print("\n===== Student Record Manager =====")
    print("1. Add Studenr")
    print("2. Save Student Data")
    print("3. Read Studenr Data")
    print("4. Exit")

    try:
         
        choice=int(input("Enter your choice :"))

        match choice:
            case 1:
                add_student()
            case 2:
                save_student()
            case 3:
                read_student()
            case 4:
                print("Program exited.")
                break
            case _:
                print("Invalid choice! Please select between 1 to 4.")

    except ValueError:
        print("Please enter a number.")
        






