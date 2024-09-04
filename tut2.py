import speech_recognition as sr

r = sr.Recognizer()

def get_text():
    with sr.Microphone() as Mic:
        print("Speak Now : ")
        text = r.listen(Mic)
        print("Time Over")

        try:
            print("Text is : ", r.recognize_google(text))
        except sr.UnknownValueError:
            print("Can't get your message ")