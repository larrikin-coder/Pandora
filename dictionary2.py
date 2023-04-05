#importing modules

import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import ttk
from PyDictionary import PyDictionary
import mysql.connector as con
import pyautogui
from PIL import ImageTk,Image
import ezgmail
import random as r
import pytesseract
import math
import os
import pyttsx3

#-------------------------------------------------------speak engine----------------------------------------------------------------------------#
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#-------------------------------------------------installation wizard--------------------------------------------------------------------------#
def install():
    def createbrain():
        mycon = con.connect(host="localhost",user="root",passwd=z3)
        if mycon.is_connected():
            speak("BODY connected to BRAIN")
        cur = mycon.cursor()
        query = "create database if not exists bibliotheca"
        cur.execute(query)

    def credentials():
        global z3
        x = e1.get()#name
        y = e2.get()#email id
        z = e3.get()#password
        z1 = ex.get()#gender
        z2 = e4.get()#confirm password
        z3 = e5.get()#mysql password
        print(x)
        print(y)
        print(z1)
        print(z2)
        print(z3)
        createbrain()
        mycon = con.connect(host="localhost",user="root",passwd=z3,database="bibliotheca")
        if mycon.is_connected():
            pass
        cur = mycon.cursor()
        query = "create table if not exists credentials(user_name varchar(30) not null,emailid varchar(40) not null,gender char(1),passwd varchar(30) not null)"
        cur.execute(query)
        query2 = "insert into credentials values('{}','{}','{}','{}')".format(x,y,z1,z)
        print(query2)
        cur.execute(query2)
        mycon.commit()
        root.destroy()

    root = tk.Tk()
    root.title("installation")
    l1 = tk.Label(text = "Bibliotheca installation wizard")
    l2 = tk.Label(text = "user name:")
    l3 = tk.Label(text = "email id:")
    lx = tk.Label(text = "gender(M/F)")
    l4 = tk.Label(text = "password:")
    l5 = tk.Label(text = "confirm password:")
    l6 = tk.Label(text = "mysql password:")
    l1.grid(column = 1,row = 0)
    l2.grid(column = 0,row = 1)
    l3.grid(column = 0,row = 2)
    lx.grid(column = 0,row = 3)
    l4.grid(column = 0,row = 4)
    l5.grid(column = 0,row = 5)
    l6.grid(column = 0,row = 6)
    e1 = tk.Entry(root,width=30) #user name
    e2 = tk.Entry(root,width=30) #email id
    ex = tk.Entry(root,width=10) #gender
    e3 = tk.Entry(root,show="*",width=30) #password
    e4 = tk.Entry(root,show="*",width=30) #confirm password
    e5 = tk.Entry(root,show="*",width=30) #mysql password
    e1.grid(column = 1,row = 1)
    e2.grid(column = 1,row = 2)
    ex.grid(column = 1,row = 3)
    e3.grid(column = 1,row = 4)
    e4.grid(column = 1,row = 5)
    e5.grid(column = 1,row = 6)
    file = os.path.join(os.getcwd(),'orbit','installer.png')
    photo = PhotoImage(file = file)
    file2 = os.path.join(os.getcwd(),'orbit','ok.png')
    photo2 = PhotoImage(file = file2)
    root.iconphoto(False,photo)
    ttk.Button(text = "okay",image = photo2,command = credentials).grid(column = 2,row =7)
    root.geometry()
    root.mainloop()
