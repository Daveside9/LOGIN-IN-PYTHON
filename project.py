from tkinter import *

root = Tk()
root.geometry("400x300")

# Function to handle form submission
def getvals():
    print("Accepted")

# Set the background color
root.config(bg="white")  # You can choose any background color you like

# Subheading
subheading = Label(root, text="Python Registration Form", font="ar 18 bold", fg="red", bg="white")
subheading.grid(row=0, column=3)

# Field Names
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
age = Label(root, text="Age")
location = Label(root, text="Location")

# Packing Field Names
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
age.grid(row=4, column=2)
location.grid(row=5, column=2)

# Variables for storing data
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
agevalue = StringVar()
locationvalue = StringVar()
checkvalue = IntVar()

# Creating entry fields
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
ageentry = Entry(root, textvariable=agevalue)
locationentry = Entry(root, textvariable=locationvalue)

# Packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
ageentry.grid(row=4, column=3)
locationentry.grid(row=5, column=3)

# Creating a checkbox
checkbtn = Checkbutton(text="Remember me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

# Submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()
