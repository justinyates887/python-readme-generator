from tkinter import *

root = Tk()
root.title('EZ-README')
root.iconbitmap('run/assets/ico.ico')

#Buttons
github_button = Button(root, text="Add GitHub URL", width=20)
title_button = Button(root, text="Add Title", width=20)
description_button = Button(root, text="Add Description", width=20)
install_button = Button(root, text='Add Installation Process', width=20)
usage_button = Button(root, text='Add Usage', width=20)
contributors_button = Button(root, text='Add Contributor', width=20)
tests_button = Button(root, text='Add Tests', width=20)
demo_button = Button(root, text='Add Demo Images', width=20)
 
 ################
 # Here we need to add buttons with all of the shield.io license images and allow for them to choose
 ################

 ################
 #Here we need to add some optional badges for them to include
 ################

save_button = Button(root, text='Save', bg='blue', fg='white', width=15)
exit_button = Button(root, text='Exit', bg='red', fg='white', width=15, command=root.quit)

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

#Label Grids
info_label.grid(row=0, column=1)
preview_label.grid(row=0, column=4)

#Entry Grids
github_entry.grid(row=1, column=0, columnspan=2)
title_entry.grid(row=2, column=0, columnspan=2)
description_entry.grid(row=3, column=0, columnspan=2)
install_entry.grid(row=4, column=0, columnspan=2)
usage_entry.grid(row=5, column=0, columnspan=2)
contributors_entry.grid(row=6, column=0, columnspan=2)
tests_entry.grid(row=7, column=0, columnspan=2)
demo_entry.grid(row=8, column=0, columnspan=2)

preview_entry.grid(row=1, column=3, columnspan=3, rowspan=7)

#Button Grids
github_button.grid(row=1, column=2)
title_button.grid(row=2, column=2)
description_button.grid(row=3, column=2)
install_button.grid(row=4, column=2)
usage_button.grid(row=5, column=2)
contributors_button.grid(row=6, column=2)
tests_button.grid(row=7, column=2)
demo_button.grid(row=8, column=2)

save_button.grid(row=8, column=4)
exit_button.grid(row=8, column=5)

root.mainloop()