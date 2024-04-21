import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import requests
from bs4 import BeautifulSoup
import time
import pyautogui
import speedtest
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:

        speak("good morning sir!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")

    else:
        speak("good evening sir")

    speak("I am jarvis. Please tell me how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding.....")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.text","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

# if __name__=="__main__":
def Task_Gui():
    wishMe()
    while True:
        query = takeCommand().lower()

        if "go to sleep" in query:
            speak("Ok sir , You can me call anytime")
            break

        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            speak(results)

        elif 'search in youtube' in query:
            speak("ok sir, this is what i found for your Search!")
            query = query.replace("jarvis", '')
            query = query.replace("search in youtube", '')
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(f"{web}")
            # pywhatkit.playonyt(query)
            speak("Done sir.")

        elif 'open google' in query:
            # webbrowser.open("google.com")
            speak("Sir, what should i search on google.")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,The time is {strTime}")

        elif 'play sad song' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "tired" in query:
            speak("Playing your favourite songs, sir")
            music_dir='D:\music'
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")

        elif 'visual studio' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\Installer\setup.exe"
            os.startfile(codePath)

        elif "notepad" in query:
            path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)

        elif 'open word' in query:
            codePath="c:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk"
            os.startfile(codePath)

        elif "temperature" in query:
            search = "temperture in midnapur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, 'html.parser')
            temp = data.find('div', class_='BNeawe').text
            speak(f"The temperature of {search} is {temp}")

        elif "hi" in query or 'hello' in query:
            speak("Hello sir, how are you ?")
        elif "i am fine" in query:
            speak("that's great, sir")
        elif "how are you" in query or "kaise ho" in query:
            speak("Perfect, sir")
        elif "thank you" in query:
            speak("you are welcome, sir")
        elif 'Who are you' in query or 'what can you do' in query or 'aap kya kya karte ho' in query:
            speak('I am your personal assistant. I am Programmed to minor tasks like opening youtube,google chrome,gmail and stackvoerflow,predict time , take a screenshot,search wikipedia,predict weather in different cities ,get top headline news from times of india and you can ask me computational or geographical questions too!')
            print('I am your personal assistant. I am Programmed to minor tasks like opening youtube,google chrome,gmail and stackvoerflow,predict time , take a screenshot,search wikipedia,predict weather in different cities ,get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "open gmail" in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Opening gmail sir...")
            time.sleep(5)

        elif "click my photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE")
            pyautogui.press("enter")

        elif "internet speed" in query:
            wifi  = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576
            download_net = wifi.download()/1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ",download_net)
            speak(f"Wifi download speed is {download_net}")
            speak(f"Wifi Upload speed is {upload_net}")


        elif "where i am" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # state= geo_data['state']
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir i am not sure , but i think we are  in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, due to network issue i am not able to find where we are.")
                pass
        
        elif "calculate" in query:
            from Calculatenumbers import WolfRamAlpha
            from Calculatenumbers import Calc
            query = query.replace("calculate","")
            query = query.replace("jarvis","")
            Calc(query)

        elif "take a screenshot" in query:
            speak("sir please tell me the name for this screenshotfile")
            name = takeCommand().lower()
            speak("Please sir hold the screen for few second , i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir the screenshot is saved in our main folder . now i am ready for next command")

        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("jarvis","")
            speak("You told me to "+rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            speak("You told me to " + remember.read())

        elif 'quit now' in query:
            speak("Thanks for using me sir, have a good day")
            sys.exit()