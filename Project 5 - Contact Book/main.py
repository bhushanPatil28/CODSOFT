import tkinter as tk
from tkinter import Label, Entry, StringVar, Scrollbar, Button


import pickle

root = tk.Tk()
root.geometry('800x500')
root.config(bg='#F0F0F0')
root.title('Contact Book')

contactlist = []

Name = tk.StringVar()
Number = tk.StringVar()
Email = tk.StringVar()
Address = tk.StringVar()

frame = tk.Frame(root, bg='#F0F0F0')
frame.pack(side=tk.RIGHT)

scroll = tk.Scrollbar(frame, orient=tk.VERTICAL, bg='#F0F0F0', troughcolor='#D0D0D0')
select = tk.Listbox(frame, yscrollcommand=scroll.set, height=12, selectbackground="#A6A6A6", selectmode=tk.SINGLE,
                    bg='#E0E0E0', font=('Arial', 12))
scroll.config(command=select.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
select.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

Label(root, text="Contact Book", font="Helvetica 24 bold", bg="#F0F0F0").place(x=300, y=20)

Label(root, text="NAME", font="Arial 14 bold", bg="#F0F0F0").place(x=50, y=80)
Entry(root, textvariable=Name, font="Arial 14").place(x=160, y=80)

Label(root, text='PHONE No: ', font='Arial 14 bold', bg="#F0F0F0").place(x=50, y=120)
Entry(root, textvariable=Number, font="Arial 14").place(x=190, y=120)

Label(root, text='EMAIL: ', font='Arial 14 bold', bg="#F0F0F0").place(x=50, y=160)
Entry(root, textvariable=Email, font="Arial 14").place(x=190, y=160)

Label(root, text='ADDRESS: ', font='Arial 14 bold', bg="#F0F0F0").place(x=50, y=200)
Entry(root, textvariable=Address, font="Arial 14").place(x=190, y=200)

button_style = {'font': 'Arial 12 bold', 'bg': '#4CAF50', 'fg': 'white', 'bd': 0, 'padx': 10, 'pady': 5}

def Selected():
    if select.curselection():
        return int(select.curselection()[0])
    else:
        return None

def AddContact():
    contactlist.append([Name.get(), Number.get(), Email.get(), Address.get()])
    Select_set()
    RESET()

def EDIT():
    selected_index = Selected()
    if selected_index is not None:
        contactlist[selected_index] = [Name.get(), Number.get(), Email.get(), Address.get()]
        Select_set()
        RESET()

def DELETE():
    selected_index = Selected()
    if selected_index is not None:
        del contactlist[selected_index]
        Select_set()
        RESET()

def VIEW():
    selected_index = Selected()
    if selected_index is not None:
        NAME, PHONE, EMAIL, ADDR = contactlist[selected_index]
        Name.set(NAME)
        Number.set(PHONE)
        Email.set(EMAIL)
        Address.set(ADDR)

def SEARCH():
    query = search_var.get().lower()
    select.delete(0, tk.END)
    for index, (name, _, _, _) in enumerate(contactlist):
        if query in name.lower():
            select.insert(tk.END, name)
            select.selection_set(index)

def VIEW_ALL():
    for contact in contactlist:
        print(contact)

def SaveContacts():
    with open('contacts.pkl', 'wb') as file:
        pickle.dump(contactlist, file)

def LoadContacts():
    try:
        with open('contacts.pkl', 'rb') as file:
            saved_contacts = pickle.load(file)
            contactlist.extend(saved_contacts)
            Select_set()
    except FileNotFoundError:
        pass  # Ignore if the file does not exist

def Select_set():
    contactlist.sort()
    select.delete(0, tk.END)
    for name, _, _, _ in contactlist:
        select.insert(tk.END, name)

def RESET():
    Name.set('')
    Number.set('')
    Email.set('')
    Address.set('')

Label(root, text="Search: ", font="Arial 14 bold", bg="#F0F0F0").place(x=50, y=250)
search_var = tk.StringVar()
search_entry = Entry(root, textvariable=search_var, font="Arial 14")
search_entry.place(x=140, y=250)
Button(root, text="Search", command=SEARCH, **button_style).place(x=300, y=250)

Button(root, text="ADD", command=AddContact, **button_style).place(x=80, y=320)
Button(root, text="EDIT", command=EDIT, **button_style).place(x=180, y=320)
Button(root, text="DELETE", command=DELETE, **button_style).place(x=280, y=320)
Button(root, text="VIEW", command=VIEW, **button_style).place(x=380, y=320)

Button(root, text="VIEW ALL", command=VIEW_ALL, **button_style).place(x=480, y=320)

Button(root, text="EXIT", command=root.destroy, font='Arial 12 bold', bg="#FF4500", fg="white", bd=0, padx=10,
       pady=5).place(x=650, y=420)

# Load existing contacts when the application starts
LoadContacts()

# Save contacts before exiting the application
root.protocol("WM_DELETE_WINDOW", SaveContacts)

root.mainloop()