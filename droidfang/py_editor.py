from tkinter import *
import base64
import tkinter.messagebox as box
import os
import tkinter as gui
from tkinter.filedialog import askopenfilename, asksaveasfilename
import random
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk, messagebox
import pyttsx3


window = gui.Tk()
window.title("py Editor")
window.configure(bg='black')
window.geometry("700x400")

def open_file():
    file_path = askopenfilename(
    filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
    if not file_path:
        return
    text_box.delete("1.0", gui.END)
    with open(file_path, "r") as input_file:
        text = input_file.read()
    text_box.insert(gui.END, text)
    text_box.title("Nightmare Editor - {file_path}")

def save_file():
    file_path = asksaveasfilename(
    defaultextension=".txt",
        filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
    if not file_path:
        return
    with open(file_path, "w") as output_file:
        text = text_box.get("1.0", gui.END)
        output_file.write(text)
    text_box.title("TPA Editor - {file_path}")

#functions
def pop_menu(event):
    menu.tk_popup(event.x_root, event.y_root)

def copy():
    text_box.event_generate("<<Copy>>")

def cut():
    text_box.event_generate("<<Cut>>")

def paste():
    text_box.event_generate("<<Paste>>")

def select_all():
    text_box.event_generate("<<SelectAll>>")

def clear():
    #Clear boxes
    text_box.delete(1.0, END)
    #my_entry.delete(0, END)

def encrypt():
    # Get text from text box
    secret = text_box.get(1.0, END)
    # Clear the text box
    text_box.delete(1.0, END)
    # Convert to byte
    secret = secret.encode("ascii")
    # Convert to base64
    secret = base64.b64encode(secret)
    # Convert it back to ascii
    secret = secret.decode("ascii")
    # Print to text box
    text_box.insert(END, secret)

def decrypt():
    # Get text from text box
    secret = text_box.get(1.0, END)
    # Clear the screen
    text_box.delete(1.0, END)
    # Convert to byte
    secret = secret.encode("ascii")
    # Convert to base64
    secret = base64.b64decode(secret)
    # Convert it back to ascii
    secret = secret.decode("ascii")
    # Print to text box
    text_box.insert(END, secret)

def fangaudiomp3():
    # Get text from text box
    x = text_box.get(1.0, END)
    # Clear the text box
    text_box.delete(1.0, END)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine. setProperty("rate", 190)
    engine.save_to_file(x, 'D:\\bin\\fang\\fangmp3s\\fangaudio_gui.mp3')
    engine.runAndWait()

def run_program():
    pass

#def run_program2():
     #os.system('python NT.py')

#def run_program3():
     #os.system('python NM.py')

# Defines top level menu
topMenu = Menu(window, bd=0, bg="black", fg="grey")
window.config(menu=topMenu)

# Create submenus and cascade them to top level menu
submenu1 = Menu(topMenu, tearoff=False, bg='black', fg='grey')
topMenu.add_cascade(menu=submenu1, label="Py Menu")
submenu1.add_command(label="Open", command=open_file)
submenu1.add_command(label="Save", command=save_file)
submenu1.add_command(label="Save as MP3", command=fangaudiomp3)
submenu1.add_command(label="Exit", command=exit)

# Create nested menus

nestedMenu = Menu(submenu1, tearoff=False, bg='black', fg='grey')
submenu1.add_cascade(menu=nestedMenu, label='Encrypt')
#nestedMenu.add_command(label="Encrypt", command=run_program)
nestedMenu.add_command(label="Encrypt", command=encrypt)
nestedMenu.add_command(label="Decrypt", command=decrypt)
nestedMenu.add_command(label="Clear", command=clear)

#text widget
text_box = ScrolledText(window, undo=True, font="Constantia 16", width=50, height=10, bd=0, bg='black', fg='grey', insertbackground="grey")
text_box.pack(fill=BOTH, side=LEFT, expand=True) #expand=true
#Chiller

#Right Click Menu
menu = Menu(window, tearoff=False, bg="black", fg="grey")
#options
menu.add_command(label="Copy", command=copy)
menu.add_command(label="Cut", command=cut)
menu.add_separator()
menu.add_command(label="Paste", command=paste)
menu.add_separator()
menu.add_command(label="Select All", command=select_all)
#menu.add_command(label="encrypt", command=encrypt)

#Make the menu pop up
window.bind("<Button - 3>", pop_menu)
#The command to run py programs for buttons and drop downs 
#buttonr = Button(window, text='Run My Program', command=run_program)
#buttonr.pack()

window.mainloop()
