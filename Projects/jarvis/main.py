
import webbrowser
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# processing command
def processCommand(c):
    print(f"Your commend is --------------------------- {c}")
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://googyoutubele.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    pass

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            # first listining text
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source)  
                audio = r.listen(source)
                print("recoginized")

            command = r.recognize_google(audio)
            # activating jarvis
            if command.lower() != "jarvis":
                speak("chaal bhonsdeyka")
            else:
                speak("yes sir") 
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    r.adjust_for_ambient_noise(source)  
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

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
