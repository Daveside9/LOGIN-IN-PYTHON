from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

#Heading
Label(root, text="Python Registration Form", font="ar 15 bold",).grid(row=0, column=3)

#Field Name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
age = Label(root, text="Age")
location = Label(root, text="Location")

#Packing Fields
name.grid(row=1,  column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
age.grid(row=4, column=2)
location.grid(row=5, column=2)

#Variables for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
agevalue = StringVar
locationvalue = StringVar
checkvalue = IntVar

#Creating entry field
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
ageentry = Entry(root, textvariable =agevalue)
locationentry = Entry(root, textvariable =locationvalue)

#Packing entry field 
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
ageentry.grid(row=4, column=3)
locationentry.grid(row=5, column=3 )

#Creating checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column= 3)
 
 #submit button
Button(text="submit", command=getvals).grid(row=7, column=3)

root.mainloop()