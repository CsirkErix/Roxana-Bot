import customtkinter as ctk
import threading
import time
import pyautogui
import pydirectinput
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

running = True
buttons = ['w','s']
move_duration = 5.0
move_interval = 2.0

# -- The base application
app = ctk.CTk()
ctk.set_appearance_mode("dark")
app.title("Roxana † Version 1.1")
app.geometry("533x400")

# -- Text on the top
robloxbot = ctk.CTkLabel(app, text="Roxana Bot", text_color="white" , font=("Arial", 24, "bold"))
robloxbot.pack(pady=20)

# -- Text on the bottom right
keszito = ctk.CTkLabel(app, text="Made by: CsirkErik", font=("Arial", 12, "italic"))
keszito.place(relx=0.98, rely=0.98, anchor="se")

# -- Status indicator
status_canvas = ctk.CTkCanvas(app, width=20, height=20, bg="#242424", highlightthickness=0)
status_canvas.place(x=10, y=10)
status_light = status_canvas.create_oval(2, 2, 18, 18, fill="red", outline="")

# -- Movement duration setting
duration_label = ctk.CTkLabel(app, text="Move duration (sec):")
duration_label.place(relx=0.02, rely=0.70, anchor="w")

duration_entry = ctk.CTkEntry(app, width=80, placeholder_text="5")
duration_entry.place(relx=0.55, rely=0.70, anchor="w")

# -- Movement interval setting
interval_label = ctk.CTkLabel(app, text="Interval between moves (sec):")
interval_label.place(relx=0.02, rely=0.82, anchor="w")

interval_entry = ctk.CTkEntry(app, width=80, placeholder_text="2")
interval_entry.place(relx=0.55, rely=0.82, anchor="w")

def apply_settings():
    global move_duration, move_interval
    try:
        duration_value = float(duration_entry.get())
        if duration_value > 0:
            move_duration = duration_value
    except ValueError:
        pass

    try:
        interval_value = float(interval_entry.get())
        if interval_value >= 0:
            move_interval = interval_value
    except ValueError:
        pass

apply_button = ctk.CTkButton(app, text="Apply", command=apply_settings, width=100)
apply_button.place(relx=0.02, rely=0.94, anchor="w")

def stop():
    global running
    running = False
    status_canvas.itemconfig(status_light, fill="red")

def botrunning():
    global running, move_duration, move_interval
    Reconnect_Check = 0
    while running:
        Reconnect_Check += 1
        if Reconnect_Check >= 15:
            try:
                    button_location = pyautogui.locateCenterOnScreen(resource_path('Reconnect.png'), confidence=0.8)
                    Reconnect_Check = 0
                    for i in range(3):
                        pydirectinput.click(button_location.x, button_location.y)
                        time.sleep(1)
                
                    time.sleep(6)
        
            except pyautogui.ImageNotFoundException:
                    pass

        for button in buttons:
                if not running:
                    break
        
                time.sleep(move_interval)
        
                pydirectinput.keyDown(button)
                time.sleep(move_duration)
                pydirectinput.keyUp(button)

def start():
    global running
    running = True
    status_canvas.itemconfig(status_light, fill="green")
    thread1 = threading.Thread(target=botrunning)
    thread1.start()

# -- Starting button
startbutton = ctk.CTkButton(app, text="Start", command=start, width=200, height=40, fg_color="green", hover_color="darkgreen")
startbutton.pack(pady=10)

# -- Stopping button
stopbutton = ctk.CTkButton(app, text="Stop", command=stop, width=200, height=40, fg_color="red", hover_color="darkred")
stopbutton.pack(pady=10)


# -- This has to be at the end of the code!
app.mainloop()