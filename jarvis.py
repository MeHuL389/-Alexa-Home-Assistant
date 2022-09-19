from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!") 

    speak("I am garvis sir, how may i help you")        
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening burr...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except exception as e:
        #print(e)
        print("Say that one more time please")
        return"None"
    return query         
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('smsreborn2017@gmail.com', '2017smsreborn')
    server.sendmail('smsreborn2017@gmail.com', to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikiepdia...")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)



        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")  
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open amazon' in query:
            webbrowser.open("amazon.in")
        elif 'open github' in query:
            webbrowser.open("github.com") 


       # elif 'play music' in query:
            #music_dir= 'C:\\Users\\mehul\\Downloads\\Video'
            #song=os.listdir(music.dir)
            #print(songs)
            #os.startfile(os.path.join(music_dir, songs[0]))


        elif' the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}") 
            print(strTime)

        elif 'open spotify' in query:
            spotifyPath = "C:\\Users\\mehul\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifyPath)

        elif 'email to mehul' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "mehulsaini928@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my burr mehul, I am not able to sned this mail right now")
