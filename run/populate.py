from tkinter import *

def error_window():
    e = Tk()

    error_label = Label(e, text='A Github URL must be provided for badges!')
    ok_button = Button(e, text='Okay')

    error_label.pack()
    ok_button.pack()

    e.mainloop()

def add_title(entry, preview_entry):
    global pe
    pe = preview_entry
    entry_data = entry.get()
    pe.insert(END, '#' + entry_data + '\n\n')

def add_github(entry, preview_entry):
    pe = preview_entry
    entry_data = entry.get()
    global githubURL
    githubURL = entry_data
    pe.insert(END, '[GitHub Repo](' + githubURL + ')' + '\n\n')

    github_info = githubURL.split('/')

    global user_repo
    user_repo = {
        'user': github_info[3],
        'repo': github_info[4]
    }

def add_markdown(entry_data, entry, pe):
    return

def add_license(preview_entry):
    if not githubURL:
        error_window()

    pe = preview_entry
    shield = 'https://img.shields.io/'
    path = 'github/license/' + user_repo['user'] + '/' + user_repo['repo']
    pe.insert(END, '![license](' + shield + path + ')\n')


def get_data(entry, preview_entry):
    pe = preview_entry
    entry_data = entry.get()
    add_markdown(entry_data, entry, pe)
