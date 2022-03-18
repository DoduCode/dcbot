import threading
import mouse
import keyboard
import sys
import tkinter as tk
from tkinter.ttk import Label, Button

def record():
    global mousepos
    global mouse_events
    global keyboard_events

    mouse_events = []

    mousepos = mouse.get_position()
    print(mousepos[0], mousepos[1])
    mouse.hook(mouse_events.append)
    keyboard.start_recording()

    keyboard.wait('esc')
    mouse.unhook(mouse_events.append)
    keyboard_events = keyboard.stop_recording()
    keyboard.start_recording()
    play()

def play():

    keyboard.add_hotkey("windows+esc", lambda: exitapp())
    print('hi')
    
    k_thread = threading.Thread(target = lambda :keyboard.play(keyboard_events))
    k_thread.start()
  
    m_thread = threading.Thread(target = lambda :mouse.play(mouse_events))
    mouse.move(-2000, -2000, absolute=False, duration=0.01)
    mouse.move(mousepos[0], mousepos[1], absolute=False, duration=0.01)
    m_thread.start()

    k_thread.join()
    m_thread.join()

    play()

def exitapp():
    root.destroy()
    sys.exit()
    exit()
    quit()

keyboard.add_hotkey('windows+esc', lambda: exitapp())

root = tk.Tk()
root.geometry('600x400')
root.resizable(True,  True)
root.title('Bot')

l1 = Label(root, text="Press the button to record and press the esc button when you are done recording.\nTo exit the bot while it is running press the esc button.")
    
b1 = Button(root, text = "Record", command = record).pack(ipadx = 10, ipady = 15)

l1.pack()

root.mainloop()
