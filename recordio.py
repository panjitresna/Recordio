"""
Recordio Live Stream Recorder v2.0 by @panjitresna

Recordio is a live stream recorder software

Supported website:
https://chaturbate.com/ (Live Stream)
https://www.facebook.com/ (Video Only)
https://www.instagram.com/ (Video Only - Public Profile)
https://www.pornhub.com/ (Video Only - Make sure that Pornhub is not blocked by your ISP or use VPN to bypass)
https://www.twitch.tv/ (Live Stream)
https://xhamster2.com/ (Video Only)
https://www.xnxx.com/ (Video Only)
https://www.youtube.com/ (Live Stream and Video)

Minimum Requirements:
- Microsoft Windows (7, 8, 10)
- Dual core processor
- 1 GB of RAM
- 150 MB for the software including the dependencies files and plenty of Hard Drive space for long session or multiple live stream recording/download
- Internet connection (at least 4 Mbps to running 1 instance in full HD video recording)

How to Use:
1. Unzip the file
2. Launch application by double click the icon (recordio.exe)
3. Select the default download folder
4. Paste the link in the text box (example: https://www.twitch.tv/shroud)
5. Click "Start Record" button 
6. Video will be recorded to the default download folder

Important Information:
- Please add recordio.exe to the exception list on your antivirus software (if you are unable to run the application or blocked by antivirus). This application is not a virus/malware. We did not spy or steal any information from the client computer
- The script will force to download the live stream video using the highest quality possible. We might add an option to choose the quality in the future update
- Default recorded video file either in MP4 or MKV format. Please use another software to convert the downloaded video to another format. Recommended free video converter software is Handbrake (https://handbrake.fr/). We might add an option to choose the video format in the future update
- You might launch multiple console to record/download multiple live stream/video but its depend on the internet speed (recommended at least 4Mbps internet speed for 1 full HD recording/downloading session)
- Manually close the console/terminal window will make the recording file corrupted. Best way to stop recording/downloading is to press CTRL + C
- You can install or copy the application folder move to flash drive to make it as a portable application
- Please note that Recordio is not responsible for media content which you download, so we suggest to ensure the copyright and permissions of the media before downloading.
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import os
import sys
import time
import urllib.request
import win32api
import subprocess

# Resize console window
# os.system("mode con cols=90 lines=20")

# Get current file directory and convert to path short name
currentDirectory = os.path.dirname(os.path.abspath(__file__))
currentDirectory = win32api.GetShortPathName(currentDirectory)

# Function to create download folder
def createdownloadFolder():
    downloadfolderPath = os.path.join(currentDirectory, "download")
    os.mkdir(downloadfolderPath)

# Function to create dependencies folder
def createdepFolder():
    depfolderPath = os.path.join(currentDirectory, "dependencies")
    os.mkdir(depfolderPath)

# Function to download dependencies file
def dependenciesDownload():
    urllib.request.urlretrieve(depdownloadLink, f"{depfolderPath}\\{depfileName}")

# Function to check dependencies file
def dependenciesChecking():
    if os.path.isfile(f"{depfolderPath}\\{depfileName}"):
        print(depfileName, "is exist")
    else:
        dependenciesDownload()

# Check download folder existence
downloadfolderPath = f"{currentDirectory}\\download"
if os.path.exists(downloadfolderPath):
    print("download folder is exist")
else:
    print("download folder doesn't exist")
    print("Creating download folder...")
    createdownloadFolder()
    print("Download folder is created. Path:", downloadfolderPath)

# Check dependencies folder existence
depfolderPath = f"{currentDirectory}\\dependencies"
if os.path.exists(depfolderPath):
    print("Dependencies folder is exist")
else:
    print("Dependencise folder doesn't exist")
    print("Creating dependencies folder. Do not close the console or window.")
    createdepFolder()
    print("Dependencies folder is created. Path:", depfolderPath)

# Check ffmpeg.exe file existence
if os.path.isfile(f"{depfolderPath}\\ffmpeg.exe"):
    print("ffmpeg.exe is exist")
else:
    print("ffmpeg.exe doesn't exist")
    print("Downloading ffmpeg.exe. Do not close the console or window.")
    depdownloadLink = "http://panjitresna.diskstation.me/ffmpeg.exe"
    depfileName = "ffmpeg.exe"
    dependenciesDownload()
    depfileNotif = "Download failed. Please download ffmpeg.exe manually from https://www.videohelp.com/software/ffmpeg and save the file on the same folder with this application. This application will close automatically in 3 seconds"
    dependenciesChecking()

# Check youtube-dl.exe file existence
if os.path.isfile(f"{depfolderPath}\\youtube-dl.exe"):
    print("youtube-dl.exe is exist")
else:
    print("youtube-dl.exe doesn't exist")
    print("Downloading youtube-dl.exe. Do not close the console or window.")
    depdownloadLink = "https://youtube-dl.org/downloads/latest/youtube-dl.exe"
    depfileName = "youtube-dl.exe"
    dependenciesDownload()
    depfileNotif = "Download failed. Please download youtube-dl.exe manually from https://ytdl-org.github.io/youtube-dl/download.html and save the file on the same folder with this application. This application will close automatically in 3 seconds"
    dependenciesChecking()

clsCommand = "cls"
os.system(command=clsCommand)
print("DO NOT CLOSE THIS CONSOLE/TERMINAL")
print("Waiting for input")

# Prepare the youtube-dl path
youtubedl = f"{depfolderPath}\\youtube-dl.exe"
livestreamLink = ""

# Create application window
mainWindow = Tk()
mainWindow.resizable(False, False)
mainWindow.title("Recordio Live Stream Recorder")

# Function to clear text box
def clearbtnCommand():
    textBox.delete(0, END)

# Function to run start button
def startbtnCommand():
    livestreamLink = link.get()

    if len(livestreamLink) == 0:
        print("Please enter or paste the link")
        messagebox.showinfo("Warning", "Please enter or paste the link")
    else:
        livestreamLink = f'"{livestreamLink}"'

        # Set file name format
        youtubedlFormat = "\\%(title)s-%(id)s.%(ext)s"

        # Set output file name and download path
        downloadOutput = f'"{downloadfolderPath + youtubedlFormat}"'

        # Prepare the command (File saved in download folder)
        cmdCommand = youtubedl + " " + "-o" + " " + downloadOutput + " " + livestreamLink

        mainWindow.destroy()
        subprocess.run(cmdCommand)
        # subprocess.call(cmdCommand)

        # Reserved execution command
        # os.system(cmdCommand) #Error if there is a space inside the path
        # win32api.WinExec(cmdCommand) #No console is created (background process) and the function doesnt wait until the process has completed
        # subprocess.Popen(cmdCommand)
        # subprocess.Popen(cmdCommand, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

# Function to change download folder

'''
Change download folder will destroy old open folder button and start download button and recreate both button again again with the new updated variable
'''

def changefolderCommand():
    newdownloadfolderPath = filedialog.askdirectory()
    labelPath = ttk.Label(mainFrame, text=newdownloadfolderPath)
    labelPath.grid(column=2, row=2, sticky=(W, E), padx=1, pady=1)

    # Check new download folder path
    if len(newdownloadfolderPath) == 0:
        print("Please select download folder")
        messagebox.showinfo("Warning", "Please select download folder")

        labelPath = ttk.Label(mainFrame, text=downloadfolderPath)
        labelPath.grid(column=2, row=2, sticky=(W, E), padx=1, pady=1)
    else:
        def openfolderCommand2():
            os.startfile(newdownloadfolderPath)

        def startbtnCommand2():
            livestreamLink = link.get()

            if len(livestreamLink) == 0:
                print("Please enter or paste the link")
                messagebox.showinfo("Warning", "Please enter or paste the link")
            else:
                livestreamLink = f'"{livestreamLink}"'

                # Set file name format
                youtubedlFormat = "\\%(title)s-%(id)s.%(ext)s"

                # Set output file name and download path
                downloadOutput = f'"{newdownloadfolderPath + youtubedlFormat}"'

                # Prepare the command (File saved in download folder)
                cmdCommand = youtubedl + " " + "-o" + " " + downloadOutput + " " + livestreamLink

                mainWindow.destroy()
                subprocess.run(cmdCommand)
                # subprocess.call(cmdCommand)

                # Reserved execution command
                # os.system(cmdCommand) #Error if there is a space inside the path
                # win32api.WinExec(cmdCommand) #No console is created (background process) and the function doesnt wait until the process has completed
                # subprocess.Popen(cmdCommand)
                # subprocess.Popen(cmdCommand, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        # Create menu bar
        menuBar = Menu(mainWindow)

        # File menu
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Clear", command=clearbtnCommand)
        fileMenu.add_command(label="Start Record", command=startbtnCommand2)
        fileMenu.add_command(label="Select Folder", command=changefolderCommand)
        fileMenu.add_command(label="Open Folder", command=openfolderCommand2)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=exitWindow)
        menuBar.add_cascade(label="File", menu=fileMenu)

        # Help menu
        helpMenu2 = Menu(menuBar, tearoff=0)
        helpMenu2.add_command(label="Help", command=helpwindow)
        helpMenu2.add_command(label="About", command=aboutWindow)
        menuBar.add_cascade(label="Help", menu=helpMenu)

        # Destroy old open folder button and recreate
        openfolderBtn.destroy()
        openfolderBtn2 = ttk.Button(mainFrame, text="Open Folder", command=openfolderCommand2)
        openfolderBtn2.grid(column=4, row=2, sticky=(W, E), padx=1, pady=1)

        # Destroy old start button and recreate
        startBtn.destroy()
        startBtn2 = ttk.Button(mainFrame, text="Start Record", command=startbtnCommand2)
        startBtn2.grid(column=4, row=1, sticky=(W, E), padx=1, pady=1)

        mainWindow.config(menu=menuBar)

# Function to open download folder
def openfolderCommand():
    os.startfile(downloadfolderPath)

# Function to exit window/application
def exitWindow():
    mainWindow.destroy()

# Function to open help message box
def helpwindow():
    messagebox.showinfo("Help", "How to Use: \n1. Launch application by double click the icon (recordio.exe) \n2. Select the default download folder \n3. Paste the link in the text box (example: https://www.twitch.tv/shroud) \n4. Click \"Start Record\" button \n5. Video will be recorded to the default download folder")

# Function to open about message box
def aboutWindow():
    messagebox.showinfo("About", "Recordio Live Stream Recorder v2.0 \nCreated by @panjitresna \nEmail: tresna.panji@gmail.com")

# Create menu bar
menuBar = Menu(mainWindow)

# File menu
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Clear", command=clearbtnCommand)
fileMenu.add_command(label="Start Record", command=startbtnCommand)
fileMenu.add_command(label="Select Folder", command=changefolderCommand)
fileMenu.add_command(label="Open Folder", command=openfolderCommand)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitWindow)
menuBar.add_cascade(label="File", menu=fileMenu)

# Help menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Help", command=helpwindow)
helpMenu.add_command(label="About", command=aboutWindow)
menuBar.add_cascade(label="Help", menu=helpMenu)

# Set main window frame
mainFrame = ttk.Frame(mainWindow, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
mainWindow.columnconfigure(0, weight=1)
mainWindow.rowconfigure(0, weight=1)

# Widget
labelLink = ttk.Label(mainFrame, text="Please Enter or Paste the Link:")
labelLink.grid(column=1, row=1, sticky=(W, E), padx=1, pady=1)

labelFolder = ttk.Label(mainFrame, text="Default Download Folder:")
labelFolder.grid(column=1, row=2, sticky=(W, E), padx=1, pady=1)

labelPath = ttk.Label(mainFrame, text=downloadfolderPath)
labelPath.grid(column=2, row=2, sticky=(W, E), padx=1, pady=1)

link = StringVar()
textBox = ttk.Entry(mainFrame, width=60, textvariable=link)
textBox.grid(column=2, row=1, sticky=(W, E), padx=1, pady=1)

clearBtn = ttk.Button(mainFrame, text="Clear", command=clearbtnCommand)
clearBtn.grid(column=3, row=1, sticky=(W, E), padx=1, pady=1)

startBtn = ttk.Button(mainFrame, text="Start Record", command=startbtnCommand)
startBtn.grid(column=4, row=1, sticky=(W, E), padx=1, pady=1)

changefolderBtn = ttk.Button(mainFrame, text="Select Folder", command=changefolderCommand)
changefolderBtn.grid(column=3, row=2, sticky=(W, E), padx=1, pady=1)

openfolderBtn = ttk.Button(mainFrame, text="Open Folder", command=openfolderCommand)
openfolderBtn.grid(column=4, row=2, sticky=(W, E), padx=1, pady=1)

mainWindow.config(menu=menuBar)
mainloop()