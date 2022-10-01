import subprocess, tkinter as tk, pyperclip

def mainToEntryScreen():
    mainMenu.destroy()
    entryMenu.pack()

def getPassword(entryText):
    unfilteredPassword = subprocess.Popen(f'netsh wlan show profile name="{entryText}" key=clear', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    password = unfilteredPassword[unfilteredPassword.find("Key Content            : ") + len("Key Content            : "):unfilteredPassword.rfind("Cost settings")].strip()
    return password

screen = tk.Tk()
screen.title("Wifi Password Rememberer")
screen.geometry("500x600")
screen.resizable(False, False)
screen.config(bg="#999999")
screen.wm_iconbitmap("wifi.ico")
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
x = (screen_width / 2) - (500 / 2)
y = (screen_height / 2) - (600 / 2)
screen.geometry('%dx%d+%d+%d' % (500, 600, x, y))

wifiIcon = tk.PhotoImage(file="wifi.png")
mainMenu = tk.Frame(screen, bg="#999999")
mainMenu.pack()
entryMenu = tk.Frame(screen, bg="#999999")
resultMenu = tk.Frame(screen, bg="#999999")
startMenuLabel = tk.Label(mainMenu, text="Wifi Password Rememberer", font=("Bahnschrift", 20), bg="#999999", fg="#000000", image=wifiIcon, compound="top")
startMenuButton = tk.Button(mainMenu, text="Start", font=("Bahnschrift", 20), bg="#909090", fg="#000000", command=lambda: mainToEntryScreen())
enterLabel = tk.Label(entryMenu, text="Enter your wifi name \n(case doesn't matter):", font=("Bahnschrift", 20), bg="#999999", fg="#000000")
preResultLabel = tk.Label(resultMenu, text=f"Your password is: \n(copied to clipboard)", font=("Bahnschrift", 20), bg="#999999", fg="#000000")
enterEntry = tk.Entry(entryMenu, font=("Bahnschrift", 20), bg="#909090", fg="#000000")
resultLabel = tk.Label(resultMenu, text="invalid", font=("Bahnschrift", 20), bg="#909090", fg="#00ffff")
enterButton = tk.Button(entryMenu, text="Enter", font=("Bahnschrift", 20), bg="#909090", fg="#000000", command=lambda: [pyperclip.copy(getPassword(enterEntry.get())), resultLabel.config(text=getPassword(enterEntry.get())), resultMenu.pack(), entryMenu.destroy()])
resultButton = tk.Button(resultMenu, text="Quit", font=("Bahnschrift", 20), bg="#909090", fg="#000000", command=lambda: screen.destroy())
preResultLabel.pack(pady=50)
resultLabel.pack()
resultButton.pack(pady=50)
enterLabel.pack(pady=50)
enterEntry.pack()
enterButton.pack(pady=50)
startMenuLabel.pack()
startMenuButton.pack(pady=50)
screen.mainloop()