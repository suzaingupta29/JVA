import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary 
import requests
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "0c68d2948715440da6bfa9fb0745a472"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#      tts = gTTS(text)
#      tts.save('temp.mp3')
     

# # Initialize Pygame
#      pygame.init()

#         # Initialize the mixer module
#      pygame.mixer.init()

#         # Load the MP3 file
#      pygame.mixer.music.load('temp.mp3')

#         # Play the MP3 file
#      pygame.mixer.music.play()

#         # Keep the program running to allow the music to play
#      while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)

#         # Quit Pygame
#     #  pygame.quit()
#      pygame.mixer.music.unload()
#      os.remove("temp.mp3")
    


def processCommand(c):
    if "open google " in c.lower():
        webbrowser.open("https://google.com")
    elif "open facbook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower(): 
          r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
          if r.status_code == 200:
              # Parsing the response JSON
                data = r.json()
                
                # Extracting the articles
                articles = data.get("articles", [])
                
                # Extracting the titles into a list
                titles = [article.get("title") for article in articles]
                
                # Printing the list of titles
                for article in  articles:
                    speak(article['title'])

if __name__ == "__main__":
    speak("Initializing Jarvis...")
while True:    
    # listen for the wake word  jarvis 
    # obtain audio from the microphone

    r= sr.Recognizer()
    
    
     
    # recognize speech using sphinx
    print("recognizing...")
    try:
        with sr.Microphone() as source:
            print("Listening...!")
            audio = r.listen(source, timeout=2,phrase_time_limit=1)

        word = r.recognize_google(audio)
        if(word.lower() == "jarvis"):
              speak("Yes")
            # listen for command 
              with sr.Microphone() as source:
                print("Jarvis active")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                processCommand(command)

    except Exception as e:
        print("Error; {0}".format(e))    