#------------------------------------------------getting user info-----------------------------------------------------------------------------
def getinfo():
    def done():
        global a
        global b
        global m
        global n
        m = e1.get()#username
        print(m)
        n = e2.get()#password
        o = e3.get()#mysql password
        try:
            mycon = con.connect(host="localhost",user="root",passwd=o,database='bibliotheca')
            if mycon.is_connected():
                print("body connected to brain")
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
            print("fetching information from brain failed brain failed")
    def forgetpasswd():
        def otp():
            nm = e1.get()
            mypwd = e2.get()
            root.destroy()
            try:
                mycon = con.connect(host="localhost",user='root',passwd=mypwd,database='bibliotheca')
                if mycon.is_connected():
                    print('connection to brain successful')
                cur = mycon.cursor()
                query = "select emailid from credentials where user_name = '{}'".format(nm)
                cur.execute(query)
                a = cur.fetchall()
                print(a)
                if len(a) == 0:
                    speak("sorry no such user name exists")
                    pyautogui.alert("sorry no such user name exists","Attention!")
                else:
                    usr = a[0][0]
                    string = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
                    otpd = ""
                    ln = len(string)
                    for i in range(6):
                        otpd += string[math.floor(r.random()*ln)]
                    bdy = "your one time password is {}".format(otpd)
                    ezgmail.send(usr,"otp for bibliotheca",bdy)
                    speak("you have recieved an otp on your registered email")
                    pyautogui.alert("you have recieved an otp on your registered email",'Message')
                    cck = pyautogui.prompt("please enter the otp:")
                    if cck == otpd:
                        speak("otp authentified syncronizing with your user_name")
                        pyautogui.alert("otp authentified syncronizing with your user_name","Message")
                        nwpwd = pyautogui.password("new password:")
                        nwpwd2 = pyautogui.password("confirm password:")
                        if nwpwd == nwpwd2:
                            try:
                                mycon = con.connect(host="localhost",user="root",passwd=mypwd,database='bibliotheca')
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
                                pyautogui.alert("your password has been updated","Message")
                                getinfo()
                            except Exception:
                                speak("connection to brain failed")
                                pyautogui.alert("connection to brain failed","Attention!")
                        else:
                            pyautogui.alert("sorry the two passwords does not match","Attention!")
                            getinfo()
                    else:
                        speak("invalid otp entered")
                        pyautogui.alert("invalid otp entered","Attention!")
                        getinfo()
            except Exception:
                speak("sorry connection to brain failed")
                pyautogui.alert("sorry connection to brain failed","Attention!")
        window.destroy()
        root = tk.Tk()
        file = os.path.join(os.getcwd(),'orbit','pwd rst.png')
        photo = tk.PhotoImage(file=file)
        root.iconphoto(False,photo)
        root.title("forget password")
        lbl = tk.Label(text="user name:")
        lbl2 = tk.Label(text="mysql passwd:")
        lbl.grid(column=0,row=0)
        lbl2.grid(column=0,row=1)
        e1 = tk.Entry(root,width=30)
        e2 = tk.Entry(root,width=30)
        e1.grid(column=1,row=0)
        e2.grid(column=1,row=1)
        btn = tk.Button(root,text="reset",image = photo,command=otp)
        btn.grid(column=2,row=2)
        root.geometry("400x105")
        root.mainloop()
    window = tk.Tk()
    window.title("credentials")
    #add icon photo for getinfo()
    file_ = os.path.join(os.getcwd(),'orbit','login.png')
    #icon_photo = tk.PhotoImage(file=r"C:\Users\SHAURYA\Desktop\PANDORA\orbit\login.png")
    icon_photo = tk.PhotoImage(file=file_)
    window.iconphoto(False, icon_photo)
    file = os.path.join(os.getcwd(),'orbit','ok.png')
    photo = tk.PhotoImage(file = file)
    file2 = os.path.join(os.getcwd(),'orbit','forget pwd.png')
    photo2 = tk.PhotoImage(file = file2)
    lbl = tk.Label(text="user name:")
    lbl2 = tk.Label(text="password:")
    lbl3 = tk.Label(text="mysql password:")
    lbl.grid(column=0,row=0)
    lbl2.grid(column=0,row=1,pady = 5)
    lbl3.grid(column=0,row=2,pady = 5)
    e1 = tk.Entry(window,width=30)#username
    e2 = tk.Entry(window,width=30)#password
    e3 = tk.Entry(window,width=30)#mysql password
    e1.grid(column=1,row=0)
    e2.grid(column=1,row=1,pady = 5)
    e3.grid(column=1,row=2,pady = 5)
    b1 = tk.Button(text="okay",image=photo,command=done)# create function done
    b2 = tk.Button(text="forget password",image=photo2,command=forgetpasswd)# create function forgetpasswd
    b1.grid(column=0,row=3,pady = 5,sticky = 'w')
    b2.grid(column=1,row=3,pady = 5,sticky = 'e')
    window.geometry("400x200")
    window.mainloop()

