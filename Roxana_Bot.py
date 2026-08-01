import customtkinter as ctk
import threading
import time
import pyautogui
import pydirectinput

futtatas = True
Gombok = ['w','s']

#Ez maga az alkalmazás, amit az "app" váétozóban mentünk el
app = ctk.CTk()
ctk.set_appearance_mode("dark")
app.title("Roxána † Version 1.0")
app.geometry("400x300")

#Ez a felso szoveg
robloxbot = ctk.CTkLabel(app, text="Roxána Bot", text_color="white" , font=("Arial", 24, "bold"))
robloxbot.pack(pady=20)

keszito = ctk.CTkLabel(app, text="Made by: CsirkErik", font=("Arial", 12, "italic"))
keszito.place(relx=0.98, rely=0.98, anchor="se")


def leallitas():
    global futtatas
    futtatas = False

def botfuttatas():
    while futtatas:
        try:
                gomb_helye = pyautogui.locateCenterOnScreen('Reconnect.png', confidence=0.8)
                print("Újracsatlakozás folyamatban...")
        
                pydirectinput.click(gomb_helye.x, gomb_helye.y)
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
inditogomb = ctk.CTkButton(app, text="Indítás", command=inditas, width=200, height=40, fg_color="green", hover_color="darkgreen")
inditogomb.pack(pady=10)

#Ez a leállító gomb
leallitogomb = ctk.CTkButton(app, text="Leállítás", command=leallitas, width=200, height=40, fg_color="red", hover_color="darkred")
leallitogomb.pack(pady=10)



#Ez kell a legvegere, ez miatt fut folyton az ablak
app.mainloop()