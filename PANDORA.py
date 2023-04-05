                                                            # P.A.N.D.O.R.A
import os
import subprocess

try:
    import pyttsx3                                          
    import datetime
    import speech_recognition as sr
    import wikipedia
    import webbrowser
    import random as r
    import wolframalpha
    import mysql.connector as con
    import ezgmail
    import pyautogui
    import pygame
    from nltk.chat.util import Chat, reflections
    from PIL import ImageTk,Image
    from tkinter import *
    from tkinter import filedialog
    import time
    from selenium import webdriver
    from datetime import datetime,timedelta
    from PyDictionary import PyDictionary
    import math as m
    import webbrowser
    import platform
    import re
    import dictionary2
    from webdriver_manager.chrome import ChromeDriverManager
    from pytube import YouTube
    from pathlib import Path
    import shutil
    
except ImportError:
    directory = os.path.join(os.getcwd(), 'debug.cmd')
    subprocess.call(directory)

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def relative():
    def register():
        try:
            q = e1.get()#user name
            w = e2.get()#email id
            e = ex.get()#relation
            r = ey.get()#gender(M/F)
            t = e3.get()#password
            y = e4.get()#confirm password
            u = e5.get()#mysql password
            if t == y:
                mycon = con.connect(host="localhost",user="root",passwd=u,database="pandora")
                if mycon.is_connected():
                    speak("connection to brain successful")
                cur = mycon.cursor()
                query2 = "insert into credentials values('{}','{}','{}','{}','{}')".format(q,w,r,y,e)
                print(query2)
                cur.execute(query2)
                mycon.commit()
                speak("regisration completed")
                root.destroy()
            else:
                speak("sorry the two passwords entered does not match")
                root.destroy()
                relative()
        except Exception:
            speak("registration failed")
            root.destroy()
    speak("redirecting towards installation process")
    root = Tk()
    root.title("installation")        
    l1 = Label(text = "pandora installation wizard")
    l2 = Label(text = "user name:")
    l3 = Label(text = "email id:")
    lx = Label(text = "relation")
    ly = Label(text = "gender(M/F)")
    l4 = Label(text = "password:")
    l5 = Label(text = "confirm password:")
    l6 = Label(text = "mysql password:")
    l1.grid(column = 1,row = 0)
    l2.grid(column = 0,row = 1)
    l3.grid(column = 0,row = 2)
    lx.grid(column = 0,row = 3)
    ly.grid(column = 0,row = 4)
    l4.grid(column = 0,row = 5)
    l5.grid(column = 0,row = 6)
    l6.grid(column = 0,row = 7)
    e1 = Entry(root,width=30) #user name
    e2 = Entry(root,width=30) #email id
    ex = Entry(root,width=30) #relation with master
    ey = Entry(root,width=10) #gender
    e3 = Entry(root,show="*",width=30) #password
    e4 = Entry(root,show="*",width=30) #confirm password
    e5 = Entry(root,show="*",width=30) #mysql password
    e1.grid(column = 1,row = 1)
    e2.grid(column = 1,row = 2)
    ex.grid(column = 1,row = 3 )
    ey.grid(column = 1,row = 4)
    e3.grid(column = 1,row = 5)
    e4.grid(column = 1,row = 6)
    e5.grid(column = 1,row = 7)
    file = os.path.join(os.getcwd(),'Resources','images','installer.png')
    photo = PhotoImage(file = file)
    file2 = os.path.join(os.getcwd(),'Resources','images','ok.png')
    photo2 = PhotoImage(file = file2)
    root.iconphoto(False,photo)
    b1 = Button(text = "okay",image = photo2,command = register)
    b1.grid(column = 2,row =7)
    root.geometry()
    root.mainloop()

def wishme():
    hr = int(datetime.now().hour)
    if hr >= 0 and hr < 12:
        speak("good morning")
    elif hr >= 12 and hr < 18:
        speak("good afternoon") 
    else:
        speak("good evening")
    speak("hi my name is pandora i am your digital assistant")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language = "en-in")
        print(f"user said:{query}\n")
    except Exception as e:
        speak("sorry sir i did not got that")
        query = pyautogui.password("enter password >>")
    return query

def yourcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        text = font.render("listening...",True,red)
        text.get_rect()
        gameWindow.blit(text,(0,0))
        pygame.display.update()
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        txt = font.render("recognizing...",True,red)
        txt.get_rect()
        file = os.path.join(os.getcwd(),'Resources','images','image2.png')
        arc2 = pygame.image.load(file)
        gameWindow.blit(txt,(0,50))
        gameWindow.blit(arc2,(600,100))
        pygame.display.update()
        query = r.recognize_google(audio,language = "en-in")
    except Exception as e:
        print(e)
        speak("sorry sir i did not got that.")
        query = pyautogui.prompt("command:")
    return query

#----------------------------------------------------------installation process---------------------------------------------------------------------------
def install():
    def createbrain():
        try:
            mycon = con.connect(host="localhost",user="root",passwd=z3)
            if mycon.is_connected():
                print("BODY connected to BRAIN")
            cur = mycon.cursor()
            query = "create database if not exists pandora"
            cur.execute(query)
        except Exception:
            speak("connection to brain failed")
    def credentials():
        global z3
        x = e1.get()
        y = e2.get()
        z = e3.get()
        z1 = ex.get()
        z2 = e4.get()
        z3 = e5.get()
        createbrain()
        try:
            mycon = con.connect(host="localhost",user="root",passwd=z3,database="pandora")
            if mycon.is_connected():
                speak("connection to brain successful")
            cur = mycon.cursor()
            query = "create table if not exists credentials(user_name varchar(30) not null,emailid varchar(40) not null,gender char(1),passwd varchar(30) not null,relation char(25))"
            cur.execute(query)
            query2 = "insert into credentials values('{}','{}','{}','{}','{}')".format(x,y,z1,z,"master")
            cur.execute(query2)
            mycon.commit()
            root.destroy()
        except Exception:
            speak("installation failed")
            quit()

    root = Tk()
    root.title("installation")
    l1 = Label(text = "pandora installation wizard")
    l2 = Label(text = "user name:")
    l3 = Label(text = "email id:")
    lx = Label(text = "gender(M/F)")
    l4 = Label(text = "password:")
    l5 = Label(text = "confirm password:")
    l6 = Label(text = "mysql password:")
    l1.grid(column = 1,row = 0)
    l2.grid(column = 0,row = 1)
    l3.grid(column = 0,row = 2)
    lx.grid(column = 0,row = 3)
    l4.grid(column = 0,row = 4)
    l5.grid(column = 0,row = 5)
    l6.grid(column = 0,row = 6)
    e1 = Entry(root,width=30) #user name
    e2 = Entry(root,width=30) #email id
    ex = Entry(root,width=10) #gender
    e3 = Entry(root,show="*",width=30) #password
    e4 = Entry(root,show="*",width=30) #confirm password
    e5 = Entry(root,show="*",width=30) #mysql password
    e1.grid(column = 1,row = 1)
    e2.grid(column = 1,row = 2)
    ex.grid(column = 1,row = 3)
    e3.grid(column = 1,row = 4)
    e4.grid(column = 1,row = 5)
    e5.grid(column = 1,row = 6)
    file = os.path.join(os.getcwd(),'Resources','images','installer.png')
    photo = PhotoImage(file = file)
    file2 = os.path.join(os.getcwd(),'Resources','images','ok.png')
    photo2 = PhotoImage(file = file2)
    root.iconphoto(False,photo)
    b1 = Button(text = "okay",image = photo2,command = credentials)
    b1.grid(column = 2,row =7)
    root.geometry()
    root.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------getting info about user-------------------------------------------------------------------- 
