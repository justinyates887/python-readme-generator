from tkinter import filedialog

def savefileas(preview_entry):
    save_text_as = filedialog.asksaveasfile(mode='w', title="README", defaultextension='.md')
    text_to_save = preview_entry.get('1.0', 'end-1c')
    save_text_as.write(text_to_save)
    save_text_as.close()