#---------------------------------------------------creating directory for offline search-----------------------------------------------------#
def dir_mkr():
    dir=os.path.join(os.getcwd(),m)
    if not os.path.exists(dir):
        os.makedirs(dir)
        dict_dir = os.path.join(dir,'dictionary')
        os.makedirs(dict_dir)
        seman_dir = os.path.join(dir,'semantics')
        os.makedirs(seman_dir)
        ant_dir = os.path.join(seman_dir,'antonyms')
        os.makedirs(ant_dir)
        syn_dir = os.path.join(seman_dir,'synonyms')
        os.makedirs(syn_dir)

#----------------------------------------------------fuctions for bibliotheca-----------------------------------------------------------------#
def Button_dict():
    def find():
        try:
            query = e1.get().strip()
            dictionary = PyDictionary()
            meaning = dictionary.meaning(query)
            title = "meaning of {}".format(query)
            speak(meaning)
            pyautogui.alert(meaning,title)
            # making a .txt file
            if len(meaning) != 0:
                file_name = "{}.txt".format(query)
                directory = os.path.join(os.getcwd(),m,'dictionary',file_name)
                myfile = open(directory,'w+')# read and write file mode used
                x = meaning.keys()
                for i in x:
                    myfile.write(i+'\n')
                    myfile.flush()
                y = meaning.values()
                for j in y:
                    for _ in j:
                        myfile.write(_+'\n')
                        myfile.flush()
                myfile.close()

        except Exception as e:
            print(e)

    def main_menu():
        window.destroy()
        main_frame()

    root.destroy()
    speak("opening dictionary window")
    window = tk.Tk()
    window.title("DICTIONARY")
    file = os.path.join(os.getcwd(),'orbit','dictionary.png')
    photo = PhotoImage(file = file)
    window.iconphoto(False,photo)
    ttk.Label(window,text = "DICTIONARY").grid(column = 2,row = 0)# ttk.Label(window, text = "Select the Month :",font = ("Times New Roman", 10)).grid(column = 0,row = 15, padx = 10, pady = 25)
    ttk.Label(window,text = "WORD-").grid(column = 1,row = 2,pady = 10)
    e1 = tk.Entry(window)
    e1.grid(column = 2,row = 2,pady = 10)
    ttk.Button(window,text="FIND",command=find).grid(column = 1,row = 4,pady = 10)#to make a def for finding meaning
    ttk.Button(window,text="MAIN MENU",command=main_menu).grid(column = 3,row = 4,pady = 10)#to quit the frame
    window.geometry("360x150")
    window.mainloop()