def getinfo():
    def done():
        global a
        global b
        global m
        global n
        m = e1.get()
        print(m)
        n = e2.get()
        o = e3.get()
        try:
            mycon = con.connect(host="localhost",user="root",passwd=o,database='pandora')
            if mycon.is_connected():
                speak("body connected to brain")
            cur = mycon.cursor()
            query = "select user_name from credentials where user_name='{}'".format(m)
            cur.execute(query)
            a = cur.fetchall()

            cur2 = mycon.cursor()
            query2 = "select passwd from credentials where user_name='{}'".format(m)
            cur2.execute(query2)
            b = cur2.fetchall()
            window.destroy()
        except Exception:
            speak("fetching information from brain failed")
    def forgetpasswd():
        def otp():
            nm = e1.get()
            mypwd = e2.get()
            root.destroy()
            try:
                mycon = con.connect(host="localhost",user='root',passwd=mypwd,database='pandora')
                if mycon.is_connected():
                    speak('connection to brain successful')
                cur = mycon.cursor()
                query = "select emailid from credentials where user_name = '{}'".format(nm)
                cur.execute(query)
                a = cur.fetchall()
                print(a)
                if len(a) == 0:
                    speak("sorry no such user name exists")
                else:
                    usr = a[0][0]
                    string = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
                    otpd = ""
                    ln = len(string)
                    for i in range(6):
                        otpd += string[m.floor(r.random()*ln)]
                    bdy = "your one time password is {}".format(otpd)
                    ezgmail.send(usr,"otp for pandora",bdy)
                    speak("you have recieved an otp on your registered email")
                    cck = pyautogui.prompt("please enter the otp:")
                    if cck == otpd:
                        speak("otp authentified syncronizing with your user_name")
                        nwpwd = pyautogui.password("new password:")
                        nwpwd2 = pyautogui.password("confirm password:")
                        if nwpwd == nwpwd2:
                            try:
                                mycon = con.connect(host="localhost",user="root",passwd=mypwd,database='pandora')
                                if mycon.is_connected():
                                    speak("connection to brain successful")
                                cur = mycon.cursor()
                                query = "update credentials set passwd='{}' where user_name='{}'".format(nwpwd,nm)
                                print(nwpwd)
                                print(usr)
                                print(query)
                                cur.execute(query)
                                mycon.commit()
                                speak("your password has been updated")
                                getinfo()
                            except Exception:
                                speak("connection to brain failed")
                        else:
                            speak("sorry the two passwords does not match")
                            getinfo()
                    else:
                        speak("invalid otp entered")
                        getinfo()
            except Exception:
                speak("sorry connection to brain failed")
        window.destroy()
        root = Tk()
        file = os.path.join(os.getcwd(),'Resources','images','pwd rst.png')
        photo = PhotoImage(file=file)
        root.iconphoto(False,photo)
        root.title("forget password")
        lbl = Label(text="user name:")
        lbl2 = Label(text="mysql passwd:")
        lbl.grid(column=0,row=0)
        lbl2.grid(column=0,row=1)
        e1 = Entry(root,width=30)
        e2 = Entry(root,width=30)
        e1.grid(column=1,row=0)
        e2.grid(column=1,row=1)
        btn = Button(root,text="reset",image = photo,command=otp)
        btn.grid(column=2,row=2)
        root.geometry("400x105")
        root.mainloop()
    window = Tk()
    window.title("credentials")
    file_ = os.path.join(os.getcwd(),'orbit','login.png')
    #icon_photo = PhotoImage(file=r"C:\Users\SHAURYA\Desktop\PANDORA\orbit\login.png")
    icon_photo = PhotoImage(file=file_)
    window.iconphoto(False, icon_photo)
    file = os.path.join(os.getcwd(),'Resources','images','ok.png')
    photo = PhotoImage(file = file)
    file2 = os.path.join(os.getcwd(),'Resources','images','forget pwd.png')
    photo2 = PhotoImage(file = file2)
    lbl = Label(text="user name:")
    lbl2 = Label(text="password:")
    lbl3 = Label(text="mysql password:")
    lbl.grid(column=0,row=0)
    lbl2.grid(column=0,row=1)
    lbl3.grid(column=0,row=2)
    e1 = Entry(window,width=30)
    e2 = Entry(window,width=30)
    e3 = Entry(window,width=30)
    e1.grid(column=1,row=0)
    e2.grid(column=1,row=1)
    e3.grid(column=1,row=2)
    b1 = Button(text="okay",image=photo,command=done)# create function done 
    b2 = Button(text="forget password",image=photo2,command=forgetpasswd)# create function forgetpasswd
    b1.grid(column=0,row=3)
    b2.grid(column=1,row=3)
    window.geometry("400x200")
    window.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------sending email and reading email------------------------------------------------------------------
