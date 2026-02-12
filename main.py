import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()   #creating a recognizer object to recognize the voice
ttsx = pyttsx3.init()          #creating a tts object to convert text to speech 

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

if __name__=="__main__":
    print("Hello, I am your assistant. How can I help you?")
    speak("Hello, I am your assistant. How can I help you?")
    while True:
        r=sr.Recognizer()   #Keep on listning to the user
        print("Listening...")
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=5)   #listning to the user
            command = r.recognize_google(audio)   #recognizing the command
            if command.lower()=='jarvis':
                print("Yes, how can I help you?")
                speak("Yes, how can I help you?")
            elif command=="stop":
                print("User: "+command)
                print("Goodbye!")
                speak("Goodbye!")
                break
            print(f"you said: {command}")
        except Exception as e:
            print("Sorry, I didn't catch that. Please try again.".format(e))
            # continue

