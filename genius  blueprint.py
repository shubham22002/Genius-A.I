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
from gtts import gTTS
import translators as ts

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

Speak("What can i do for you ?")


def Whatsapp():
    Speak("Tell Me The Name Of The Person!")
    name = takecommand()

    if '' in name:
        Speak("Tell Me The Message!")
        msg = takecommand()
        Speak("Tell me the time In Hour!")
        hour = int(takecommand())
        Speak("Tell me the time In Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+91(number)", msg, hour, min, 10)

    if '' in name:
        Speak("Tell Me The Message!")
        msg = takecommand()
        Speak("Tell me the time In Hour!")
        hour = int(takecommand())
        Speak("Tell me the time In Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+91(number)", msg, hour, min, 10)
        pywhatkit.press('enter')

    if 'stranger' in name:
        Speak("Tell Me The Phone Number!")
        tr = takecommand()
        phone = int(15)
        phone = tr
        Speak("Tell Me The Message!")
        msg = takecommand()
        Speak("Time In Hour!")
        hour = int(takecommand())
        Speak("Time In Minutes!")
        min = int(takecommand())
        pywhatkit.sendwhatmsg(phone, msg, hour, min, 10)

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


def closeapps():
    if 'close chrome' in query:
        os.system("TASKKILL /im ") #name of application.exe

    elif 'close mic' in query:
        os.system("TASKKILL /im ") #name of application.exe

def read():
    Speak("In which Language?")
    lan = takecommand()

    if 'marathi' in lan:
        Speak("Select the Pdf")
        book = askopenfilename()
        book1 = open(book,'rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        Speak("Page number")
        print("Enter the Page number and press")
        panu = int(input(''))
        page = pdfreader.getPage(panu)
        text = page.extractText()
        print(text)
        Speak("Name the file")
        ask = input('')
        ty = gTTS(ts.google(text,from_language='en',to_language="mr"))
        print("Please Wait...")
        ty.save(f"{ask}.mp3")
        Speak("done sir")
        os.startfile(book)

    if 'hindi' in lan:
        Speak("Select the Pdf")
        book = askopenfilename()
        book1 = open(book,'rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        Speak("Page number")
        print("Enter the Page number and press")
        panu = int(input(''))
        page = pdfreader.getPage(panu)
        text = page.extractText()
        print(text)
        Speak("Name the file")
        ask = input('')
        ty = gTTS(ts.google(text,from_language='en',to_language="hi"))
        print("Please Wait...")
        ty.save(f"{ask}.mp3")
        Speak("done sir")
        os.startfile(book)
    
    if 'Normal' in lan:
        Speak("Select the Pdf")
        book = askopenfilename()
        book1 = open(book,'rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        Speak("Page number")
        print("Enter the Page number and press")
        panu = int(input(''))
        page = pdfreader.getPage(panu)
        text = page.extractText()
        player = pyttsx3.init()
        player.say(text)
        player.runAndWait()
        os.startfile(book)

while True:

    query = takecommand()

    if 'read pdf' in query:
        read()

    if 'play' in query:
        song = query.replace('play', '')
        Speak('Playing' + song)
        pywhatkit.playonyt(song)

    if 'video' in query:
        song = query.replace('play', '')
        Speak('Playing' + video)
        pywhatkit.playonyt(video)

    if 'who are you' in query:
        Speak("Hi ,I am Genius the A.I. known as artificial intelligence created by SHUBHAM PAWAR")

    if 'name' in query:
        Speak("My name is Genius")

    if 'are you there' in query:
        Speak("Yes,sir")

    if 'full form' in query:
        Speak("My full form is genetor executable network intelligence user service")

    if 'well done' in query:
        Speak("Thank you Sir")

    if 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        Speak('Current time is ' + time)

    if 'google' in query:
        query = query.replace("google", " ")
        pywhatkit.search(query)

    if 'mute' in query:
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

    if 'volume up' in query:
        pyautogui.hotkey('volumeup')
        pyautogui.press('k')

    if 'volume down' in query:
        pyautogui.hotkey('volumedown')
        pyautogui.press('k')

    if 'whatsapp' in query:
        Whatsapp()

    if 'minimise' in query:
        pyautogui.hotkey('Win', 'd')

    if 'maximize' in query:
        pyautogui.hotkey('Win', 'd')

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

    if 'youtube' in query:
        query = query.replace("youtube", " ")
        webbrowser.open('https://www.youtube.com')
        time.sleep(5)
        pyautogui.press('/')
        pyautogui.write(query)
        pyautogui.press('enter')

    if 'remind me' in query:
        Speak("What to remind sir")
        msg = takecommand()
        remeber = open("remind.txt", "w")
        remeber.write(msg)
        remeber.close()

    if 'said' in query:
        remeber = open('remind.txt', 'r')
        Speak(remeber.read())

    if 'internet speed' in query:
        Speak("Checking speed")
        test = speedtest.Speedtest()
        downloading = test.download()
        correctDown = int(downloading/800000)
        uploading = test.upload()
        correctUpload = int(uploading/800000)
        Speak(f"The downloading speed is {correctDown} mbps and uploading is {correctUpload} mbps")

    if 'how to' in query:
        mk = query.replace("genius", "")
        max_result = 1
        how_to_fun = search_wikihow(mk, max_result)
        assert len(how_to_fun) == 1
        how_to_fun[0].print()
        Speak1(how_to_fun[0].summary)

    if 'retype' in query:
        pyautogui.press('/')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')

    if 'type' in query:
        wr = takecommand()
        wr = wr.replace("type", "")
        pyautogui.write(wr)
        pyautogui.press('enter')

    if 'terminate' in query:
        Speak("Ok sir, have a nice day")
        exit()

    if 'temperature' in query:
        region = takecommand()
        url = (f"https://www.google.com/search?q={region}")
        r = requests.get(url)
        data = BeautifulSoup(r.text, 'html.parser')
        temperature = data.find("div", class_="BNeawe").text
        region = region.replace('temperature', '')
        Speak(f"The Temperature {region} is {temperature}")

    if 'shutdown' in query:
        Speak("Do you want to shutdown ?")
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

    if 'restart' in query:
        Speak("Do you want to restart ?")
        vr = takecommand()
        if 'yes' in vr:
            os.system('shutdown /r /t 1')
        else:
            break

    if 'close window' in query:
        pyautogui.hotkey('alt', 'f4')

    if 'close this tab' in query:
        pyautogui.hotkey('ctrl', 'w')

    if 'open new tab' in query:
        pyautogui.hotkey('ctrl', 't')

    if 'open new window' in query:
        pyautogui.hotkey('ctrl', 'n')

    if 'history' in query:
        pyautogui.hotkey('ctrl', 'h')

    if 'download' in query:
        pyautogui.hotkey('ctrl', 'j')



