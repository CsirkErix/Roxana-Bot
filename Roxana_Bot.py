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

futtatas = True
Gombok = ['w','s']

#Ez maga az alkalmazás, amit az "app" váétozóban mentünk el
app = ctk.CTk()
ctk.set_appearance_mode("dark")
app.title("Roxana † Version 1.0.3")
app.geometry("400x300")

#Ez a felso szoveg
robloxbot = ctk.CTkLabel(app, text="Roxana Bot", text_color="white" , font=("Arial", 24, "bold"))
robloxbot.pack(pady=20)

keszito = ctk.CTkLabel(app, text="Made by: CsirkErik", font=("Arial", 12, "italic"))
keszito.place(relx=0.98, rely=0.98, anchor="se")


def leallitas():
    global futtatas
    futtatas = False

def botfuttatas():
    while futtatas:
        try:
                gomb_helye = pyautogui.locateCenterOnScreen(resource_path('Reconnect.png'), confidence=0.8)
                print("Reconnecting...")
                for i in range(3):
                    pydirectinput.click(gomb_helye.x, gomb_helye.y)
                    time.sleep(1)
                
                time.sleep(6)
        
        except pyautogui.ImageNotFoundException:
                pass

        for gomb in Gombok:
                if not futtatas:
                    break
        
                time.sleep(2)
        
                pydirectinput.keyDown(gomb)
                time.sleep(3)
                pydirectinput.keyUp(gomb)

def inditas():
    global futtatas
    futtatas = True
    szal1 = threading.Thread(target=botfuttatas)
    szal1.start()

#Ez az indító gomb
inditogomb = ctk.CTkButton(app, text="Start", command=inditas, width=200, height=40, fg_color="green", hover_color="darkgreen")
inditogomb.pack(pady=10)

#Ez a leállító gomb
leallitogomb = ctk.CTkButton(app, text="Stop", command=leallitas, width=200, height=40, fg_color="red", hover_color="darkred")
leallitogomb.pack(pady=10)



#Ez kell a legvegere, ez miatt fut folyton az ablak
app.mainloop()