#variables for email
#functions for email
def sendemail():
    attach = []
    ccr = []
    def browse():
        window.filename=filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("pdf files", "*.pdf"),("all files","*")))
        lbl = Label(window,text=window.filename)
        text1 = lbl.cget("text")
        attach.append(text1)
    def browseimage():
        window.filename=filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("png files", "*.png"),("jpeg files","*.jpg"),("all files","*")))
        lbl = Label(window,text=window.filename)
        text2 = lbl.cget("text")
        attach.append(text2)
    def cc():
        def done():
            recipient = entry.get()
            ccr.append(recipient)
        root = Tk()
        root.title("cc")
        label = Label(root,text="recipient name:")
        label.grid(column=0,row=0)
        entry = Entry(root,width=30)
        entry.grid(column=0,row=1)
        button = Button(root,text="ok",command=done)
        button.grid(column=0,row=2)
        root.geometry("200x200")
        root.mainloop()
    def send():
        a = txt.get()
        b = txt2.get()
        c = txt3.get(1.0, END+"-1c")
        if not ccr:
            ezgmail.send(a,b,c,attach)
        else:
            ezgmail.send(a,b,c,attach)
            ezgmail.send(ccr[0],b,c,attach)
        y = "email has been send {}".format(sal)
        speak(y)
        pyautogui.alert("email send")
        window.destroy()
    window = Tk()
    window.title("email")
    file1 = os.path.join(os.getcwd(),'Resources','images','add file.png')
    photo1 = PhotoImage(file = file1)
    file2 = os.path.join(os.getcwd(),'Resources','images','add image.png')
    photo2 = PhotoImage(file = file2)
    file3 = os.path.join(os.getcwd(),'Resources','images','email.png')
    photo3 = PhotoImage(file = file3)
    file4 = os.path.join(os.getcwd(),'Resources','images','ok.png')
    photo4 = PhotoImage(file = file4)
    file5 = os.path.join(os.getcwd(),'Resources','images','cc.png')
    photo5 = PhotoImage(file = file5)
    window.iconphoto(False,photo3)
    x = Label(window,text="recipient email address:")
    x.grid(column=0,row=0)
    txt = Entry(window,width=30)
    txt.grid(column=0,row=1)
    y = Label(window,text="subject line:")
    y.grid(column=0,row=2)
    txt2 = Entry(window,width=35)
    txt2.grid(column=0,row=3)
    z = Label(window,text="body:")
    z.grid(column=0,row=4)
    txt3 = Text(window,height=10,width=50)
    txt3.grid(column=0,row=5)
    btn = Button(window,text="add attachment",image = photo1,command = browse)
    btn.grid(column=0,row=6)
    btn2 = Button(window,text="add attachment",image = photo2,command = browseimage)
    btn2.grid(column=0,row=7)
    btn3 = Button(window,text="cc",image = photo5,command=cc)
    btn3.grid(column=0,row=8)
    btn5 = Button(window,text="ok",image = photo4,command=send)
    btn5.grid(column=0,row=9)
    window.geometry("400x450")
    window.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------setting alarm--------------------------------------------------------------------------------------
