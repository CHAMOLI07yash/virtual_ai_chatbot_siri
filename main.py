import speech_recognition as sr  # import the dependencies 
import pyttsx3                   # python text to speech 
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener =sr.Recognizer()      # the  speech_recognition has a method Recognizer() that will listen your voice
engine =pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source: # your voice is source from the microphone
            print("listening...")
            voice =listener.listen(source)
            command =listener.recognize_google(voice)
            command=command.lower()   #lowercase
            if 'alexa' in command:     #print command if and only if you the specified text is in your voice as sorce here
                # engine.say(command)
                command=command.replace('alexa','')
                print(command)  

    except:
        pass
    return command

def run_Alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk("playing"+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk("the current time is" +time)
        print(time)
    elif 'who the heck is' in command:
        person=command.replace('who the heck is','')
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('hey you ,I have a boyfriend')
    elif 'are you in relationship' in command:
        talk('sorry ,I am in relationship with siri brother')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("please say the command aga in")

while True:
    run_Alexa()