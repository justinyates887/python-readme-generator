import PySimpleGUI as sg
import os.path

#Create window
def gui:
    sg.Window(title="README Generator", layout=[[sg.text('Hello World')] [sg.button('Okay')]], margins=(300, 300)).read()

    sg.Text("Choose Location"),
    sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
    sg.FolderBrowse(),

    while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()