def callalarm():
    def setalarm():
        a = e1.get()
        b = e2.get()
        c = e3.get()
        if len(a) == 0:
            a = 0
        if len(b) == 0:
            b = 0
        if len(c) == 0:
            c = 0 
        x = int(a)
        y = int(b)
        z = int(c)
        curt = time.strftime("%H:%M:%S")
        alt = (datetime.now() + timedelta(hours=x) + timedelta(minutes=y) + timedelta(seconds=z)).strftime('%H:%M:%S')
        while curt != alt:
            curt = time.strftime("%H:%M:%S")
            time.sleep(1)
            if curt == alt:
                file = os.path.join(os.getcwd(),'Resources','music')
                l = os.listdir(file)
                music_dir = file
                os.startfile(os.path.join(music_dir,l[0]))
    def dismiss():
        os.system('TASKKILL /F /IM alarm.mp3')
        root.destroy()
    global e1
    global e2
    global e3
    root = Tk()
    root.title("ALARM")
    file = os.path.join(os.getcwd(),'Resources','images','alarm.png')
    photo = PhotoImage(file=file)
    file2 = os.path.join(os.getcwd(),'Resources','images','ok.png')
    photo2 = PhotoImage(file=file2)
    root.iconphoto(False,photo)
    l1 = Label(text="HOURS:")
    l2 = Label(text="MINUTES:")
    l3 = Label(text="SECONDS:")
    l1.grid(column=0,row=0)
    l2.grid(column=0,row=1)
    l3.grid(column=0,row=2)
    e1 = Entry(root)
    e2 = Entry(root)
    e3 = Entry(root)
    e1.grid(column=1,row =0)
    e2.grid(column=1,row =1)
    e3.grid(column=1,row =2)
    b1 = Button(root,text="save",image = photo2,command=setalarm)
    b2 = Button(root,text="dismiss",command = dismiss)
    b1.grid(column = 2 ,row =3)
    b2.grid(column = 3,row = 3)
    root.geometry("400x400")
    root.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def gameloop():
    def master():
        try:
            global mst
            global gndr
            global gndr2
            myrealcon = con.connect(host="localhost",user="root",passwd=sqlpwd,database="pandora")
            cur = myrealcon.cursor()
            query = "select user_name from credentials where user_name='{}'".format(m)
            print(query)
            cur.execute(query)
            data = cur.fetchall()
            mst = data[0][0]

            cur2 = myrealcon.cursor()
            query2 = "select gender from credentials where user_name='{}'".format(m)
            cur2.execute(query2)
            data2 = cur2.fetchall()
            gndr = data2[0][0]
            print(mst,gndr)
            if gndr == "M":
                gndr2="Mister"
            if gndr == "F":
                gndr2="Mistress"
            print(gndr2)
        except Exception as g:
            print(g)
            speak("connection to brain failed")
            quit()
    master()
    global sal
    if gndr2 == "Mister":
        sal = "sir"
    if gndr2 == "Mistress":
        sal = "ma'am"
    speak("please give your command")
    query = yourcommand().lower().strip() #yourcommand() rather than takecommand()
    print(query)
    if "introduce" in query:
        x = "hi {} {} i am pandora your personal virtual assistant".format(gndr2,mst)
        y = "pandora stands for python automated newly developed and organised requisite assistant"
        speak(x)
        speak(y)
        print(x)
    elif "processor" in query:
        x = platform.processor()
        y = "{} my processor is".format(sal)
        speak(x)
    elif "wikipedia" in query:
        print(sal)
        x = "{} searching wikipedia...".format(sal)
        print(x)
        speak(x)
        query = query.replace("wikipedia",'')
        results = wikipedia.summary(query,sentences=2)
        y = "{} according to wikipedia".format(sal)                                                          
        speak(y)
        speak(results)
    elif "calculate" in query:
        app_id = "E46YXW-T5LG6RT7K7"
        client = wolframalpha.Client(app_id)
        indx = query.split().index("calculate")
        query = query.split()[indx+1:]
        res = client.query(' '.join(query))
        ans = next(res.results).text
        x = "{} the answer is".format(sal)
        speak(sal+ans)
    elif "send email" in query:
        x = "yes {}".format(sal)
        speak(x)
        speak("opening the interface for email")
        sendemail()
    elif "read email" in query:
        x = "speaking emails for you {}".format(sal) #work on email reading for only specified subject sender or body
        speak(x)
        unread = ezgmail.unread()
        if len(unread) != 0:
            for i in range(len(unread)-1):
                speak(str(unread[i]).strip('<>'))
            y = "you are all caught up now {}".format(sal)
            speak(y)
        else:
            y = "you are all caught up {}".format(sal)
            speak(y)
    
    elif "play music" in query:
        x = "{} do you want to play specific music or want me play randomly?".format(sal)
        speak(x)
        command = yourcommand().lower()
        if "specific" in command:  #playing specific music
            speak("please give the name of music")
            mp = pyautogui.prompt("Music name-")
            l = os.listdir(r"C:\\Users\SHAURYA\Music\music")
            for i in range(len(l)-1):
                if mp in l[i].lower():
                    music_dir = r"C:\\Users\SHAURYA\Music\music"
                    os.startfile(os.path.join(music_dir,l[i]))
                    break
            else:
                speak("specified song not in your music directory") # checking the music to play music on spotify or not
        elif "play random" in command: # playing random music by command
            speak("sir playing a music randomly")
            music_dir = r"C:\\Users\SHAURYA\Music\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[r.randint(1,len(songs)-1)]))
        else: 
            speak("sir since you have not speacified music i am playing a random one") #playing random music because not specified or command to random play
            music_dir = r"C:\\Users\SHAURYA\Music\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[r.randint(1,len(songs)-1)]))
    
    elif "spotify" in query:
        song = query.replace('spotify','')
        speak("opening spotify for you")
        os.system('c:\windows\System32\taskkill.exe /f /im spotify.exe')
        os.system('spotify.exe')
        time.sleep(7)
        file = os.path.join(os.getcwd(),'Resources','images','spotify.png')
        spotify = pyautogui.locateCenterOnScreen(file,grayscale=False)
        pyautogui.click(file)
        pyautogui.write(song)
        pyautogui.press('enter')
        time.sleep(8)
        pyautogui.click(379,260)

    elif "google" in query:
        speak("opening google")
        query = query.replace("google",'')
        try:
            driver = webdriver.Chrome()#ChromeDriverManager().install()
            driver.maximize_window()
            driver.get("https://google.com")
            time.sleep(1)
            file = os.path.join(os.getcwd(),'Resources','images','google.png')
            google = pyautogui.locateOnScreen(file)
            pyautogui.write(query)
            pyautogui.press("enter")
        except Exception:
            speak('sorry sir the current version of google driver is not supported')
            speak('installing new driver')
            driver = webdriver.Chrome(ChromeDriverManager().install())  # ChromeDriverManager().install()
            speak('driver installed')
            driver_version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
            usr_path = os.path.join(str(Path.home()),'.wdm','drivers','chromedriver','win32',driver_version,'chromedriver.exe')
            shutil.copy(usr_path,os.getcwd())
            speak('driver pasted in your directory')
            driver.maximize_window()
            driver.get("https://google.com")
            time.sleep(1)
            file = os.path.join(os.getcwd(), 'Resources','images', 'google.png')
            google = pyautogui.locateOnScreen(file)
            pyautogui.write(query)
            pyautogui.press("enter")
                
    elif "youtube" in query:
        try:
            speak("opening youtube")
            query = query.replace("youtube",'')
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://youtube.com")
            time.sleep(1)
            search_box = driver.find_element_by_xpath('//*[@id="search"]')
            search_box.send_keys(query)
            search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
            search_button.click()
        except Exception:
            speak('sorry sir the current version of google driver is not supported')
            speak('installing new driver')
            # ChromeDriverManager().install()
            driver = webdriver.Chrome(ChromeDriverManager().install())
            speak('driver installed')
            driver_version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
            usr_path = os.path.join(str(Path.home()), '.wdm', 'drivers','chromedriver', 'win32', driver_version, 'chromedriver.exe')
            shutil.copy(usr_path, os.getcwd())
            speak('driver pasted in your directory')
            driver.maximize_window()
            driver.get("https://youtube.com")
            search_box = driver.find_element_by_xpath('//*[@id="search"]')
            search_box.send_keys(query)
            search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
            search_button.click()

    elif "the time" in query:
        curttime = datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {curttime}")

    elif "alarm" in query:
        speak("opening interface for alarm")
        callalarm()
    elif "increase volume" in query: #increase volume by 2
        speak("increasing volume")
        pyautogui.press("volumeup")
    elif "decrease volume" in query:
        speak("decreasing volume")
        pyautogui.press("volumedown")
    elif "mute volume" in query:
        speak("muting volume")
        y = "{} you would not be able to listen to me while volume is muted".format(sal)
        speak(y)
        pyautogui.press("volumemute")
    elif "register" in query:
        speak("opening registration portal")
        relative()
    elif "my name is" in query:
        x = re.search(r"^my name is",query)
        y = query.split(x.group())
        for i in range(len(y)):
            if len(y[i]) != 0:
                namae = y[i].strip()
        mycon = con.connect(host="localhost",user="root",passwd=sqlpwd,database="pandora")
        if mycon.is_connected():
            speak("oh")
        cur = mycon.cursor()
        query = "select user_name from credentials"
        cur.execute(query)
        data2 = cur.fetchall()
        q = len(data2)
        for i in range(q):
            if namae in (data2[i]):
                print(namae)
                if namae == data2[0][0]:
                    speak("sir you dont need to tell me your name you are my master after all")
                    break
                else:
                    x = "hello {} how are you doing , ask me to do any task".format(data2[i])
                    speak(x)
                    break
        else:
            speak('sorry sir i do not recognize you')
            x = "if you register i will surely recall you can ask {} {} to register you".format(gndr2,mst)
            speak(x)
    elif "shutdown" in query:
        x = "{} you are about to shutdown".format(sal)
        y = "shutdown process will start in next 5 seconds"
        speak(x)
        speak(y)
        time.sleep(5)
        os.system("shutdown/s")
    elif "restart" in query:
        x = "{} you are about to restart".format(sal)
        y = "restart process will start in next 5 seconds"
        speak(x)
        speak(y)
        time.sleep(5)
        os.system("shutdown/r")
    elif "sleep" in query:
        x = "{} sleep mode is about to start".format(sal)
        y = "you won't be able to use me until then"
        z = "sleep mode will start in next 5 seconds"
        speak(x)
        speak(y)
        speak(z)
        time.sleep(5)
        os.system("RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0")
    elif "meaning of" in query:
        dictionary = PyDictionary()
        query = query.replace("meaning of"," ").strip()
        x = dictionary.meaning(query)
        y = "{} the meaning of the requested word is".format(sal)
        speak(y)
        speak(x)
    elif "debugging" in query:
        speak('starting debugging process')
        directory = os.path.join(os.getcwd(), 'debug.cmd')
        subprocess.call(directory)
        speak('debugging compelete')
    elif "dictionary" in query:
        speak("opening dictionary program")
        dictionary2.main()
    elif 'download' in query:
        speak('opening youtube video downloading portal')
        link = pyautogui.prompt('Please enter video url:')
        video = YouTube(link)
        stream = video.streams.get_highest_resolution()
        stream.download()
        speak('Downloading completed')
        

