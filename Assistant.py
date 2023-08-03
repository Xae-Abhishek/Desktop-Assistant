import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import time as time
import webbrowser
import pywhatkit as pwt


# Using The Microsoft Speech Tools to Pronounce 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

# Setting The Default Voice To David
engine.setProperty('voices', voices[0].id)

# The Function To Speak The Given String In Argument
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function That Greets Us At The Start and IntroDuces Himself

def wishme():
    
    hour=int(datetime.datetime.now().hour)
    print("Assistant : ",end="\n\n")

    if hour>0 and hour<12:
        print("\t    Good morning")
        speak("Good Morning")

        print("\t    Have A Good Day Today")
        speak("Have A Good Day Today")
    elif hour<18:
        print("\t    Good Afternon")
        speak("Good Afternon")
        
    else:
        print("\t    Good Evening")
        speak("Good Evening")
        
    print("\n\n\t    I am Jarvis Your Personalised Desktop Assistant")
    speak("I am Jarvis Your Personalised Desktop Assistant")

    print("\t    Please Command me to task as you see fit")
    speak("Please Command me to task as  you see fit")


# Recognise User Input From Microphone
def takecommand():
    
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        
        
        r.energy_threshold=10
        audio = r.listen(source,timeout=10,phrase_time_limit=5)

      
    # recognizing the audio  in case we are unabele to recognise the audio it will show custom Exception

    try:
        print("\n\tRecognizing ...")
        query=r.recognize_google(audio,language='en-in')
        print("\n\tUser Said : ",query)

       
        time.sleep(2)
    except Exception as e:
        print(e)
        print("\n\tSay That Again Please")
        

        # return none mens no task is to be performed as we are unabel to recognise the mic
        return "None"


    # Task To be performed when we are abel to recognize the mic
    return query

# Body of The Program
os.system("cls")
wishme()

while True:
    time.sleep(2)

    os.system('cls')
    
    
    print("\n\n\tAssistant Is Listening : ")

    # lower to avoid the case errors
    
    query=takecommand().lower()

    # task 1 Wikipedia Search

    # Task Related To WikiPedia
    if 'wikipedia' in query:
        speak('Searching Wikipedia')
        query=query.replace('wikipedia', '')

        # Wikipedia search Result
        
        result=wikipedia.summary(query,sentences=2)
        
        # Speak The Result
        speak("According To WikiPedia")
        print("\n\n",result)
        speak(result)

    # Open Websites
    elif 'youtube' in query:
        webbrowser.open('youtube.com')
    
    # open google

    elif 'google' in query:
        webbrowser.open('google.com')

    # open times of india
    elif 'news update' in query:
        webbrowser.open('timesofindia.com')

    
    elif 'open geeks for geeks' in query:
        webbrowser.open('https://www.geeksforgeeks.org/')

    elif 'chess' in query:
        webbrowser.open('chess.com')
    

    elif 'college' in query or 'university' in query:
        webbrowser.open('https://www.ljku.edu.in/')

    elif "song" in query:
        print("\n\n\t Which Song : ")
        speak("Which Song")
        
        song_details=takecommand().lower()
        
        pwt.playonyt(song_details)
        print("Done")

    
    elif 'code' in query:
        path=r"C:\Users\91972\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(path)

    elif 'chrome' in query or 'surf' in query or 'web' in query or 'search' in query:
        path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(path)
    elif query=='none':
        pass
    
    else:
        print("\n\tCommand Not Recorgnised")
        print("\n\tTry Other Task")
        speak("I am Unabel To Do That")
        time.sleep(2)