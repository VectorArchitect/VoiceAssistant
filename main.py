import speech_recognition as sr
import webbrowser
import pyttsx3

#n=input("Enter name of assistant: ")   #taking the name from the user
name = 'Jarvis'   #name of the assistant

recognizer = sr.Recognizer()   #creating a recognizer object to recognize the voice
engine = pyttsx3.init()          #creating an engine object of pyttsx3 to convert text to speech 

def processCommand(command):
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        with sr.Microphone() as source:
                    print(f"{name} active, Listening...Say what to search on google")
                    command = recognizer.listen(source)   #listning to the user
                    search_query = command
                    webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        with sr.Microphone() as source:
                    print(f"{name} active, Listening... say what to search on youtube")
                    command = recognizer.listen(source)   #listning to the user
        if "search for" in command:
            search_query = command.split("search for")[-1].strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in command:
        webbrowser.open("https://www.twitter.com")
    elif "open x" in command:
        webbrowser.open("https://www.x.com")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
    print(command)
    pass

def speak(text):
    engine.say(text)           #saying the text
    engine.runAndWait()         #running the engine to say the text and it will wait until the speech is finished before moving on to the next command

if __name__=="__main__":
    print(f"{name}: Initializing {name}...")
    speak(f"Initializing {name}...")
    while True:
        print("Listening...")
        #r=sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)   #listning to the user
            
            print("recognizing...")
            command = recognizer.recognize_google(audio).lower()   #recognizing the command
            print("User: "+command)

            if command.lower()==name.lower():
                print("User: "+command)
                print(f"{name}: Yes, how can I help you?")
                speak("Yes, how can I help you?")
                with sr.Microphone() as source:
                    print(f"{name} active, Listening...")
                    audio = recognizer.listen(source)   #listning to the user
            elif command.lower()=="stop":
                print("User: "+command)
                speak("Goodbye!")
                print("Goodbye!")
                break
            processCommand(command)
        except sr.WaitTimeoutError:
            print("No speech detected, listening again...")
            continue
        except sr.UnknownValueError:
            print("Could not understand audio")
            continue
        except Exception as e:                               #this exception is for any other error that may occur while recognizing the speech and it will print the error message and continue listening for the next command
            print(f"Error: {e}")
            continue

