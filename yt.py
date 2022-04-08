# Made by Adithya

from yt_dlp import YoutubeDL
import PySimpleGUI as sg
import time    
import webbrowser
from os import chdir

def ytdownloader(url , path):
    print("Downloading Playlist")
    ydl = YoutubeDL()
    cd = chdir(path)
    r = ydl.extract_info(url, download=True)
sg.theme("TealMono")
layout = [
    [sg.Text('Made By Adithya')],
    [sg.Button('My_Website')],
    [sg.Button('Help')],
    [sg.Text('Enter URL:')],
    [sg.InputText('' , key='URL')],
    [sg.Text("Choose a folder: ")],
    [sg.FolderBrowse(key="file")],
    [sg.Button('Download')]
    ]
time.sleep(2)
window = sg.Window('YT Downloader', layout , size=(600,600) , resizable=True)

time.sleep(3)

while True:
    event, values = window.read()
    url = values["URL"]
    path = values["file"]
    
    
    if event == 'My_Website':
        webbrowser.open('https://vvadithya.github.io', new=2)
    if event == 'Help':
        webbrowser.open('https://vvadithya.github.io/coding_projects/ytdownloader/yt.hml', new=2)  
    if event == 'Download':
        ytdownloader(url , path)              
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

window.close()

