BROWN = "#9A297E"
DEEP = "#486594"
RED = "#940303"
ORANGE = "#E6501B"

from tkinter import *
from tkinter import messagebox
import random
 
# ---------------------------------------PASSWORD GENERATOR-----------------------------------------------------------

def gen_pass():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    for i in numbers:
        letters.append(i)
    for i in symbols:
        letters.append(i)
    password = []
    for i in range(0,10):
        password.append(random.choice(letters))
    random.shuffle(password)
    new = ""
    for i in password:
        new+=i
    password_entry.delete(0,END)
    password_entry.insert(0,new) # Entry.insert() requires two arguments: entry.insert(index, string)
       
# ---------------------------------------SAVE PASSWORD-------------------------------------------

def click_add():

    get_website = website_entry.get()
    get_email = email_entry.get()
    get_password = password_entry.get()
    
    if len(get_email)==0 or len(get_password)==0 or len(get_website)==0:
        messagebox.showinfo(title="Fill Everything",message="You can't just let the website, email & password entry empty!!!")
    else:
        is_true = messagebox.askokcancel(title="Check Again",message="Are all information correct?")#<---- message box require only 2 things title, message
        if is_true:
            with open("DAY-29/all.txt","a") as f:
                f.write(f"\n{get_website} | {get_email} | {get_password}")
                
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)
        

# ---------------------------------------SAVE UI-------------------------------------------------


window = Tk()
window.title("PASSWORD")
window.config(padx=70,pady=70,bg=RED)

name = Label(text="Check Password", font=("Century",25,"bold"), fg="white",bg=RED)
name.grid(row=1,column=2)

#LOGO
logo = PhotoImage(file="DAY-29/rlock2.png")
canvas = Canvas(width=300,height=300,bg=RED,highlightthickness=0)
canvas.create_image(150,150,image = logo)
canvas.grid(row=2,column=2)

#LABELS
website_name = Label(text="Website:",font=("Century",16,"bold"), fg="white",bg=RED)
website_name.grid(row=3,column=1,sticky='e')
email_name = Label(text="Email/Username",font=("Century",16,"bold"), fg="white",bg=RED)
email_name.grid(row=4,column=1,sticky='e')
password_name = Label(text="Password",font=("Century",16,"bold"), fg="white",bg=RED)
password_name.grid(row=5,column=1,sticky='e')

#ENTRY
website_entry = Entry(width=35)
website_entry.grid(row=3,column=2,columnspan=2,sticky="EW",pady=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=4,column=2,columnspan=2,sticky="EW",pady=2)
password_entry = Entry(width=21)
password_entry.grid(row=5,column=2,sticky="EW",pady=2)


#BUTTONS
gen = Button(text="Generate",font=("Century",12,"bold"), fg="black",bg="white",command=gen_pass)
gen.grid(row=5,column=3,sticky="EW",padx=2)

add_data = Button(text="Add",font=("Century",12,"bold"), fg="black",bg="white",width=36,command=click_add)
add_data.grid(row=6,column=2,columnspan=2,sticky="EW",pady=2)





window.mainloop()