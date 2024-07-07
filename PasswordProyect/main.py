from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
passworda = ""
password_list = []
def passwordgenerator():
    global password_list
    global passworda
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    for char in password_list:
        passworda += char


    password_entry.delete(0,END)
    password_entry.insert(0,passworda)
    password_list=[]
    passworda=""
    
 


# ---------------------------- SAVE PASSWORD ------------------------------- #


    

def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        
        website:{
            "email": email,
            "password": password        
            
            }
              
              
              
              }


    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title="error", message="You left a camp without text")
    

    else:

        def read():
            try:
                with open("PYTHON\PasswordProyect\saves.json","r") as file:
                    data=json.load(file)

            except:
                with open("PYTHON\PasswordProyect\saves.json","w") as file:
                    json.dump(new_data,file,indent=4)


            else:
                data.update(new_data)
                with open("PYTHON\PasswordProyect\saves.json","w") as file:
                    json.dump(data,file,indent=4)


        read()
            
                
        website_entry.delete(0,END)
        email_entry.delete(0,END)
        password_entry.delete(0,END)

def find_password():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    try:
        with open("PYTHON\PasswordProyect\saves.json","r") as file:
            dict=json.load(file)
            for key,value in dict.items():
                if website!=key:
                    pass
                elif website==key:
                    messagebox.showinfo(title=website,message=f"Email: {value['email']}\nPassword: {value['password']}")
                else:
                    messagebox.showinfo(title="error",message="No website found")
                
    except FileNotFoundError:
        messagebox.showerror(title="error",message="File not Found")
       
        

            
    
        
    
    









# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password")
window.config(padx=20,pady=20)

website_text=Label(text="Website:")
website_text.grid(column=0,row=1)

unsername_text=Label(text="Email/Username:")
unsername_text.grid(column=0,row=2)

password_text=Label(text="Password:")
password_text.grid(column=0,row=3)



canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="PYTHON\PasswordProyect\logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)


website_entry=Entry(width=20)
website_entry.grid(column=1,row=1,columnspan=2,sticky="EW")
website_entry.focus()


email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2,sticky="EW")
email_entry.insert(0,"antcogley05@gmail.com")

password_entry=Entry(width=21)
password_entry.grid(column=1,row=3,sticky="EW")




search_button=Button(text="Search",command=find_password)
search_button.grid(column=2,row=1,sticky="EW")
generate_button=Button(text="Generate Password",command=passwordgenerator)
generate_button.grid(column=2,row=3,sticky="EW")

add_button=Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2,sticky="EW")





window.mainloop()

