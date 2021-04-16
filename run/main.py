from populate import *

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

root = Tk()
root.title('EZ-README')
root.iconbitmap('run/assets/ico.ico')

#Buttons
github_button = Button(root, text="Add GitHub URL", width=20, bg='#c1bdbd', command=lambda: add_github(github_entry, preview_entry))
title_button = Button(root, text="Add Title", width=20, bg='#c1bdbd', command=lambda: add_title(title_entry, preview_entry))
description_button = Button(root, text="Add Description", width=20, bg='#c1bdbd', command=lambda: get_text_data('Description', description_entry, preview_entry))
install_button = Button(root, text='Add Installation Process', width=20, bg='#c1bdbd', command=lambda: get_text_data('Installation', install_entry, preview_entry))
usage_button = Button(root, text='Add Usage', width=20, bg='#c1bdbd', command=lambda: get_text_data('Usage', usage_entry, preview_entry))
contributors_button = Button(root, text='Add Contributor', width=20, bg='#c1bdbd', command=lambda: get_entry_data('Contributors', contributors_entry, preview_entry))
tests_button = Button(root, text='Add Tests', width=20, bg='#c1bdbd', command=lambda: get_entry_data('Tests', tests_entry, preview_entry))
demo_button = Button(root, text='Add Demo Images', width=20, bg='#b4b4b4')
 
#License Buttons
mit_image = ImageTk.PhotoImage(Image.open('run/assets/mit.PNG'))
mit_button = Button(root, image=mit_image, command=lambda: add_license(preview_entry))
forks_image = ImageTk.PhotoImage(Image.open('run/assets/forks.PNG'))
forks_button = Button(root, image=forks_image, command=lambda: add_forks(preview_entry))
stars_image = ImageTk.PhotoImage(Image.open('run/assets/stars.PNG'))
stars_button = Button(root, image=stars_image, command=lambda: add_stars(preview_entry))

#Optional Badge Buttons
size_image = ImageTk.PhotoImage(Image.open('run/assets/size.PNG'))
size_button = Button(root, image=size_image, command=lambda: add_size(preview_entry))
lines_image = ImageTk.PhotoImage(Image.open('run/assets/lines.png'))
lines_button = Button(root, image=lines_image, command=lambda: add_lines(preview_entry))
pulls_image = ImageTk.PhotoImage(Image.open('run/assets/closedpr.PNG'))
pulls_button = Button(root, image=pulls_image, command=lambda: add_pulls(preview_entry))

save_button = Button(root, text='Save', bg='#848fe5', fg='white', width=15, padx=30)
exit_button = Button(root, text='Exit', bg='#f94a4a', fg='white', width=15, padx=30, command=root.quit)

 #Entries
github_entry = Entry(root, width=90, borderwidth=3)
title_entry = Entry(root, width=90, borderwidth=3)
description_entry = Text(root, width=68, borderwidth=3, height=8)
install_entry = Text(root, width=68, borderwidth=3, height=8)
usage_entry = Text(root, width=68, borderwidth=3, height=8)
contributors_entry = Entry(root, width=90, borderwidth=3)
tests_entry = Entry(root, width=90, borderwidth=3)
demo_entry = Entry(root, width=90, borderwidth=3)

preview_entry = Text(root, width=68, borderwidth=3, height=40)

#Labels
info_label = Label(root, text='Add any info you need!')
preview_label = Label(root, text='Preview of Markdown')
badges_label = Label(root, text='Optional Badges')

#Label Grids
info_label.grid(row=0, column=1)
preview_label.grid(row=0, column=4)
badges_label.grid(row=3, column=1)

#Entry Grids
github_entry.grid(row=2, column=0, columnspan=2)
title_entry.grid(row=1, column=0, columnspan=2)
description_entry.grid(row=6, column=0, columnspan=2)
install_entry.grid(row=7, column=0, columnspan=2)
usage_entry.grid(row=8, column=0, columnspan=2)
contributors_entry.grid(row=9, column=0, columnspan=2)
tests_entry.grid(row=10, column=0, columnspan=2)
demo_entry.grid(row=11, column=0, columnspan=2)

preview_entry.grid(row=1, column=4, columnspan=3, rowspan=11)

#Button Grids
github_button.grid(row=2, column=2)
title_button.grid(row=1, column=2)
description_button.grid(row=6, column=2)
install_button.grid(row=7, column=2)
usage_button.grid(row=8, column=2)
contributors_button.grid(row=9, column=2)
tests_button.grid(row=10, column=2)
demo_button.grid(row=11, column=2)

mit_button.grid(row=4, column=0)
forks_button.grid(row=4, column=1)
stars_button.grid(row=4, column=2)

size_button.grid(row=5, column=0)
lines_button.grid(row=5, column=1)
pulls_button.grid(row=5, column=2)

save_button.grid(row=12, column=5)
exit_button.grid(row=12, column=6)

#Seperator
separator = ttk.Separator(root, orient='vertical')
separator.grid(column=3, row=0, rowspan=12, sticky='ns')

#Row and column spacing
root.columnconfigure(2, pad=12)
root.columnconfigure(3, pad=12)
root.rowconfigure(8, pad=12)
root.rowconfigure(6, pad=12)

root.mainloop()