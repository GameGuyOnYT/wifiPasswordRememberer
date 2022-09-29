import subprocess
from colors import colors

while True:
    wifiName = input(colors.OKCYAN + "Enter your wifi name (case doesn't matter): " + colors.ENDC)
    str1 = subprocess.Popen(f'netsh wlan show profile name="{wifiName}" key=clear',
                            shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    str2 = str1[
        str1.find("Key Content            : ") + len("Key Content            : "):str1.rfind("Cost settings")].strip()
    if not str2.__contains__("tem."):
        print(colors.OKBLUE + 'Password: ' + colors.OKGREEN + str2 + colors.ENDC)
        quit()
    elif str2.__contains__("tem."):
        print(colors.FAIL + "This network is invalid. Maybe a typo?\n" + colors.ENDC)