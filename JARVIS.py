
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("\nListening...")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return ""

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        print("Internet connection / speech service problem.")
        return ""

    except Exception as e:
        print("Microphone error:", e)
        return ""


def greeting():

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning sir.")

    elif hour < 18:
        speak("Good afternoon sir.")

    else:
        speak("Good evening sir.")

    speak("I am Jarvis. How may I help you?")

def handle_command(command):

    # Google
    if "open google" in command:
        speak("Open Google.")
        webbrowser.open("https://www.google.com")

    # YouTube
    elif "open youtube" in command:
        speak("Open YouTube.")
        webbrowser.open("https://www.youtube.com")

    # GitHub
    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")

    # Search
    elif command.startswith("search"):

        query = command.replace("search", "", 1).strip()

        if query:
            speak("Searching Google.")

            url = (
                "https://www.google.com/search?q="
                + query.replace(" ", "+")
            )

            webbrowser.open(url)

        else:
            speak("What should I search for?")

    # Play YouTube
    elif command.startswith("play"):

        song = command.replace("play", "", 1).strip()

        if song:
            speak("Searching YouTube.")

            url = (
                "https://www.youtube.com/results?search_query="
                + song.replace(" ", "+")
            )

            webbrowser.open(url)

        else:
            speak("What should I play?")

    # Time
    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak("The current time is " + current_time)

    # Date
    elif "date" in command:

        current_date = datetime.datetime.now().strftime("%d %B %Y")

        speak("Today's date is " + current_date)

    # Calculator
    elif "open calculator" in command:

        speak("Open calculator.")

        os.system("start calc")

    # Notepad
    elif "open notepad" in command:

        speak("Opening Notepad.")

        os.system("start notepad")

    # CMD
    elif "open cmd" in command:

        speak("Opening command prompt.")

        os.system("start cmd")

    # File Explorer
    elif "open file explorer" in command:

        speak("Opening File Explorer.")

        os.system("start explorer")

    # Exit
    elif (
        "stop jarvis" in command
        or "exit jarvis" in command
        or "quit jarvis" in command
    ):

        speak("Goodbye sir.")

        return False

    # Unknown command
    else:

        speak("Sorry sir, I don't know that command yet.")

    return True



if __name__ == "__main__":

    greeting()

    while True:

        command = listen()

        if not command:
            continue

        # Check wake word
        if "jarvis" in command:

            command = command.replace("jarvis", "").strip()

            # If user only says "Jarvis"
            if not command:

                speak("Yes sir, I am listening.")

                command = listen()

                if not command:
                    continue

            should_continue = handle_command(command)

            if not should_continue:
                break

        else:

            print("Wake word 'Jarvis' not detected.")
            

if __name__ == "__main__":

    greeting()

    while True:

        command = listen()

        if not command:
            continue

        # Check wake word
        if "jarvis" in command:

            command = command.replace("jarvis", "").strip()

            # If user only says "Jarvis"
            if not command:

                speak("Yes sir, I am listening.")

                command = listen()

                if not command:
                    continue

            should_continue = handle_command(command)

            if not should_continue:
                break

        else:

            print("Wake word 'Jarvis' not detected.")