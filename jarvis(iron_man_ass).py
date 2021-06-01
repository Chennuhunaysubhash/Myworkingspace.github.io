import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki

listener = sr.Recognizer()
speaker = pyttsx3.init()

rate = speaker.getProperty('rate')
speaker.setProperty('rate', 150)

voices = speaker.getProperty('voices')

speaker.setProperty('voice', voices[1].id)

def speak(text):
    speaker.say('yes boss ' + text)
    speaker.runAndWait()
def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()

va_name = 'jarvis'

speak_ex('I am your ' + va_name + 'tell me boss.')

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name + ' ', '')
                # print(command)
                # speak(command)

    except:
        print('Check your MicroPhone')
        speak_ex('Check your MicroPhone')
    return command

while True:
    user_command = take_command()
    if 'close' in user_command:
        print('See you again boss. I will be there when ever you call me')
        speak('See you again boss. I will be there when ever you call me')
        break
    elif 'time' in user_command:
        cut_time = dt.datetime.now().strftime("%I:%M %p")
        print(cut_time)
        speak(cut_time)
    elif 'play' in user_command:
        user_command = user_command.replace('play ', '')
        print('playing ' + user_command)
        speak('playing ' + user_command + 'enjoy boss.')
        pk.playonyt(user_command)
        break
    elif 'search for' in user_command or 'google' in user_command or 'get the results for' in user_command:
        user_command = user_command.replace('search for ', '')
        user_command = user_command.replace('google ', '')
        user_command = user_command.replace('get the results for ', '')
        speak('searching for ' + user_command)
        pk.search(user_command)
    elif 'who is' in user_command or 'get the details' in user_command:
        user_command = user_command.replace('who is ', '')
        user_command = user_command.replace('get the details ', '')
        info = wiki.summary(user_command, 2)
        print(info)
        speak(info)
    elif 'who are you' in user_command:
        speak_ex('I am your ' + va_name + 'tell me boss.')
    else:
        speak_ex('please say it again boss.')