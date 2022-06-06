import pyttsx3
import speech_recognition as sr
import webbrowser
import DateTime
import wikipedia
#print(sr.Microphone.list_microphone_names())

def assistant(audio):
    engine = pyttsx3.init()
# getter: To get the current
# engine property value
    voices = engine.getProperty('voices')
# setter method
# [0] for male voice
# [1] for female voice
    engine.setProperty('voices', voices[1].id)
# Method governing assistant's speech
    engine.say(audio)
# Blocks/processes queued commands
    engine.runAndWait()

def greeting():
# This is a simple greeting and
# it informs the user that the
# assistant has started
    assistant("Hello, I am your Virtual Assistant. How Can I Help You Today")

def audioinput():
# this function is all about
# taking the audio input from
# the user
    aud = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('listening and processing')
# The pause is optional here
        #aud.pause_threshold = 0.7
        audio = aud.listen(source)
# Using try (for valid commands)
# and exception for when the assistant
# doesnt "catch" the command
    try:
        print("understanding")
# en-eu is simply for the accent here
# english we can also use 'en-GB' or 'en-au'
# for UK and Australian accents
        phrase = aud.recognize_google(audio, language='en-us')
        print("you said: ", phrase)
    except Exception as exp:
        print(exp)
        print("Can you please repeat that")
        return "None"
    return phrase

def theTime(self):
# This function is for time
    time = str(datetime.datetime.now())
# time needs to be sliced for
# better audio comprehension
    print(time)
    hour = time[11:13]
    min = time[14:16]
    assistant(self, "The time right now is" + hour + "Hours and" + min + "Minutes")

def theDay():
# This function is for the day
    day = datetime.datetime.today().weekday() + 1
# assigning a number makes it a bit cleaner
    Day_dict = {1: 'Monday', 2: 'Tuesday',
    3: 'Wednesday', 4: 'Thursday',
    5: 'Friday', 6: 'Saturday',
    7: 'Sunday'}
    if day in Day_dict.keys():
        weekday = Day_dict[day]
        print(weekday)
    assistant("it's " + weekday)

def core_code():

    greeting()

    while (True):

        r = sr.Recognizer()
        my_mic = sr.Microphone(device_index=1) #my device index is 1, you have to put your device index
        with my_mic as source:
            print("Say now!!!!")
            audio = r.listen(source)
            user_input = r.recognize_google(audio, language='en-us') #take voice input from the microphone
        print(r.recognize_google(audio, language='en-us'))
        if "open medium" in user_input.lower():
            assistant("Opening Medium.com")

            webbrowser.open("www.medium.com")
            continue
        elif "open google" in phrase:
            assistant("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        elif "what day it is" in phrase:
            theDay()
            continue
        elif "what time it is" in phrase:
            theTime()
            continue

        elif "bye" in phrase:
            assistant("Exiting. Have a Good Day")
            exit()
        elif "from wikipedia" in phrase:

            assistant("Checking the wikipedia ")
            phrase = phrase.replace("wikipedia", "")

            result = wikipedia.summary(phrase, sentences=4)
            assistant("As per wikipedia")
            assistant(result)
        elif "what is your name" in phrase:
            assistant("I am your nameless virtual assistant")

core_code()
  