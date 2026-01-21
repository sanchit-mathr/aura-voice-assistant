from speech import listen, speak
from commands import process_command

speak("Aura started")

while True:
    command = listen()
    if command:
        process_command(command)
