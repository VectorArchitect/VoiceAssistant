import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

#n=input("Enter name of assistant: ")   #taking the name from the user
name = 'Jarvis'   #name of the assistant

recognizer = sr.Recognizer()   #creating a recognizer object to recognize the voice
engine = pyttsx3.init()          #creating an engine object of pyttsx3 to convert text to speech 




#####command function

def processCommand(command):
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        # with sr.Microphone() as source:
        #             print(f"{name} active, Listening...Say what to search on google")
        #             command = recognizer.listen(source)   #listning to the user
        #             search_query = command
        #             webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        # with sr.Microphone() as source:
        #             print(f"{name} active, Listening... say what to search on youtube")
        #             command = recognizer.listen(source)   #listning to the user
        # if "search for" in command:
        #     search_query = command.split("search for")[-1].strip()
        #     webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in command:
        webbrowser.open("https://www.twitter.com")
    elif "open x" in command:
        webbrowser.open("https://www.x.com")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
    elif "open github" in command:
        webbrowser.open("https://www.github.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ",1)[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    print(f"User: {command}")





def speak(text):
    engine.say(text)           #saying the text
    engine.runAndWait()         #running the engine to say the text and it will wait until the speech is finished before moving on to the next command

if __name__=="__main__":
    print(f"Say {name} to activate assistant.")

    while True:
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)   #listning to the user
            print("recognizing...")
            command = recognizer.recognize_google(audio).lower()
            
            if command.lower()==name.lower():               #if command == name of assistant
                print("User: "+command)
                print(f"{name}: Yes, how can I help you?")
                speak("Yes, how can I help you?")
                print(f"{name} is Listening...")
            
                while True:
                    try:
                        print(f"{name} active, Listening...")
                        with sr.Microphone() as source:
                            audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)   #listning to the user
                        print("recognizing...")
                        command = recognizer.recognize_google(audio).lower()   #recognizing the command #converting it to readable text by sending it to Google's Speech Recognition API.
                        #Microphone → audio (AudioData) → recognize_google() → command (text string)
                        print("User: "+command)
                        
                        if command.lower()=="stop" or command.lower()=="exit" or command.lower()=="quit" or command.lower()=="stop stop":
                            print("User: "+command)
                            speak("Goodbye!")
                            print("Goodbye!")
                            #break
                            exit()
                        elif command.lower()=="help" or command.lower()=="help help":
                            print("Available commands:")
                            print("- Open Google")
                            print("- Open YouTube")
                            print("- Open Facebook")
                            print("- Open Twitter")
                            print("- Open X")
                            print("- Open Instagram")
                            speak("Available commands are: Open Google, Open YouTube, Open Facebook, Open Twitter, Open X, and Open Instagram.")
                        else:
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
            else:
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)   #listning to the user
                print("recognizing...")
                command = recognizer.recognize_google(audio).lower()
        except sr.WaitTimeoutError:
            print("No speech detected, listening again...")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:                               #this exception is for any other error that may occur while
            print(f"Error: {e}")
