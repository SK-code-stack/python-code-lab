import webbrowser
import speech_recognition as sr
import pyttsx3
import musicLibrary
import timeCommand
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv
import google.generativeai as genai


# loads .env file
load_dotenv()
API = os.getenv("API")

r = sr.Recognizer()
engine = pyttsx3.init()


# def speak_old(text):
#     engine.say(text)
#     engine.runAndWait()


def speak(text):
    # Convert text to mp3
    tts = gTTS(text)
    tts.save("voice.mp3")

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

def processAI(c):
    genai.configure(api_key=API)

    model = genai.GenerativeModel("gemini-2.0-flash")

    AI_response = model.generate_content(f"give a short responce on this command --> {c}")
    speak(AI_response.text)

# processing command
def processCommand(c):
    print(f"Your command is --------------------------- {c}")
    if c.lower() == "jarvis":
        speak("yes sir")
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif timeCommand.time in c.lower():
        speak("are you asking time")
    else:
        processAI(command)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    activated = False  # Activation state

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source)  
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                command = r.recognize_google(audio)
                print("Recognized")

            if not activated:
                # First activation
                if command.lower() == "jarvis":
                    speak("Yes sir, I am ready.")
                    activated = True
                else:
                    # Target response once -------------------------------------- 
                    speak("chal nikal")
                    # speak("chaal bhonsdeyka")
            else:
                # Already activated, process any command
                processCommand(command)

            if "shutdown" in command.lower():
                speak("Shutting down.")
                break

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Could not request results from Google. Check your internet connection.")
        except Exception as e:
            print("Error:", e)
