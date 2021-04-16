from tkinter import *
from main import *

def error_window():
    e = Tk()

    error_label = Label(e, text='A Github URL must be provided for badges!')
    ok_button = Button(e, text='Okay')

    error_label.pack()
    ok_button.pack()

    e.mainloop()

def add_markdown(entry_data, entry):
    if entry == title_entry:
        preview_entry.insert(0, '#' + entry_data)

def add_shields(button, githubURL):
    if not githubURL:
        error_window()
    

def get_data(entry):
    entry_data = entry.get()
    add_markdown(entry_data, entry)
