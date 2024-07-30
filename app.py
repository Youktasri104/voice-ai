import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import wikipedia
import pyjokes
import ecapture
import subprocess

a = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
###with sr.Microphone() as source:
     # print(sr.__version__)
     # print(dir(a))
      #a.adjust_for_ambient_noise(source)
     # print("listening...")
      #v=a.listen(source, timeout=1)

def talk(text):
       engine.say(text)
       engine.runAndWait()

#def wish():
     # talk("hello , this is youktasri'voice assistant , what can i do for you")
     #

def take():

    try:

            with sr.Microphone() as source:
                   a.adjust_for_ambient_noise(source)
                   talk("hello!, this is your voice assistent. what can i do for you? ")
                   print("listening...")
                   v = a.listen(source, timeout=1)
                   print("recognizing")
                   c=a.recognize_google(v)
                   print(c)

    except sr.UnknownValueError:
            print("not working")
    except sr.RequestError as e:
            print(f"could not;{e}")
    return c


def run():
       c=take()
       if 'play' in c:
              talk("playing the video in youtube")
              pywhatkit.playonyt(c)

       elif 'time' in c:
              d=datetime.datetime.now().strftime("%I %M %p")
              print(d)
              talk("the current time is"+ d)
              #talk(f"the time is {d.hour} and {d.minute}")

       elif 'date' in c:
              e=datetime.datetime.today().strftime("%B %d ,%Y")
              print(e)
              talk('today is'+e)

       elif 'YouTube' in c:
              talk("here we go to youtube")
              webbrowser.open("youtube.com")

       elif 'Google' in c:
              talk("here we go to google")
              webbrowser.open("google.com")

       elif 'chat GPT' in c:
              talk("here we go to chatgpt")
              webbrowser.open("chatgpt.com")

       elif 'about'in c:
              talk("here is the information")
              i=wikipedia.summary(c,2)
              print(i)
              talk(i)

       elif 'joke' in c:
              p=pyjokes.get_joke()
              print(p)
              talk(p)

       elif 'camera'in c or 'picture' in c or 'photo' in c :
              talk("taking a picture")
              ecapture.capture(0,'camera','myimg.jpg')

       elif 'shudown' in c or 'restart' in c:
              talk("shuting down your system")
              subprocess.call("shutdown/p/f") 

       elif 'hi' in c or 'hello' in c:
              talk("hello! its great to hear you" )

       elif 'how are you' in c:      
              talk("i am good sir")

       elif 'who are you' in c:
              talk("i am voice assistent created by yuktasri. ")
              
            

run()
       
