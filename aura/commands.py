import pyjokes
from utils import google_search, youtube_search, get_time
from speech import speak

def process_command(command):
    if "time" in command:
        speak(f"The time is {get_time()}")

    elif "joke" in command:
        speak(pyjokes.get_joke())

    elif "youtube" in command or "watch" in command:
        youtube_search(command)
        speak("Here is what I found on YouTube")

    elif "stop" in command or "exit" in command:
        speak("Goodbye")
        exit()

    else:
        google_search(command)
        speak("Here is what I found on Google")
