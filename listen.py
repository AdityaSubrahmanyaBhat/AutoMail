import speech_recognition as sr
import talk
import mail

listener=sr.Recognizer()

def get_audio(duration=5):
    with sr.Microphone() as source:
        audio=listener.record(source=source,duration=duration)
        final_audio=listener.recognize_google(audio)
        print(final_audio)
        return final_audio

responses=["yes","yes please","yes Friday","yes I do","yes I want to send a mail","yes send it","yes Friday send it"]

def listen():
    talk.greet()
    talk.talk("Do you want to send a mail?")
    audio=get_audio()
    if audio in responses:
        talk.talk("Ok sure , What is the message?")
        message=get_audio(10)
        talk.talk("Shall i send it sir?")
        confirmation=get_audio()
        if confirmation in responses:
            mail.send_mail(message)
            talk.talk("I have sent the mail.")
            talk.bye()
        else:
            talk.bye()