import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import urllib.parse


def speak(text):
    print("Assistant:", text)
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable")
        return ""


def search_google(query):
    encoded = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={encoded}"
    webbrowser.open(url)
    speak("Here is what I found on the web")

def search_youtube(query):
    encoded = urllib.parse.quote(query)
    url = f"https://www.youtube.com/results?search_query={encoded}"
    webbrowser.open(url)
    speak("Here is what I found on YouTube")


def process_command(command):
    print("Processing:", command)

    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "joke" in command:
        speak(pyjokes.get_joke())

    elif "open google" in command or "open browser" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "stop" in command or "exit" in command:
        speak("Goodbye")
        exit()

    elif "youtube" in command or "video" in command or "watch" in command:
        search_youtube(command.replace("youtube", "").replace("watch", ""))

    else:
        search_google(command)


# MAIN LOOP
speak("Assistant started")

while True:
    command = listen()
    if command:
        process_command(command)
