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

#Buttons
#############################################################################
def add_license(preview_entry):
    if not githubURL:
        error_window()

    pe = preview_entry
    shield = 'https://img.shields.io/'
    path = 'github/license/' + user_repo['user'] + '/' + user_repo['repo']
    pe.insert(END, '![license](' + shield + path + ')\n')

def add_forks(preview_entry):
    if not githubURL:
        error_window()

    pe = preview_entry
    shield = 'https://img.shields.io/'
    path = 'github/forks/' + user_repo['user'] + '/' + user_repo['repo']
    pe.insert(END, '![forks](' + shield + path + ')\n')

def add_stars(preview_entry):
    if not githubURL:
        error_window()

    pe = preview_entry
    shield = 'https://img.shields.io/'
    path = 'github/stars/' + user_repo['user'] + '/' + user_repo['repo']
    pe.insert(END, '![stars](' + shield + path + ')\n')

def add_size(preview_entry):
    if not githubURL:
        error_window()

    pe = preview_entry
    shield = 'https://img.shields.io/'
    path = 'github/languages/code-size/' + user_repo['user'] + '/' + user_repo['repo']
    pe.insert(END, '![size](' + shield + path + ')\n')

def add_lines(preview_entry):
    if not githubURL:
        error_window()

    pe = preview_entry
    shield = 'https://img.shields.io/'
    path = 'tokei/lines/github/' + user_repo['user'] + '/' + user_repo['repo']
    pe.insert(END, '![lines](' + shield + path + ')\n')

def add_pulls(preview_entry):
    if not githubURL:
        error_window()

    pe = preview_entry
    shield = 'https://img.shields.io/'
    path = 'github/issues-pr-closed/' + user_repo['user'] + '/' + user_repo['repo']
    pe.insert(END, '![pulls](' + shield + path + ')\n')

#############################################################################

def add_markdown(entry_data, heading, pe):
    pe.insert(END, '\n\n##' + heading + '\n\n' + entry_data)

def get_text_data(type, entry, preview_entry):
    heading = type
    pe = preview_entry
    entry_data = entry.get("1.0",'end-1c')
    add_markdown(entry_data, heading, pe)

def get_entry_data(type, entry, preview_entry):
    heading = type
    pe = preview_entry
    entry_data = entry.get()
    add_markdown(entry_data, heading, pe)
