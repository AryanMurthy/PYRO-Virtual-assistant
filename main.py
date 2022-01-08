#importing the required libraries for the project
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
listener = sr.Recognizer()
engine = pyttsx3.init() #initializing python text to speech library in a variable

#giving voice of a male or female to the virtual assistant
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#defining a function for the engine variable to execute speech recognition
def talk(text):
    engine.say(text)
    engine.runAndWait()

#virtual assistant giving it's introduction to the user
talk('I am pyro, your personal voice assistant.')
talk('How may I help you today')

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...') #when listening appears in the prompt, the user can start speaking
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'pyro' in command: #given the name of assistant as Pyro-python robot
                command = command.replace('pyro','')
                print(command)
    except:
        pass
    return command

def run_pyro():
    command = take_command()
    print(command)

    #playing any video in youtube
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    #searching any keyword in google
    elif 'search' in command:
        my_search = command.replace('search','')
        talk('searching' + my_search)
        pywhatkit.search(my_search)

    #asking for time from pyro
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)

    #asking for date from pyro
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        print(date)
        talk('Current date is' + date)

    #extracting 3 lines of information from wikipedia about any topic
    elif 'wiki' in command:
        person = command.replace('wiki','')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    #asking pyro whether its single
    elif 'are you single' in command:
        talk('I am in a relationship with wifi.')

    #confessions
    elif 'i love you' in command:
        talk('I love you too, but as a friend.')

    #aking pyro for a joke by using pyjokes library
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    #To terminate the program
    elif 'ok bye' in command:
        talk('Hope to see you again. Byeeeeeeee!')
        sys.exit('process completed')

    #default if pyro do not understand what is being said
    else:
        talk('please say that again, I didnt understood.')

while True:
    run_pyro()



