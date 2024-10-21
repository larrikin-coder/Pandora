<h1> PANDORA </h1>
<h4> Python Automated Newly Developed and Organized Requisite Assistant</h4>

# How did i achieve GUI for the application?
- Utilizing both tkinter module and pygame module to sync and run all the codes so that the User Experience is not laggy and instead of command line based a bit interactive simplay running a pygame mainloop helped me to achieved all this.
- To give a command using voice simply press SpaceBar when inside the application.


# Speech Recognition and Production
- For speech Recognition we are using a module name speech_recognition and we take command using take_command Function
```py
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
```
- For Speech Production we are using another module named pyttsx3 we can change the voice of the Assistant using voices[index_id]. Sapi5 a microsoft service provides the voices.
```py
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
```

# Installation
Auto-Installation enabled (creation of database and required modules)
```py
import os
import subprocess

try:
    import pyttsx3                                          
    import datetime
    import speech_recognition as sr
    import wikipedia
    import webbrowser
    import random as r
except ImportError:
    directory = os.path.join(os.getcwd(), 'debug.cmd')
    subprocess.call(directory)
```
- A batch-file name debug.cmd is created containing all the modules with the version specifics which allows the program to execute installation for all the modules listed without user interaction.


Installation Function

```py
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
```
# Instructions 
- Introduce: Introduces herself.
- Send email: Email Interface created for sending mail via the app only with the ability to add documents of various types with the help of on-screen dialog box.
```py
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
```
- Play Music: Plays musics from your system randomly or you can either specify the music to be played
- Increase/ Decrease System Volume
- Shutdown/ Restart/ Sleep/ Hibernate
- Youtube: opens and search on Youtube
```py
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
```
- Search Meanings and Sematics: utilizes in-house module (dictionary.py) to find the sematics and words.
- Other Few uses cases
  - Processor
  - Wikipedia
  - Calculator
    - Scientific
    - Basic
  - Date and time
  - Download youtube video

