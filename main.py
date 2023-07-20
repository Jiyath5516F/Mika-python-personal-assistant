import pyttsx3 
import speech_recognition as sr 
import datetime
import time
import wikipedia 
import webbrowser
import os
import sys
import subprocess
import smtplib
import wolframalpha
from urllib.request import urlopen
import json
import pyjokes
import urllib.request
from clint.textui import progress
import requests
from bs4 import BeautifulSoup
import win32com.client as wincl
import winshell
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()





def wishMe():
    speak("Initializing Mika")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("Now I am online")
    print(':)')
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Mika. Online and ready sir. Please tell me how may I help you")      

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Sorry say that again please...")
        print("Sorry say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ncsound.net@gmail.com', 'ncsoundjk')
    server.sendmail('jiyathkiller@gmail.com', to, content)
    server.close()
    



if __name__ == '__main__':
    
    
    GREETINGS = ["hello Mika", "Mika", "wake up Mika", "you there Mika", "time to work Mika", "hey Mika",
             "ok Mika", "are you there"]
    GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]
    
    clear = lambda: os.system('cls')
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif "goodbye" in query or "offline" in query or "bye Mika" in query:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()
            
        #if 'good bye' in query or 'ok bye' in query or 'stop' in query:
            #speak('your personal assistant Mika is shutting down,Good bye')
            #print('your persnal assistant Mika is shutting down,Good bye')
            #break
        

        
        elif query in GREETINGS:
            speak(random.choice(GREETINGS_RES))
        
        elif 'email to friend' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                #to = "kloganathan074@gmail.com"  
                to = "jiyathkiller@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("youtube.com")
            time.sleep(5)

        elif 'open google' in query:
            speak('opening google')
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
            time.sleep(5)

        elif 'open stackoverflow' in query:
            speak('opening stackoverflow')
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("stackoverflow.com")
            time.sleep(5)
            
        elif 'open my website' in query:
            speak('opening your website')
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://jiyathkhan.000webhostapp.com/")
            time.sleep(5)
            
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(query)
            time.sleep(5)

        elif 'time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Time is {strTime}")

        elif 'open code' in query:
            speak('opening VS cose')
            codePath = "C:\\Users\\JiyathHiba\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            time.sleep(5)
            
        elif 'who are you' in query or 'what can you do' in query:
            speak('I am Mika version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
        
        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by jiyath")
            print("I was built by jiyath")
            
        elif "thanks you" in query or "thanks" in query:
            speak("i'm honoured to serve")
            print("i'm honoured to serve")
            
            
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
            
            
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
            
 
        elif "why you come to world" in query:
            speak("Thanks to jiyath. further It's a secret")
            
        
        elif 'ask' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="c75453a53a208d711bc39544dc9fcb00"
            client = wolframalpha.Client('X7K9GJ-7AVYX9AXGL')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer) 
            

        
                
        elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\664d695aa56340b694b2a9f14833ad2e\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
                
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('Notes.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")  
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "i want to see my notes" in query:
            speak("Showing Notes")
            file = open("Notes.txt", "r")
            print(file.read())
            speak(file.read(6))
            
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/"+location+"")
            
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif "calculate" in query:
             
            app_id = "X7K9GJ-7AVYX9AXGL"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
            
            
        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("X7K9GJ-7AVYX9AXGL")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
                
        elif "weather" in query:
            api_key = "c75453a53a208d711bc39544dc9fcb00"
            base_url = "http://api.openweathermap.org/data/2.5/forecast?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))


elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            
def some_function():
    print("Hello")
    
mappings = {'greeting': some_function}



assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()
assistant.request() 