if __name__ == "__main__":
    speak('please enter your my sql password')
    sqlpwd = pyautogui.password("enter mysql password>>")
    print(sqlpwd)
    try:
        mycon = con.connect(host="localhost",user="root",passwd=sqlpwd)
        if mycon.is_connected():
            speak("connection to brain successful")
            cur = mycon.cursor()
            query = "show databases"
            cur.execute(query)
            data = cur.fetchall()
            print(data)
            q = len(data)
            print(q)
            for i in range(q):
                if "pandora" in (data[i]):
                    speak("connected to the processing unit")
                    q -= 1
                    break
            else:
                speak("opening installation wizard")
                install()
                try:
                    mycon = con.connect(host="localhost",user="root",passwd=sqlpwd,database="pandora")
                    cur = mycon.cursor()
                    query = "select * from credentials"
                    cur.execute(query)
                    y = tuple()
                    for x in cur:
                        y = y + (x,)
                    crd = list(y)
                    print(crd)
                    if len(crd) == 0:
                        speak("installation incomplete")
                        speak("credentials unsaved")
                        speak("you wont be able to use pandora until you compelete installation")
                        quit()
                except Exception as e:
                    speak("connection to brain failed")
                    
                    
    except Exception as f:
        speak("connection to brain failed")
         
    getinfo()
    try:
        if m in a[0]:
            if n in b[0]:
                try: 
                    speak("initialising")
                    speak("loading interface")
                    x = pygame.init()
                    blue = (0,0,225,225)
                    white = (225,225,225,225)
                    red = (225,0,0,225)
                    black = (0,0,0,225)
                    gameWindow = pygame.display.set_mode((1920,1020)) #game window size
                    pygame.display.set_caption("PANDORA")
                    exit_game = False
                    file = os.path.join(os.getcwd(),'Resources','images','image.png')
                    arc = pygame.image.load(file)
                    file2 = os.path.join(os.getcwd(),'Resources','images','jarvis.png')
                    font = pygame.font.Font("freesansbold.ttf", 50)
                    icon = pygame.image.load(file2)
                    file3 = os.path.join(os.getcwd(),'Resources','images','background.jpg')
                    bg = pygame.image.load(file3)
                    pygame.display.set_icon(icon)
                    gameWindow.blit(bg,(0,0))
                    gameWindow.blit(arc,(600,100))
                    pygame.display.update()
                    wishme()
                    while not exit_game:
                        pygame.display.set_icon(icon)
                        gameWindow.blit(bg,(0,0))
                        gameWindow.blit(arc,(600,100)) #arc coordinates
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit_game = True    
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    gameloop()
                except Exception as j:
                    speak("sorry an error occured")
                    print(j)
            else:
                speak("incorrect password entered")
                quit()
        else:
            speak("incorrect username entered")
            quit()
    except Exception as k:
        speak("Access denied check whether any entry field(s) is/are empty")
        print(k)