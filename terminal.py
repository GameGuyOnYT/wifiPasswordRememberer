import subprocess, colors, pyperclip

while True:
    wifiName = input(colors.colors.OKCYAN + "Enter your wifi name (case doesn't matter): " + colors.colors.ENDC)
    str1 = subprocess.Popen(f'netsh wlan show profile name="{wifiName}" key=clear', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    str2 = str1[str1.find("Key Content            : ") + len("Key Content            : "):str1.rfind("Cost settings")].strip()
    if not str2.__contains__("tem."):
        print(colors.colors.OKBLUE + 'Password: ' + colors.colors.OKGREEN + str2 + colors.colors.ENDC)
        pyperclip.copy(str2)
        quit()
    else:
        print(colors.colors.FAIL + "This network is invalid. Maybe a typo?\n" + colors.colors.ENDC)
