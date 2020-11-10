# importing pyttsx3
import pyttsx3
#importing seechrecognition as sr
import speech_recognition as sr
# importing wikipedia
import wikipedia
# importing date and time using datetime module
import datetime

# creating function as take_commands which accepts audio,recognize it
# and gives output,
# if there is no error.
def take_commands():
    # initializing speechrecognition.
    r = sr.Recognizer()
    # opening physical microphone of computer.
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.5
        # declaring original audio to the variable.
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            # returning none if there is no error.
            return "None"
    return Query
# creating speak function which gives speaking
# capability to the voice assistance
def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say
    # will be spoken by the voice assistant
    engine.say(audio)
    engine.runAndWait()

# creating greetme function to welcome the user
# in the beggining of the running
def greetMe():
    CurrentHour = int(datetime.datetime.now().hour)
    # creating if condition to say greetings,
    # according to the time.
    if CurrentHour >= 0 and CurrentHour < 12:
        Speak('Good Morning!')
    elif CurrentHour >= 12 and CurrentHour < 18:
        Speak('Good Afternoon!')
    elif CurrentHour >= 18 and CurrentHour != 0:
        Speak('Good Evening!')
greetMe()
Speak('Hey Buddy, It\'s  your assistant Thunder!')
Speak('tell me about today?')

# driver code
if __name__ == '__main__':
    # using while loop to comunicate infinitely.
    while True:
        command = take_commands()
        if "nothing Thunder" in command:
            Speak("Sure sir! as your wish")
            Speak("bye, have a great day")
            # break is used to terminate the loop
            break
        elif "what\'s up" in command or 'how are you' in command:
            Speak('I am good!')
        elif "what are you" in command:
            Speak('i am example of personal assisstant and i am here to make your life easy')
        elif "hello" in command:
            Speak("hey")
        else:
            # declaring information from wikipedia in variable outputs.
            outputs = wikipedia.summary(command, sentences=4)
            Speak('Gotcha')
            Speak('Wikipedia says')
            Speak(outputs)
