Student = {
    'Balwant':90,
    'Vivek':87,
    'Mohit':85,
    'Manoj':83
}


name=input("Enter the name of student :")
if name in Student:
    print(name,"marks :",Student[name])
else:
    print("Student not found")
    