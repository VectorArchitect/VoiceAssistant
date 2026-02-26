import time
# from xmlrpc import client
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from google import genai
import os





#name=input("Enter name of assistant: ")   #taking the name from the user
name = 'Jarvis'   #name of the assistant

recognizer = sr.Recognizer()   #creating a recognizer object to recognize the voice
engine = pyttsx3.init()          #creating an engine object of pyttsx3 to convert text to speech 

#API keys
newsapi="xxxxxxxxxxxxxx"   #news api key    #Account-savinavsharma
gemini_api_key = "xxxxxxxxxxxxxxxxxxxxx"   #Google Gemini API key # account-VectorArchitect0

client = genai.Client(api_key=gemini_api_key)

def speak(text):
    print(f"Assistant is saying: {text}") #debug line to show what assistant is saying in the console, jisse aapko pata chalega ki assistant kya bol raha hai
    engine.say(text)           #saying the text
    engine.runAndWait()         #running the engine to say the text and it will wait until the speech is finished before moving on to the next command
    engine.stop()               #stopping the engine after saying the text, jisse agar koi aur command aati hai to assistant usko turant sun sake without waiting for the previous speech to finish

#AI process function to get response from google gemini
def aiProcess(prompt):
    response = client.chat.send_message(
        model="gemini-2.0-flash",
        content=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.text

def aiProcess(command):
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=command
    )
    answer = response.text
    print(f"{name}: {answer}")
    # speak(answer.text)
    # response = client.models.generate_content_stream(
    # for chunk in response:
    #     print(f"{name}: "+chunk.text, end="", flush=True)
    #     speak(chunk.text)

#country for news
country = {
    "United States": "us",
    "India": "in",
    "United Kingdom": "gb"
}

#genere for news   
categories = ["sports", "technology"]   # valid NewsAPI categories
keywords = ["bitcoin"]                  # search keywords, not categories
genere = categories + keywords  


#####command function

def processCommand(command):
    # print(f"User: {command}")
    if command.lower()=="stop" or command.lower()=="exit" or command.lower()=="quit" or command.lower()=="stop stop":
                            # print("User: "+command)
                            speak("Goodbye!")
                            print("Goodbye!")
                            # time.sleep(2)
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

    elif "open brave" in command:
        webbrowser.open("https://search.brave.com/?lang=en-in")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        # with sr.Microphone() as source:
        #             print(f"{name} active, Listening...Say what to search on google")
        #             command = recognizer.listen(source)   #listning to the user
        #             search_query = command
        #             webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    # 
    ###################SEARCH ON YOUTUBE#################
    # 
    # elif "search" in command and "youtube" in command:
    #     with sr.Microphone() as source:
    #                 print(f"{name} active, Listening... say what to search on youtube")
    #                 command = recognizer.listen(source)   #listning to the user
    #                 search_query = command #.split("search for")[-1].strip()
    #                 webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
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
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I don't have that song in my library.")
     
     
     ############ NEWS API ############
    elif "news" in command.lower():
        # detect genre
        matched_genre = next((g for g in categories if g in command.lower()), None)
        matched_query = next((k for k in keywords if k in command.lower()), None)
        
        # detect country
        matched_country = "us"  # default
        for country_name, country_code in country.items():
            if country_name.lower() in command.lower():
                matched_country = country_code
                break

        # build correct URL
        if matched_query:
            url = f"https://newsapi.org/v2/top-headlines?q={matched_query}&country={matched_country}&apiKey={newsapi}"
        elif matched_genre:
            url = f"https://newsapi.org/v2/top-headlines?category={matched_genre}&country={matched_country}&apiKey={newsapi}"
        else:
            url = f"https://newsapi.org/v2/top-headlines?country={matched_country}&apiKey={newsapi}"

        print(f"Fetching news: {url}")  # debug - so you can see what URL is called
        
        r = requests.get(url)
        if r.status_code == 200:
            articles = r.json().get("articles", [])
            if not articles:
                speak("Sorry, no news found.")
            else:
                speak(f"Here are the top news headlines for {matched_country.upper()}:") 
                for article in articles[:3]:  # read top 3 articles
                    title = article.get("title", "No Title")
                    clean_title = title.split("-")[0].strip()  # remove source if present
                    print(f"News: {clean_title}")
                    speak(clean_title)
        else:
            print(f"API Error: {r.status_code}")
            speak("Sorry, I could not fetch the news.")

    #############################  USING GOOGLE GEMINI TO ANSWER QUESTIONS  #############################
    else:
        output=aiProcess(command)
        speak(output)
#######################################################################################################################################################

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
                
                        processCommand(command)
                        break
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
                continue
                # with sr.Microphone() as source:
                #     audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)   #listning to the user
                # print(f"{name} is not active, Listening...")
                # command = recognizer.recognize_google(audio).lower()
            if command.lower()=="stop" or command.lower()=="exit" or command.lower()=="quit" or command.lower()=="stop stop":
                            print("User: "+command)
                            speak("Goodbye!")
                            print("Goodbye!")
                            # time.sleep(2)
                            #break
                            exit()
        except sr.WaitTimeoutError:
            print("No speech detected, listening again...")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:                               #this exception is for any other error that may occur while
            print(f"Error: {e}")