def convert():
    def cmd(event):
        global lang
        lang = n.get()
    def find():
        try:
            if lang == "Languages":
                pyautogui.alert("No language selected","Attention!")
            if lang == "English":
                query = e1.get().strip()#english word
                dictionary = PyDictionary()
                translate = dictionary.translate(query,'en')
                title = "{} word in English".format(query)
                spk = "{} is {}".format(title,translate)
                speak(spk)
                pyautogui.alert(translate,title)
            else:
                d1 = {'Spanish':'es','Hindi':'hi'}
                dictionary = PyDictionary()
                language = d1.get(lang)#language to be converted in
                print(language)
                word = e1.get().strip()#word
                print(word)
                trans_wrd = dictionary.translate(word,language)
                print(trans_wrd)
                title = "{} word in {}".format(word,lang)
                print(title)
                spk = "{} is {}".format(title,trans_wrd)
                speak(spk)
                pyautogui.alert(trans_wrd,title)
        except Exception as e:
            print(e)
    def upload_photo():
        speak("please select the image")
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        window.filename=filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("png files", "*.png"),("jpeg files","*.jpg"),("all files","*")))
        lbl = tk.Label(window,text=window.filename)
        directory = lbl.cget("text")
        x = (pytesseract.image_to_string(directory))
        if lang == "English":
            dictionary = PyDictionary()
            translate = dictionary.translate(x,'en')
            title = "{} word in {}".format(x,lang)
            spk = "{} is {}".format(title,translate)
            speak(spk)
            pyautogui.alert(translate,title)
            
        else:
            d1 = {'Spanish':'es','Hindi':'hi'}
            language = d1.get(lang)
            dictionary = PyDictionary()
            translate = dictionary.translate(x,language)
            title = "{} word in {}".format(x,lang)
            spk = "{} is {}".format(title,translate)
            speak(spk)
            pyautogui.alert(translate,title)
    def main_menu():
        window.destroy()
        main_frame()

    root.destroy()
    speak("opening Convert English Words to preferred Languages window")
    window = tk.Tk()
    window.title("Convert English Words to preferred Languages")
    photo = PhotoImage(file = r"C:\Users\SHAURYA\Desktop\PANDORA\orbit\dictionary.png")
    window.iconphoto(False,photo)
    ttk.Label(window,text = "Convert English Words to preferred Languages").grid(column = 1,row = 0)
    ttk.Label(window,text = "English Word-").grid(column = 0,row = 4,pady = 10)
    e1 = ttk.Entry(window)
    e1.grid(column = 1,row = 4,pady = 10)
    n = tk.StringVar()
    lang_combo = ttk.Combobox(window,width = 20,textvariable = n)
    lang_combo.bind('<<ComboboxSelected>>',cmd)
    lang_combo['values'] = ('Languages','English','Spanish','Hindi')
    lang_combo.grid(column = 2,row = 4,pady = 10)
    lang_combo.current(0)# default value of language
    ttk.Button(window,text="FIND",command=find).grid(column = 0,row = 7,pady = 10)#pady
    ttk.Button(window,text="UPLOAD PHOTO",command=upload_photo).grid(column = 1,row = 7,pady = 10,sticky = 'e')#pady
    ttk.Button(window, text="MAIN MENU", command=main_menu).grid(column = 2,row = 7,pady = 10,sticky ='e')#pady
    window.geometry("600x150")
    window.mainloop()

def semantic():
    def antonym():
        word = e1.get().strip()
        dictionary = PyDictionary()
        ant_wrd = dictionary.antonym(word)
        if len(word) == 0:
            speak("word text field found empty")
            pyautogui.alert("Word Text field found empty","ATTENTION!")
        elif ant_wrd == None:
            x = "{} word does not have any Antonyms".format(word)
            speak(x)
            pyautogui.alert(x,"ATTENTION!")
        elif len(ant_wrd) > 1:
            title = "Antonyms of word {}".format(word)
            spk = "{} is {}".format(title,ant_wrd)
            speak(spk)
            pyautogui.alert(ant_wrd,title)
        elif len(ant_wrd) == 1:
            title = "Antonym of word {}".format(word)
            spk = "{} is {}".format(title,ant_wrd)
            speak(spk)
            pyautogui.alert(ant_wrd,title)
        # making a .txt file
        if len(ant_wrd) != 0:
            file_name = "{}.txt".format(word)
            directory = os.path.join(os.getcwd(),m,'semantics','antonyms',file_name)
            myfile = open(directory,'w+')# read and write file mode used
            new_lst = []
            for _ in ant_wrd:
                new_lst.append(_ + '\n')
            myfile.writelines(new_lst)
            myfile.flush()
            myfile.close()
    def synonym():
        word = e1.get().strip()
        dictionary = PyDictionary()
        syn_wrd = dictionary.synonym(word)
        if len(word) == 0:
            speak("word text field found empty")
            pyautogui.alert("Word Text field found empty","ATTENTION!")
        elif syn_wrd == None:
            x = "{} word does not have any Antonyms".format(word)
            speak(x)
            pyautogui.alert(x,"ATTENTION!")
        elif len(syn_wrd) > 1:
            title = "synonyms of word {}".format(word)
            spk = "{} is {}".format(title,syn_wrd)
            speak(spk)
            pyautogui.alert(syn_wrd,title)
        elif len(syn_wrd) == 1:
            title = "synonym of word {}".format(word)
            spk = "{} is {}".format(title,syn_wrd)
            speak(spk)
            pyautogui.alert(syn_wrd,title)
        # making a .txt file
        if len(syn_wrd) != 0:
            file_name = "{}.txt".format(word)
            directory = os.path.join(os.getcwd(),m,'semantics','synonyms',file_name)
            myfile = open(directory,'w+')# read and write file mode used
            new_lst = []
            for _ in syn_wrd:
                new_lst.append(_ + '\n')
            myfile.writelines(new_lst)
            myfile.flush()
            myfile.close()
    def main_menu():
        window.destroy()
        main_frame()
    root.destroy()
    speak("opening semantics window")
    window = tk.Tk()
    window.title("Semantics")
    file = os.path.join(os.getcwd(),'orbit','dictionary.png')
    photo = PhotoImage(file = file)
    window.iconphoto(False,photo)
    ttk.Label(window,text="SEMANTICS").grid(column = 2,row = 0)
    ttk.Label(window,text="Word-").grid(column = 1,row = 2,pady = 10)
    e1 = ttk.Entry(window)
    e1.grid(column = 2,row = 2,pady = 10)
    ttk.Button(window,text="Antonym",command =antonym).grid(column = 0,row = 4,pady = 10)
    ttk.Button(window,text="Main Menu",command =main_menu).grid(column = 2,row = 4,pady = 10)
    ttk.Button(window,text="Synonym",command =synonym).grid(column = 3,row = 4,pady = 10)
    window.geometry("410x150")
    window.mainloop()

