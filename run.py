from numpy import pad
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import *
from turtle import bgcolor, onclick, width
from PIL import Image,ImageTk

r=sr.Recognizer()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def record_audio():
 with sr.Microphone() as source:
    speak("What shortcut do you require")
    print("What shortcut do you require")
    audio1=r.listen(source)
    voice_rec = r.recognize_google(audio1)
    print(voice_rec)
    # except sr.UnknownValueError:
    #     speak("Sorry I did not get that")
    #     print("Sorry I did not get that")
    # except sr.RequestError:
    #     speak("Sorry my speech servor is down")
    #     print("Sorry my speech servor is down")
    return voice_rec
  



#CASES FOR SHORTCUTS
def reply(voice_rec):
    if "copy" in voice_rec:
        speak("control plus c")
        print("cntrl+c")
        label2.configure(text="CNTRL + C", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a") # THIS IS NEW
        
    elif "paste" in voice_rec:
        speak("control plus v")
        print("cntrl+v")
        label2.configure(text="CNTRL + v", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "select all content" in voice_rec:
        speak("control plus A")
        print("cntrl+A")
        label2.configure(text="CNTRL + A", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "cut" in voice_rec:
        speak("control plus x")
        print("cntrl+x")
        label2.configure(text="CNTRL + X", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    
    elif "redo" in voice_rec:
        speak("control plus Y")
        print("cntrl+Y")
        label2.configure(text="CNTRL + Y", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "create new folder on desktop or File Explorer" in voice_rec:
        speak("control plus Shift plus n")
        print("cntrl+shift+N")
        label2.configure(text="CNTRL + Shift + N", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "close active window" in voice_rec:
        speak("alt plus f4")
        print("alt+f4")
        label2.configure(text="alt + f4", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "delete selected item to recycle bin" in voice_rec:
       speak("contol plus d")
       print("cntrl+D")
       label2.configure(text="CNTRL + D", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")  
    
    elif "open Quick Link menu" in voice_rec:
        speak("Windows key Plus X")
        print("Windows key + X")
        label2.configure(text="Windows key + X", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open Clipboard bin" in voice_rec:
        speak("Windows key Plus V")
        print("Windows key + V")
        label2.configure(text="Windows key + V", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "open the Windows Ink Workspace" in voice_rec:
        speak("Windows key Plus W")
        print("Windows key + W")
        label2.configure(text="Windows key + W", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        

    elif "open Ease of Access settings" in voice_rec:
        speak("Windows key Plus U")
        print("Windows key + U")
        label2.configure(text="Windows key + U", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open Project settings" in voice_rec:
        speak("Windows key Plus P")
        print("Windows key + P")
        label2.configure(text="Windows key + P", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open Narrator" in voice_rec:
        speak("Windows key Plus Control Plus Enter")
        print("Windows key + Ctrl + Enter")
        label2.configure(text="Windows key + Cntrl + Enter", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "zoom in using the magnifier" in voice_rec:
        speak("Windows key Plus Plus")
        print("Windows key + Plus (+)")
        label2.configure(text="Windows key + (+)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "zoom out using the magnifier" in voice_rec:
        speak("Windows key plus Minus")
        print("Windows key + Minus (-)")
        label2.configure(text="Windows key + (-)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "exit magnifier" in voice_rec:
        speak("Windows key plus Escape")
        print("Windows key + Esc")
        label2.configure(text="Windows key + Esc", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "start IME reconversion" in voice_rec:
        speak("Windows key plus Forwards lash")
        print("Windows key + Forwards lash (/)")
        label2.configure(text="Windows key + (/)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "temporarily peek at the desktop" in voice_rec:
        speak("Windows key plus Comma")
        print("Windows key + Comma (,)")
        label2.configure(text="Windows key + (,)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "maximize app windows" in voice_rec:
        speak("Windows key Plus Up arrow key")
        print("Windows key + Up arrow key")
        label2.configure(text="Windows key + Up Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "minimize app windows" in voice_rec:
        speak("Windows key Plus Down arrow key ")
        print("Windows key + Down arrow key ")
        label2.configure(text="Windows key + Down Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "minimize or maximize all but the active desktop window" in voice_rec:
        speak("Windows key Plus Home")
        print("Windows key + Home")
        label2.configure(text="Windows key + Home", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "restore minimized windows on the desktop" in voice_rec:
        speak("Windows key Plus Shift Plus M")
        print("Windows key + Shift + M")
        label2.configure(text="Windows key + Shift + M", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "stretch desktop window to the top and bottom of the screen" in voice_rec:
        speak("Windows key Plus Shift Plus Up arrow key")
        print("Windows key + Shift + Up arrow key")
        label2.configure(text="Windows key + Shift + Up Arrow Key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "maximize or minimize active windows vertically while maintaining width" in voice_rec:
        speak("Windows key Plus Shift Plus Down arrow key")
        print("Windows key + Shift + Down arrow key")
        label2.configure(text="Windows key + Shift + Down Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "move active window to monitor on the left" in voice_rec:
        speak("Windows key Plus Shift Plus Left arrow key")
        print("Windows key + Shift + Left arrow key")
        label2.configure(text="Windows key + shift + Left Arrow Key ", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "move active window to monitor on the right" in voice_rec:
        speak("Windows key Plus Shift Plus Right arrow key")
        print("Windows key + Shift + Right arrow key")
        label2.configure(text="Windows key + Shift + Right arrow Key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "snap app or window left" in voice_rec:
        speak("Windows key Plus Left arrow key")
        print("Windows key + Left arrow key")
        label2.configure(text="Windows key + Left Arrow Key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "snap app or window right" in voice_rec:
        speak("Windows key Plus Right arrow key")
        print("Windows key + Right arrow key")
        label2.configure(text="Windows key + Right Arrow Key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open app in number position in the taskbar" in voice_rec:
        speak("Windows key Plus Number")
        print("Windows key + Number (0-9)")
        label2.configure(text="Windows key + (0-9)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open another instance of the app in number position in the taskbar" in voice_rec:
        speak("Windows key plus Shift plus Number")
        print("Windows key + Shift + Number (0-9)")
        label2.configure(text="Windows key + Shift + (0-9)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "switch to last active window of the app in number position in the taskbar" in voice_rec:
        speak("Windows key plus Control plus Number")
        print("Windows key + Ctrl + Number (0-9)")
        label2.configure(text="Windows key + Shift + (0-9)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open Jump List of the app in number position in the taskbar" in voice_rec:
        speak("Windows key plus Alt plus Number")
        print("Windows key + Alt + Number (0-9)")
        label2.configure(text="Windows key + Alt + (0-9)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open another instance as an administrator of the app in number position in the taskbar" in voice_rec:
        speak("Windows key Plus Control Plus Shift Plus Number")
        print("Windows key + Number (0-9)")
        label2.configure(text="Windows key + (0-9)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "change previous selected input option" in voice_rec:
        speak("Windows key Plus Control Plus Spacebar")
        print("Windows key + Ctrl + Spacebar")
        label2.configure(text="Windows key + Ctrl + Spacebar", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "change keyboard layout and input language" in voice_rec:
        speak("Windows key Plus Spacebar")
        print("Windows key + Spacebar")
        label2.configure(text="Windows key + Spacebar", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open Task View" in voice_rec:
        speak("Windows key Plus Tab")
        print("Windows key + Tab")
        label2.configure(text="Windows key + Tab", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "create a virtual desktop" in voice_rec:
        speak("Windows key Plus Ctrl Plus D")
        print("Windows key + Ctrl + D")
        label2.configure(text="Windows key + Ctrl + D", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "close active virtual desktop" in voice_rec:
        speak("Windows key Plus Ctrl Plus F4")
        print("Windows key + Ctrl + F4")
        label2.configure(text="Windows key + Ctrl + F4", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "switch to the virtual desktop on the right" in voice_rec:
        speak("Windows key Plus Ctrl Plus Right arrow")
        print("Windows key + Ctrl + Right arrow")
        label2.configure(text="Windows key + Ctrl + Right arrow", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")


    elif "switch to the virtual desktop on the left" in voice_rec:
        speak("Windows key Plus Ctrl Plus Left arrow")
        print("Windows key + Ctrl + Left arrow")
        label2.configure(text="Windows key + Ctrl + Left arrow", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        

    elif "wake up the device when black or a blank screen" in voice_rec:
        speak("Windows key Plus Ctrl Plus Shift Plus B ")
        print("Windows key + Ctrl + Shift + B ")
        label2.configure(text="Windows key + Ctrl + Shift + B", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "capture full screenshot in the \"Screenshots\" folder" in voice_rec:
        speak("Windows key Plus Print Screen")
        print("Windows key + PrtScn")
        label2.configure(text="Windows key + PrtScn", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "create part of the screen screenshot" in voice_rec:
        speak("Windows key Plus Shift Plus S")
        print("Windows key + Shift + S")
        label2.configure(text="Windows key + Shift + S", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "cycle through notifications" in voice_rec:
        speak("Windows key Plus Shift Plus V")
        print("Windows key + Shift + V")
        label2.configure(text="Windows key + Shift + V", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "scroll to bottom of window" in voice_rec:
        speak("End")
        print("End")
        label2.configure(text="End", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "select all content of the current line" in voice_rec:
        speak("Control plus A")
        print("Ctrl + A")
        label2.configure(text="ctrl + A", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "copy selected items to clipboard" in voice_rec:
        speak("Control plus C or Control plus Insert")
        print("Ctrl + C or Ctrl + Insert")
        label2.configure(text="ctrl + C or ctrl + Insert", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "paste content from clipboard" in voice_rec:
        speak("Control plus V or Shift plus Insert")
        print("Ctrl + V or Shift + Insert")
        label2.configure(text="ctrl + V or Shift + Insert", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "starts mark mode" in voice_rec:
        speak("Control plus M")
        print("Ctrl + M")
        label2.configure(text="ctrl + M", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "move screen up one line" in voice_rec:
        speak("Control plus Up arrow key")
        print("Ctrl + Up arrow key ")
        label2.configure(text="ctrl + Up Arrow Key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "move screen down one line" in voice_rec:
        speak("Control plus Down arrow key")
        print("Ctrl + Down arrow key ")
        label2.configure(text="ctrl + Down Arrow Key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "open search for Command Prompt" in voice_rec:
        speak("Control plus F")
        print("Ctrl + F ")
        label2.configure(text="ctrl + F", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "move cursor left or right in the current line" in voice_rec:
        speak("Left or right arrow keys")
        print("Left or right arrow keys ")
        label2.configure(text="Left or Right Arrow Keys", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "cycle through command history of the current session" in voice_rec:
        speak("Up or down arrow keys")
        print("Up or down arrow keys")
        label2.configure(text="Up or down arrow keys", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "move cursor one page up" in voice_rec:
        speak("Page up ")
        print("Page up ")
        label2.configure(text="Page Up", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "move cursor one page down" in voice_rec:
        speak("Page down")
        print("Page down ")
        label2.configure(text="Page Down", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "scroll to top of the console" in voice_rec:
        speak("Control plus Home")
        print("Ctrl + Home")
        label2.configure(text="ctrl + Home", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "scroll to the bottom of the console" in voice_rec:
        speak("Control plus End")
        print("Ctrl + End")
        label2.configure(text="ctrl + End", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "open Start menu" in voice_rec:
        speak("Windows key")
        print("Windows key")
        label2.configure(text="Windows key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "open Action center" in voice_rec:
        speak("Windows key plus A")
        print("Windows key + A") 
        label2.configure(text="Windows key + A", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "open Search" in voice_rec:
        speak("Windows key plua S  or Q")
        print("Windows key + S ( or Q) ")
        label2.configure(text="Windows key + S(or Q)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "display and hide the desktop" in voice_rec:
        speak("Windows key plus D")
        print("Windows key + D ")
        label2.configure(text="Windows key + D", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "locks computer" in voice_rec:
        speak("Windows key plus L")
        print("Windows key + L")
        label2.configure(text="Windows key + L", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "minimize all windows" in voice_rec:
        speak("Windows key plus M")
        print("Windows key + M")
        label2.configure(text="Windows key + M", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "set focus notification area in the taskbar" in voice_rec:
        speak("Windows key plus B")
        print("Windows key + B")
        label2.configure(text="Windows key + B", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "launch Cortana app" in voice_rec:
        speak("Windows key plus C")
        print("Windows key + C")
        label2.configure(text="Windows key + C", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "launch Feedback Hub app" in voice_rec:
        speak("Windows key plus F")
        print("Windows key + F")
        label2.configure(text="Windows key + F", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "launch Game bar app" in voice_rec:
        speak("Windows key plus G")
        print("Windows key + G ")
        label2.configure(text="Windows key + G", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "change input between desktop and Mixed Reality" in voice_rec:
        speak("Windows key plus Y")
        print("Windows key + Y")
        label2.configure(text="Windows key + Y", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "lock device orientation" in voice_rec:
        speak("Windows key plus O")
        print("Windows key + O")
        label2.configure(text="Windows key + O", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "cycle through apps in the taskbar" in voice_rec:
        speak("Windows key plus T")
        print("Windows key + T")
        label2.configure(text="Windows key + T", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "switch input between the desktop experience and Windows Mixed Reality" in voice_rec:
        speak("Windows key plus Z")
        print("Windows key + Z")
        label2.configure(text="Windows key + Z", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "set focus on a tip for Windows 10 when applicable.k" in voice_rec:
        speak("Windows key plus J")
        print("Windows key + J")
        label2.configure(text="Windows key + J", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "open dictation feature" in voice_rec:
        speak("Windows key plus H")
        print("Windows key + H")
        label2.configure(text="Windows key + H", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "open File Explorer" in voice_rec:
        speak("Windows key plus E")
        print("Windows key + E")
        label2.configure(text="Windows key + E", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
         
        
    elif "open Settings" in voice_rec:
        speak("Windows key plus I")
        print("Windows key + I")
        label2.configure(text="Windows key + I", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "open Run command" in voice_rec:
        speak("Windows key plus R")
        print("Windows key + R")
        label2.configure(text="Windows key + R", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "open Connect settings" in voice_rec:
        speak("Windows key plus K")
        print("Windows key + K")
        label2.configure(text="Windows key + K", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "refresh current window" in voice_rec:
        speak("control plus f five")
        print("Ctrl + F5")
        label2.configure(text="ctrl + F5", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")


    elif "view open apps" in voice_rec:
        speak("cntrol plus alt plus tab")
        print("Ctrl + Alt + Tab")
        label2.configure(text="ctrl + Alt + Tab", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    elif "select multiple items on desktop or File Explorer" in voice_rec:
        speak("control plus arrow keys plus spacebar")
        print("Ctrl + Arrow keys (to select) + Spacebar")
        label2.configure(text="ctrl + Arrow keys(to select) + Spacebar", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
        
    elif "runs command for the underlined letter in apps" in voice_rec:
        speak("alt plus underlined letter")
        print("Alt + Underlined letter")
        label2.configure(text="Alt + Underlined Letter", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "switch between open apps while pressing Tab multiple times" in voice_rec:
        speak("alt plus tab")
        print("Alt + Tab")    
        label2.configure(text="Alt + Tab", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "go back" in voice_rec:
        speak("alt plus left arrow key")
        print("Alt + Left arrow key") 
        label2.configure(text="Alt + Left Arrow Key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
        
    elif "go forward" in voice_rec:
        speak("alt plus right arrow key")
        print("Alt + Right arrow key") 
        label2.configure(text="Alt + Right Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a") 
        
        
    elif "move up one screen" in voice_rec:
        speak("alt plus page up")
        print("Alt + Page Up")
        label2.configure(text="Alt + Page up", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a") 
          
    elif "move down one screen" in voice_rec:
        speak("alt plus page down")
        print("Alt + Page down")
        label2.configure(text="Alt + Page Down", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "cycle through open windows" in voice_rec:
        speak("alt plus escape")
        print("Alt + Esc")   
        label2.configure(text="Alt + Esc", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "open context menu for the active window" in voice_rec:
        speak("alt plus spacebar")
        print("Alt + Spacebar")    
        label2.configure(text="Alt + Spacebar", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "reveals typed password in Sign-in screen" in voice_rec:
        speak("alt plus f eight")
        print("Alt + F8")
        label2.configure(text="Alt + F8", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "open another instance of an app from the taskbar" in voice_rec:
        speak("shift plus click app button")
        print("Shift + Click app button")
        label2.configure(text="Shift + Click app Button", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "run app as administrator from the taskbar" in voice_rec:
        speak("control plus shift plus click app button")
        print("Ctrl + Shift + Click app button")
        label2.configure(text="ctrl + Shift + Click App Button", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "show window menu for the app from the taskbar" in voice_rec:
        speak("shift plus right click app button")
        print("Shift + Right-click app button")
        label2.configure(text="Shift + Right-Click App Button", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    
    elif "cycle through windows in the group from the taskbar" in voice_rec:
        speak("control plus click a grouped app button")
        print("Ctrl + Click a grouped app button")
        label2.configure(text="ctrl + Click a grouped App Button", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "show window menu for the group from the taskbar" in voice_rec:
        speak("shift plus right click grouped app button")
        print("Shift + Right-click grouped app button")
        label2.configure(text="Shift + Right-Click App Button", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "move the cursor to the beginning of the previous word" in voice_rec:
        speak("control plus left arrow key")
        print("Ctrl + Left arrow key")
        label2.configure(text="ctrl + Left Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "move the cursor to the beginning of the next word" in voice_rec:
        speak("control plus right arrow key")
        print("Ctrl + Right arrow key")
        label2.configure(text="ctrl + Right Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "move the cursor to the beginning of the previous paragraph" in voice_rec:
        speak("control plus up arrow key")
        print("Ctrl + Up arrow key")
        label2.configure(text="ctrl + Up Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "move the cursor to the beginning of the next paragraph" in voice_rec:
        speak("control plus down arrow key")
        print("Ctrl + Down arrow key")
        label2.configure(text="ctrl + Down Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "select block of text" in voice_rec:
        speak("control plus shift plus arrow key")
        print("Ctrl + Shift + Arrow key")
        label2.configure(text="ctrl + Shift + Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "enable or disable Chinese IME" in voice_rec:
        speak("control plus spacebar")
        print("Ctrl + Spacebar")
        label2.configure(text="ctrl + Spacebar", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "open context menu for selected item" in voice_rec:
        speak("shift plus f ten")
        print("Shift + F10")
        label2.configure(text="Shift + F10", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "enable app menu bar" in voice_rec:
        speak("f ten")
        print("F10")
        label2.configure(text="F10", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "select multiple items" in voice_rec:
        speak("shift plus arrow keys")
        print("Shift + Arrow keys")
        label2.configure(text="Shift + Arrow keys", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "open Quick Link menu" in voice_rec:
        speak("windows key plus x")
        print("Windows key + X")
        label2.configure(text="Windows key + X", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    
    elif "open app in number position from the taskbar" in voice_rec:
        speak("windows key plus number between zero and nine")
        print("Windows key + Number(0-9)")
        label2.configure(text="Windows key + Number(0-9)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "cycle through apps in the taskbar" in voice_rec:
        speak("windows key plus t")
        print("Windows key + T")
        label2.configure(text="Windows key + T", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    
    elif "open Jump List of the app in number position from the taskbar" in voice_rec:
        speak("windows key plus alt plus number between zero and nine")
        print("Windows key + Alt + Number (0-9)")
        label2.configure(text="Windows key + Alt + Number(0-9)", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "display and hide the desktop" in voice_rec:
        speak("windows key plus d")
        print("Windows key + D")
        label2.configure(text="Windows key + D", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "minimize all windows" in voice_rec:
        speak("windows key plus m")
        print("Windows key + M")
        label2.configure(text="Windows key + M", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "restore minimized windows on the desktop" in voice_rec:
        speak("windows key plus shift plus m")
        print("Windows key + Shift + M")
        label2.configure(text="Windows key + Shift + M", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "minimize or maximize all but the active desktop window" in voice_rec:
        speak("windows key plus home")
        print("Windows key + Home")
        label2.configure(text="Windows key + Home", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "stretch desktop window to the top and bottom of the screen" in voice_rec:
        speak("windows key plus shift plus up arrow key")
        print("Windows key + Shift + Up arrow key")
        label2.configure(text="Windows key + Shift + Up Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "maximize or minimize active desktop windows vertically while maintaining width" in voice_rec:
        speak("windows key plus shift plus down arrow key")
        print("Windows key + Shift + Down arrow key") 
        label2.configure(text="Windows key + Shift + Down Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
        
    
    elif "move active window to monitor on the left" in voice_rec:
        speak("windows key plus shift plus left arrow key ")
        print("Windows key + Shift + Left arrow key")
        label2.configure(text="Windows key + Shift + Left Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "return to settings" in voice_rec:
       speak("backspace")
       print("backspace")
       label2.configure(text="Backspace", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
       

    elif "open file explorer" in voice_rec:
       speak("windows plus e")
       print("windows+E")
       label2.configure(text="Windows key + E", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "select address bar" in voice_rec:
       speak("alt plus d")
       print("alt+D")
       label2.configure(text="Alt + D", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "select search box" in voice_rec:
       speak("contol plus e")
       print("cntrl+E")
       label2.configure(text="Ctrl + E", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")      
     
    elif "open new window" in voice_rec:
       speak("contol plus n")
       print("cntrl+N") 
       label2.configure(text="ctrl + N", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "close active window" in voice_rec:
       speak("contol plus w")
       print("cntrl+W")
       label2.configure(text="ctrl + W", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
   
    elif "start search " in voice_rec:
       speak("contol plus f")
       print("cntrl+F")
       label2.configure(text="ctrl + F", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "change view file and folder" in voice_rec:
       speak("contol plus mouse scroll")
       print("cntrl+mouse scroll")
       label2.configure(text="ctrl + mouse scroll", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "expands all folder" in voice_rec:
       speak("contol plus shift plus e")
       print("cntrl+shift+E")   
       label2.configure(text="ctrl + Shift + E", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "create new folder" in voice_rec:
       speak("contol plus shift plus n")
       print("cntrl+shift+N")
       label2.configure(text="ctrl + Shift + N", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "focus on address bar" in voice_rec:
       speak("contol plus l")
       print("cntrl+L")
       label2.configure(text="ctrl + L", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "change folder size" in voice_rec:
       speak("contol plus shift plus number")
       print("cntrl+shift+number") 
       label2.configure(text="ctrl + Shift + Number", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")  
    
    elif "display preview panel" in voice_rec:
       speak("alternate key plus p")
       print("alt+P")
       label2.configure(text="Alt + P", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open properties" in voice_rec:
       speak("alternate key plus enter")
       print("alt+Enter")  
       label2.configure(text="Alt + Enter", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "view next folder" in voice_rec:
       speak("alternate plus right arrow key")
       print("alt+ right arrow") 
       label2.configure(text="Alt + Right Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a") 

    elif "view previous folder" in voice_rec:
       speak("alternate plus left arrow key")
       print("alt+ left arrow")  
       label2.configure(text="Alt + Left Arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "move up folder" in voice_rec:
       speak("alternate plus up arrow key")
       print("alt+ up arrow") 
       label2.configure(text="Alt + Up Arrow Key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "switch active window" in voice_rec:
       speak("fuction key 11")
       print("F11")
       label2.configure(text="F11", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "refresh" in voice_rec:
       speak("fuction key 5")
       print("F5")  
       label2.configure(text="F5", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "rename selected item" in voice_rec:
       speak("fuction key 2")
       print("F2")  
       label2.configure(text="F2", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "switch focus on address bar" in voice_rec:
       speak("fuction key 4")
       print("F4")  
       label2.configure(text="F4", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "refresh file explorer" in voice_rec:
       speak("fuction key 5")
       print("F5")
       label2.configure(text="F5", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")
    
    elif "cycle through elements on screen" in voice_rec:
       speak("fuction key 6")
       print("f6")
       label2.configure(text="F6", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "scroll to top of window" in voice_rec:
       speak("Home")
       print("Home") 
       label2.configure(text="Home", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "move active window to monitor on right" in voice_rec:
       speak("window key plus shift plus right arrow key")
       print("window+shift+right arrow")  
       label2.configure(text="Windows Key + Shift + Right Arrow", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "snap app" in voice_rec:
       speak("window key plus left arrow key")
       print("window+left arrow") 
       label2.configure(text="Windows Key + left Arrow", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open search" in voice_rec:
       speak("window key plus S")
       print("window+S")  
       label2.configure(text="Windows Key + S", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")  

    elif "open date and time in taskbar" in voice_rec:
       speak("window key plus alternate key plus D")
       print("window+alt+D")
       label2.configure(text="Windows Key + Alt + D", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open task view" in voice_rec:
       speak("window key plus tab")
       print("window+tab")   
       label2.configure(text="Windows Key + Tab", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "create new virtual desktop" in voice_rec:
       speak("window key plus control plus D")
       print("window+ctrl+D")
       label2.configure(text="Windows Key + ctrl + D", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "create active virtual desktop" in voice_rec:
       speak("window key plus control plus F4")
       print("window+ctrl+F4")  
       label2.configure(text="Windows Key + ctrl + F4", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")  

    elif "switch to virtual desktop on right" in voice_rec:
       speak("window key plus control plus right arrow key")
       print("window+ctrl+right arrow") 
       label2.configure(text="Windows Key + ctrl +right arrow", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a") 

    elif "switch to virtual desktop on left" in voice_rec:
       speak("window key plus control plus left arrow key")
       print("window+ctrl+left arrow") 
       label2.configure(text="Windows Key + ctrl + left arrow key", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open project settings" in voice_rec:
       speak("window key plus P")
       print("window+P")     
       label2.configure(text="Windows Key + P", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open action center" in voice_rec:
       speak("window key plus A")
       print("window+A")
       label2.configure(text="Windows Key + A", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    elif "open settings app" in voice_rec:
       speak("window key plus I")
       print("window+I")
       label2.configure(text="Windows Key + I", font="Times 30 bold italic",fg="#143d59" ,bg="#f4b41a")

    else:
        speak("Sorry I did not get that")
                    

def ask():
    query=record_audio().lower()
    reply(query)

def write():
    query=(textv.get()).lower()
    reply(query)



root=Tk()

logo=Image.open("D:/Shortcut_with_Voice/samarpan.png")
logo=logo.resize((60,80),Image.ANTIALIAS)
i=ImageTk.PhotoImage(logo)
Label(root,image=i).pack(side=TOP,fill=BOTH)

obj=LabelFrame(root,text="Shortcut ", bd=7,background="#0D98BA",font=15,fg="white")
obj.pack(fill="both" , expand="yes",side=BOTTOM)


frame0=Frame(obj,borderwidth=2,background="#0D98BA")
frame0.pack()

label2 = Label(frame0, text="")
label2.pack(fill=BOTH,pady=(60,0))

frame3=Frame(obj,borderwidth=2,background="#0D98BA")
frame3.pack(padx= 10,side=BOTTOM)

frame1=Frame(frame3,borderwidth=2,background="#0D98BA")
frame1.pack(padx= 10)

frame2=Frame(frame3,borderwidth=2,background="#0D98BA")
frame2.pack()


textv=StringVar()

Entry(frame1,textvariable=textv,font=30,width=55,bd=5).pack(padx=10,side=LEFT)

image=Image.open("D:/Shortcut_with_Voice/samarpan.png")
image=image.resize((60,60),Image.ANTIALIAS)
microphone=ImageTk.PhotoImage(image)
Button(frame1,image=microphone,relief=SUNKEN,borderwidth=10,command=ask).pack(side=LEFT)

btn=Button(frame2,text="Speak",font=10,height=2,width=10,bg="black",fg="white",anchor="center",command=write).pack(padx=10,side=LEFT)

root.title("Shortcut Reminder")
# # root.geometry("600x300")
root.geometry("800x400")
# root.configure()
root.resizable(False,False)
root.mainloop()