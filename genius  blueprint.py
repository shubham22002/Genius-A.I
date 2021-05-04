import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import os
import webbrowser
import pyautogui
import time
import speedtest
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import requests
import PyPDF2
from tkinter.filedialog import *
import translators as ts
from gtts import gTTS
import playsound
import smtplib
from getpass inport getpass

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def Speak(audio):
    engine.say(audio)
    print(f"Genius  :{audio}")
    engine.runAndWait()

def Speak1(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak("Good Morning,sir")
    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon,sir")
    else:
        Speak("Good Evening,sir")

wishme()

Speak("What can I do for you ?")

def Whatsapp():
    Speak("Tell Me The Name Of The Person!")
    name = takecommand()

    if 'a' in name: #add your your important person name
        Speak("Tell Me The Message!")   #speak the message
        msg = takecommand()
        Speak("Tell me the time In Hour!")  #speak the time in hour format
        hour = int(takecommand())
        Speak("Tell me the time In Minutes!") #speak the minutes (note:minute should be greater than the current time)
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+91(number)", msg, hour, min, 10) #type phone in the bracket

    if 'b' in name:
        Speak("Tell Me The Message!")
        msg = takecommand()
        Speak("Tell me the time In Hour!")
        hour = int(takecommand())
        Speak("Tell me the time In Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+91(number)", msg, hour, min, 10)
        pywhatkit.press('enter')

    if 'stranger' in name:
        Speak("Tell Me The Phone Number!") # if the number is not save
        phone = int(15)
        phone = f"+91{takecommand()}" #speak the number of unsaved person
        Speak("Tell Me The Message!")
        msg = takecommand()
        Speak("Time In Hour!")
        hour = int(takecommand())
        Speak("Time In Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg(phone, msg, hour, min, 10)
        pyautogui.press('enter')

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            query = command.recognize_google(audio, language='en-in')
            print(f"You said:{query}")

        except Exception as Error:
            return "none"

        return query.lower()

def Info():
    try:
        mk = query.replace("genius", "")
        max_result = 1
        how_to_fun = search_wikihow(mk, max_result)
        assert len(how_to_fun) == 1
        how_to_fun[0].print()
        Speak1(how_to_fun[0].summary)

    except Exception as e:
            Speak("Speak again")

def closeapps():
    if 'close chrome' in query:
        os.system("TASKKILL /im ()") #name of application.exe (eg."C:\Program Files\Google\Chrome\Application\chrome.exe") - copy only chrome.exe

    elif 'close mic' in query:
        os.system("TASKKILL /im ()") #name of application.exe

def PDF():
    Speak("In which Language?")
    lan = takecommand()

    if 'marathi' in lan:               # make pdf read in marathi
        Speak("Select the Pdf")        # select the pdf file from pop up window of file manager
        book = askopenfilename()
        book1 = open(book,'rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        Speak("Page number")           # speak the page number less than the page number you want (eg.you want 10 page number then speak 9)
        panu = int(takecommand())
        page = pdfreader.getPage(panu)
        text = page.extractText()
        print(text)
        Speak("Name the file")
        ask = takecommand()            # speak the file name
        try:
            ty = gTTS(ts.google(text,from_language='en',to_language="mr"))  #you can add your language checking documentation on google translate. 
            Speak1("Please Wait")
            print("Please Wait...")
            ty.save(f"{ask}.mp3")
            os.startfile(book)         # automatically opens the pdf file
            time.sleep(3)
            pyautogui.click(x=42, y=96)
            pyautogui.press('backspace')
            no = panu + 1               
            pyautogui.write(f"{no}")
            pyautogui.press('enter')
            Speak1("Playing audio")
            playsound.playsound(f"{ask}.mp3")
            Speak("Done sir")

        except Exception as e:
            Speak("Speak the commands again")
            return lan

    if 'hindi' in lan:                    # make pdf read in hindi
        Speak("Select the Pdf")
        book = askopenfilename()
        book1 = open(book,'rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        Speak("Page number")
        panu = int(takecommand())
        page = pdfreader.getPage(panu)
        text = page.extractText()
        print(text)
        Speak("Name the file")
        ask = takecommand()
        try:
            ty = gTTS(ts.google(text,from_language='en',to_language="hi"))
            Speak1("Please Wait")
            print("Please Wait...")
            ty.save(f"{ask}.mp3")
            os.startfile(book)          # automatically opens the pdf file
            time.sleep(3)
            pyautogui.click(x=42, y=96)
            pyautogui.press('backspace')
            no = panu + 1
            pyautogui.write(f"{no}")
            pyautogui.press('enter')
            Speak1("Playing audio")
            playsound.playsound(f"{ask}.mp3")
            Speak("Done sir")

        except Exception as e:
            Speak("Speak the commands again")
            return lan

    
    if 'english' in lan:
        Speak("Select the Pdf")         
        book = askopenfilename()
        book1 = open(book,'rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        Speak("Page number")
        panu = int(takecommand())
        page = pdfreader.getPage(panu)
        text = page.extractText()
        print(text)
        player = pyttsx3.init()        # directly starts reading pdf
        player.say(text)
        player.runAndWait()
        os.startfile(book)

def Speed():
    try:
        Speak("Checking speed")
        test = speedtest.Speedtest()
        downloading = test.download()
        correctDown = int(downloading/800000)
        uploading = test.upload()
        correctUpload = int(uploading/800000)
        Speak(f"The downloading speed is {correctDown} mbps and uploading is {correctUpload} mbps")

    except Exception as e:
            Speak("Speak again")

def email():
    ob=smtplib.SMTP("smtp.gmail.com",587)
    ob.ehlo()
    ob.starttls()
    myself = "Your email address.com"     #add your email address (note:before adding email address go to less secure app in google mail and turn it on)
    Speak("Enter the password")
    pass2 = getpass("Password:")
    ob.login(myself,pass2)
    Speak("Type the email address of the client") #add client email address
    top = input("Client email:")            
    Speak("Subject")                 #speak subject
    subject = takecommand()
    Speak("What is the Text in body")
    boby = takecommand()                  #speak what to text in body
    message = "Subject:{}\n\n{}".format(subject,boby)
    ob.sendmail(myself,top,message)
    Speak("Mail sent successfully")
    ob.quit()

while True:

    query = takecommand()

    if 'read pdf' in query:
        PDF()

    if 'play' in query:
        song = query.replace('play', '')         # speak play before search the song
        Speak('Playing' + song)
        pywhatkit.playonyt(song)

    if 'video' in query:
        song = query.replace('play', '')         # speak play before search the song
        Speak('Playing' + video)
        pywhatkit.playonyt(video)

    if 'who are you' in query:
        Speak("Hi ,I am Genius the A.I. known as Artificial Intelligence created by SHUBHAM PAWAR")  # you can modifiy upto well done query

    if 'name' in query:
        Speak("My name is Genius")

    if 'are you there' in query:
        Speak("Yes,sir")

    if 'full form' in query:
        Speak("My full form is Genetor Executable Network Intelligence User Service")

    if 'well done' in query:
        Speak("Thank you Sir")

    if 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p') # speak time
        Speak('Current time is ' + time)

    if 'day' in query:
        day = datetime.datetime.now().strftime("%A")
        Speak(day)

    if 'date' in query:
        date= datetime.date.today()
        Speak(date)

    if 'google' in query:
        query = query.replace("google", " ")   # speak google before search the anything
        pywhatkit.search(query)

    if 'mute' in query:           # this the automation of youtube upto volume down query
        pyautogui.press('m')

    if 'sound' in query:
        pyautogui.press('m')

    if 'pause' in query:
        pyautogui.press('k')

    if 'resume' in query:
        pyautogui.press('k')

    if 'full screen' in query:
        pyautogui.press('f') 

    if 'exit screen' in query:
        pyautogui.press('f')
        
    if 'contract' in query:
        pyautogui.press('i')
        time.sleep(2)
        pyautogui.press('k')

    if 'expand' in query:
        pyautogui.press('i')
        time.sleep(1)
        pyautogui.press('k')

    if 'speed up' in query:
        pyautogui.press('>')

    if 'speed down' in query:
        pyautogui.press('<')

    if 'forward' in query:
        pyautogui.press('j')
        pyautogui.press('k')

    if 'backward' in query:
        pyautogui.press('l')
        pyautogui.press('k')

    if 'volume up' in query:
        pyautogui.hotkey('volumeup')

    if 'volume down' in query:
        pyautogui.hotkey('volumedown')

    if 'message' in query:                 # calls whatspp fuction
        Whatsapp()

    if 'minimise' in query:                 #minimize the window
        pyautogui.hotkey('Win', 'd')

    if 'maximize' in query:                #maximize the window
        pyautogui.hotkey('Win', 'd')

    if 'youtube' in query:
        query = query.replace("youtube", " ")         # speak google before search the anything
        webbrowser.open('https://www.youtube.com')
        time.sleep(5)
        pyautogui.press('/')
        pyautogui.write(query)
        pyautogui.press('enter')

    if 'remind me' in query:
        Speak("Name the file")   # Create remind.txt file
        ask = takecommand()
        remeber = open(ask, "w")
        Speak("what to remind sir")
        msg = takecommand()
        remeber.write(msg)
        Speak("Done sir")
        remeber.close()

    if 'said' in query:
        remeber = open(ask, 'r')
        Speak(remeber.read())

    if 'internet speed' in query: # calls Speed function
        Speed()
 
    if 'how to' in query: # calls Info function
        Info()

    if 'retype' in query:
        pyautogui.press('/')              #speak retype to clear the text from serachbox and say what you want to search
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        wr = takecommand()
        pyautogui.write(wr)
        pyautogui.press('enter')

    if 'terminate' in query:       # gets exit form code
        Speak("Ok sir, have a nice day")    
        exit()

    if 'temperature' in query:      # speak temperature of(name) - name=state,district
        url = (f"https://www.google.com/search?q={query}")
        r = requests.get(url)
        data = BeautifulSoup(r.text, 'html.parser')
        temperature = data.find("div", class_="BNeawe").text
        query = query.replace("temperature","")
        Speak(f"The Temperature{query} is {temperature}")

    if 'shutdown' in query:
        Speak("Do you want to shutdown ?") # close all the working apps and shutdown the pc
        vr = takecommand()
        if 'yes' in vr:
            Speak("As you wish")
            Speak("Closing all the working application")
            Speak("Done sir")
            Speak("Have a nice Day")
            closeapps()
            os.system('shutdown /s /t 1')
        else:
            break

    if 'restart' in query:           # restarts the pc
        Speak("Do you want to restart ?")
        vr = takecommand()
        if 'yes' in vr:
            os.system('shutdown /r /t 1')
        else:
            break

    if 'close window' in query:
        pyautogui.hotkey('alt', 'f4')

    if 'close this tab' in query:      #automation of chrome
        pyautogui.hotkey('ctrl', 'w')

    if 'open new tab' in query:
        pyautogui.hotkey('ctrl', 't')

    if 'open new window' in query:
        pyautogui.hotkey('ctrl', 'n')

    if 'history' in query:
        pyautogui.hotkey('ctrl', 'h')

    if 'download' in query:
        pyautogui.hotkey('ctrl', 'j')

    if 'clear chat' in query:         # clear all the chats
        clear = lambda: os.system("cls")
        clear()

    if 'mail' in query:
        email()                      #calls email function