#--------------------------------------------------------------------settings-------------------------------------------------------------------#
def settings():
    def forgetpasswd():
        def otp():
            nm = e1.get()
            mypwd = e2.get()
            root.destroy()
            try:
                mycon = con.connect(host="localhost",user='root',passwd=mypwd,database='bibliotheca')
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
                    print(usr)
                    string = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
                    otpd = ""
                    ln = len(string)
                    for i in range(6):
                        otpd += string[math.floor(r.random()*ln)]

                    bdy = "your one time password is {}".format(otpd)
                    ezgmail.send(usr,"otp for Bibliotheca",bdy)
                    speak("you have recieved an otp on your registered email")
                    cck = pyautogui.prompt("please enter the otp:")
                    if cck == otpd:
                        speak("otp authentified syncronizing with your user_name")
                        nwpwd = pyautogui.password("new password:")
                        nwpwd2 = pyautogui.password("confirm password:")
                        if nwpwd == nwpwd2:
                            try:
                                mycon = con.connect(host="localhost",user="root",passwd=mypwd,database='bibliotheca')
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
        root = tk.Tk()
        file = os.path.join(os.getcwd(),'orbit','pwd rst.png')
        photo = tk.PhotoImage(file=file)
        root.iconphoto(False,photo)
        root.title("forget password")
        lbl = tk.Label(text="user name:")
        lbl2 = tk.Label(text="mysql passwd:")
        lbl.grid(column=0,row=0)
        lbl2.grid(column=0,row=1)
        e1 = tk.Entry(root,width=30)
        e2 = tk.Entry(root,width=30)
        e1.grid(column=1,row=0)
        e2.grid(column=1,row=1)
        btn = tk.Button(root,text="reset",image = photo,command=otp)
        btn.grid(column=2,row=2)
        root.geometry("400x105")
        root.mainloop()
    def add_account():
        window.destroy()
        install()
    def delete_account():
        mysqlpwd = pyautogui.password("enter mysql password>")
        mycon = con.connect(host="localhost",user="root",passwd=mysqlpwd,database='bibliotheca')
        if mycon.is_connected:
            print("connection to brain successful")
        cur = mycon.cursor()
        query = "select user_name from credentials"
        cur.execute(query)
        data = cur.fetchall()
        if m in data[0]:
            cur2 = mycon.cursor()
            query2 = "delete from credentials where user_name='{}'".format(m)
            print(query2)
            cur2.execute(query2)
            mycon.commit()
            pyautogui.alert("your account has been successful deleted","MESSAGE")
            window.destroy()
        else:
            pyautogui.alert("sorry some error occured","ALERT!")
            window.destroy()
    def main_menu():
        window.destroy()
        main_frame()
    root.destroy()
    window = tk.Tk()
    window.title("Settings")
    file = os.path.join(os.getcwd(),'orbit','settings.png')
    photo = tk.PhotoImage(file=file)
    window.iconphoto(False,photo)
    txt = "Current Login-{}".format(m)
    ttk.Label(window,text=txt).grid(column = 2,row = 0)
    ttk.Button(window,text="change password",command =forgetpasswd).grid(column = 0,row = 4,pady = 10)
    ttk.Button(window,text="add account",command = add_account).grid(column = 2,row = 4,pady = 10)
    ttk.Button(window,text="delete account",command = delete_account).grid(column = 4,row = 4,pady = 10)
    ttk.Button(window,text="main menu",command = main_menu).grid(column = 2,row = 6,pady = 10)
    window.geometry('384x115')
    window.mainloop()
