import speech_recognition as sr


def recognize():
    # obtain audio from the microphone
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True

    #Settings

    with sr.Microphone() as source:
        print("You better say noodle....")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("You my ears aren't working")
    except sr.RequestError as e:
        print("Yo google pooped itself so I don't understand anything; {0}".format(e))