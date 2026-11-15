import tkinter as tk
import keyboard
import mouse

root = tk.Tk()
root.geometry('400x200')
root.title('Auto Clicker')
timeT = tk.Label(root,text='Seconds between clicks:')
time = tk.Entry(root,bg='grey')
active = tk.Label(root,text='Inactive',fg='red')

def stop(_=None):
    global stahp
    stahp = True
    active.configure(text='Inactive',fg='red')

stahp = False
rep = 0
def preclick(_=None):
    global rep
    rep = 0
    click()

def click():
    global rep, stahp, hotkey
    if not stahp:
        mouse.click(lr.lower())
        try:
            root.after(int(float(time.get())*1000),click)
            active.configure(text='Active',fg='green')
            if rep == 0:
                keyboard.remove_hotkey(hotkey)
                hotkey = keyboard.add_hotkey('f7', stop)
            rep += 1
        except ValueError:
            stop()
            keyboard.remove_hotkey(hotkey)
            hotkey = keyboard.add_hotkey('f7', click)
            stahp = False
    else:
        keyboard.remove_hotkey(hotkey)
        hotkey = keyboard.add_hotkey('f7', preclick)
        stahp = False

lr = 'Left'
def switchLR():
    global lr
    lr = 'Left' if lr == 'Right' else 'Right'
    lrbut.configure(text=lr)
lrbut = tk.Button(root,bg='grey',text='Left',command=switchLR)

hotkey = keyboard.add_hotkey('f7', preclick)

timeT.pack()
time.pack()
active.pack(pady=10)
lrbut.pack(pady=20)

root.mainloop()