#--------------------------------------------------------main_frame-------------------------------------------------------#
def main_frame():
    def quit():
        root.destroy()
    dir_mkr()
    global root
    root = tk.Tk()
    root.title("Bibliotheca")
    file = os.path.join(os.getcwd(),'orbit','dictionary.png')
    photo = PhotoImage(file = file)
    root.iconphoto(False,photo)
    file2 = os.path.join(os.getcwd(),'orbit','bg.png')
    bg_img = PhotoImage(file=file2)
    background = ttk.Label(root,image = bg_img)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    ttk.Label(root,text = "Bibliotheca",font = ("Comic Sans MS", 20)).grid(column = 0,row = 15, padx = 200, pady = 25)
    ttk.Button(root,text = "Dictionary",command = Button_dict).grid(column = 0,row = 200,padx = 10,pady = 100,sticky = "w")
    ttk.Button(root,text = "Convert English Words",command = convert).grid(column = 0,row = 200,padx = 200,pady = 100,sticky = "s")
    ttk.Button(root,text = "Semantics",command = semantic).grid(column = 0,row = 200,padx = 10,pady = 100,sticky = "e")
    ttk.Button(root,text = "Quit",command = quit).grid(column = 0,row = 0,pady = 25,sticky = "e")
    ttk.Button(root,text = "Settings",command=settings).grid(column = 0,row = 0,padx = 10,pady = 25,sticky = "w")
    root.geometry("590x400")
    root.mainloop()

#--------------------------------------------------__main__----------------------------------------------------------------------------------#
def main():
    speak("kindly enter your mysql password")
    sqlpwd = pyautogui.password("enter mysql password>>")
    try:
        mycon = con.connect(host="localhost",user="root",passwd=sqlpwd)
        if mycon.is_connected():
            cur = mycon.cursor()
            query = "show databases"
            cur.execute(query)
            data = cur.fetchall()
            for i in data:
                if "bibliotheca" in i:
                    mycon = con.connect(host="localhost",user="root",passwd=sqlpwd,database="bibliotheca")
                    if mycon.is_connected():
                        cur = mycon.cursor()
                        query = "select user_name from credentials"
                        cur.execute(query)
                        data = cur.fetchall()
                        print(data)
                        print(len(data))
                        if len(data) != 0:
                            break
            else:
                speak("opening installation wizard")
                install()
            getinfo()
            try:
                if len(a) == 0:
                    pass
                elif len(b) == 0:
                    pass
                elif m == None:
                    pass
                elif n == None:
                    pass
            except NameError:
                speak("check wheter the account exists or the entry field(s) are empty")
                pyautogui.alert("Check whether the account exists or the entry field(s) are empty","MESSAGE")
            if m in a[0]:
                if n in b[0]:
                    main_frame()
                else:
                    speak("incorrect password entered")
                    pyautogui.alert("incorrect password entered","Attention!")
            else:
                speak("incorrect username entered")
                pyautogui.alert("incorrect username entered")
    except Exception as e:
        speak("Access denied")
        pyautogui.alert("Access Denied!","ALERT!")
        print(e)