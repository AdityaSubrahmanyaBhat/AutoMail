import pyttsx3


friday =pyttsx3.init()


rate=friday.getProperty('rate')
friday.setProperty('rate',130)

# voices=friday.getProperty('voices')
# friday.setProperty('voice',voices[0].id)
# 0 - male , 1 - female



def greet():
    friday.say("Hello sir , Friday at your service")
    friday.runAndWait()


def bye():
    friday.say("Good bye sir , have a nice day")
    friday.runAndWait()


def talk(str):
    friday.say(str)
    friday.runAndWait()



