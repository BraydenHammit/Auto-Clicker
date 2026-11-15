import tkinter as tk
import keyboard
import mouse

def stop(_=None):
    global stahp
    stahp = True

stahp = False
rep = 0
def click(_=None):
    global rep, stahp, hotkey
    if not stahp:
        mouse.click('left')
        root.after(int(float(time.get())*1000),click)
        if rep == 0:
            keyboard.remove_hotkey(hotkey)
            hotkey = keyboard.add_hotkey('f7', stop)
    else:
        keyboard.remove_hotkey(hotkey)
        hotkey = keyboard.add_hotkey('f7', click)
        stahp = False


hotkey = keyboard.add_hotkey('f7', click)
root = tk.Tk()
root.geometry('400x400')
root.title('Auto Clicker')

timeT = tk.Label(root,text='Seconds between clicks:')
time = tk.Entry(root,bg='grey')

timeT.pack()
time.pack()

root.mainloop()