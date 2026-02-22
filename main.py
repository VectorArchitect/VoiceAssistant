import time
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests





#n=input("Enter name of assistant: ")   #taking the name from the user
name = 'Jarvis'   #name of the assistant

recognizer = sr.Recognizer()   #creating a recognizer object to recognize the voice
engine = pyttsx3.init()          #creating an engine object of pyttsx3 to convert text to speech 
newsapi="xxxxxxxxxx"   #news api key
def speak(text):
    engine.say(text)           #saying the text
    engine.runAndWait()         #running the engine to say the text and it will wait until the speech is finished before moving on to the next command

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
                        
    elif "open google" in command:
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
     ############
    elif "news" in command.lower():
        # detect genre
        matched_genre = next((g for g in categories if g in command.lower()), None)
        
        # detect country
        matched_country = "us"  # default
        for country_name, country_code in country.items():
            if country_name.lower() in command.lower():
                matched_country = country_code
                break

    # build correct URL
    if "bitcoin" in command.lower():
        url = f"https://newsapi.org/v2/top-headlines?q=bitcoin&country={matched_country}&apiKey={newsapi}"
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
        for article in articles:
            title = article.get("title", "No Title")
            print(f"News: {title}")
            speak(title)
    else:
        print(f"API Error: {r.status_code}")
        speak("Sorry, I could not fetch the news.")
     ############
    # elif "news" in command.lower():
    #     r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
    #     if r.status_code == 200:      #checks if the request was successful (status code 200 means OK)
    #         data =r.json()            #parses the JSON response from the API and converts raw data into a Python dictionary. The resulting dictionary is stored in the variable data.
    #         articles = data.get("articles", [])   #retrieves the value associated with the key "articles" from the data dictionary. If the key "articles" does not exist, it returns an empty list [] as a default value. The resulting list of articles is stored in the variable articles.
    #         for article in articles:
    #             title = article.get("title", "No Title")    #retrieves the value associated with the key "title" from each article dictionary. If the key "title" does not exist, it returns the string "No Title" as a default value. The resulting title of each article is stored in the variable title.
    #             speak(title)
    #             print(f"News: {title}")
    #             speak("Next news...")
    # elif "news" in command.lower() and "bitcoin" in command.lower():
    #     r = requests.get(f"https://newsapi.org/v2/top-headlines?q=bitcoin&apiKey={newsapi}")
    #     if r.status_code == 200:      #checks if the request was successful (status code 200 means OK)
    #         data =r.json()            #parses the JSON response from the API and converts raw data into a Python dictionary. The resulting dictionary is stored in the variable data.
    #         articles = data.get("articles", [])   #retrieves the value associated with the key "articles" from the data dictionary. If the key "articles" does not exist, it returns an empty list [] as a default value. The resulting list of articles is stored in the variable articles.
    #         for article in articles:
    #             title = article.get("title", "No Title")    #retrieves the value associated with the key "title" from each article dictionary. If the key "title" does not exist, it returns the string "No Title" as a default value. The resulting title of each article is stored in the variable title.
    #             speak(title)
    #             print(f"News: {title}")
    # elif "news" in command.lower() and "technology" in command.lower() and "tech" in command.lower():
    #     r=requests.get(f"https://newsapi.org/v2/top-headlines?q=technology&apiKey={newsapi}")
    #     if r.status_code == 200:      #checks if the request was successful (status code 200 means OK)
    #         data =r.json()            #parses the JSON response from the API and converts raw data into a Python dictionary. The resulting dictionary is stored in the variable data.
    #         articles = data.get("articles", [])   #retrieves the value associated with the key "articles" from the data dictionary. If the key "articles" does not exist, it returns an empty list [] as a default value. The resulting list of articles is stored in the variable articles.
    #         for article in articles:
    #             title = article.get("title", "No Title")    #retrieves the value associated with the key "title" from each article dictionary. If the key "title" does not exist, it returns the string "No Title" as a default value. The resulting title of each article is stored in the variable title.
    #             speak(title)
    #             print(f"News: {title}")  
    # elif "news" in command and "sports" in command:
    #     r=requests.get(f"https://newsapi.org/v2/top-headlines?q=sports&apiKey={newsapi}")
    #     if r.status_code == 200:      #checks if the request was successful (status code 200 means OK)
    #         data =r.json()            #parses the JSON response from the API and converts raw data into a Python dictionary. The resulting dictionary is stored in the variable data.
    #         articles = data.get("articles", [])   #retrieves the value associated with the key "articles" from the data dictionary. If the key "articles" does not exist, it returns an empty list [] as a default value. The resulting list of articles is stored in the variable articles.
    #         for article in articles:
    #             #title = article.get("title", "No Title")    #retrieves the value associated with the key "title" from each article dictionary. If the key "title" does not exist, it returns the string "No Title" as a default value. The resulting title of each article is stored in the variable title.
    #             print(f"News: {article['title']}")
    #             speak(article["title"])              



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
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)   #listning to the user
                print(f"{name} is not active, Listening...")
                command = recognizer.recognize_google(audio).lower()
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
