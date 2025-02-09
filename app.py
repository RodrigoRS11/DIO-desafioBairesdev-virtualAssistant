import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import pyjokes
import wikipedia
import webbrowser
import winshell
from pygame import mixer
import time

def get_audio():
    """Captures audio from the microphone and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print(text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not get that.")
    except sr.RequestError:
        speak("Sorry, the service is not available")
    return ""

def speak(text):
    """Converts text to speech and plays the generated audio."""
    filename = "voice.mp3"
    
    try:
        if os.path.exists(filename):
            os.remove(filename)
    except PermissionError:
        print("Waiting, try again...")
        time.sleep(1)
        os.remove(filename)
    
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    
    while mixer.music.get_busy():
        time.sleep(0.1)
    
    mixer.quit()

def save_to_text_file(text):
    """Saves the recognized speech to a text file."""
    with open("speech_output.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")

def open_browser_search(query):
    """Opens the default web browser and searches for the given query."""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}")

def respond(command):
    """Processes the voice command and performs the corresponding action."""
    print(f"Text from get_audio: {command}")
    
    if 'youtube' in command:
        speak("What do you want to search for?")
        keyword = get_audio()
        if keyword:
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.open(url)
            speak(f"Here is what I have found for {keyword} on YouTube")
    elif 'google' in command:
        speak("What do you want to search for?")
        query = get_audio()
        open_browser_search(query)
    elif 'search' in command:
        speak("What do you want to search for?")
        query = get_audio()
        if query:
            try:
                result = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("No Wikipedia page found for that query.")
            open_browser_search(query)
    elif 'speech to text' in command:
        speak("What do you want to transfor in text?")
        query = get_audio()
        save_to_text_file(query)
    elif 'text to speech' in command:
        query = input("What do you want to say? ")
        speak(query)
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'empty recycle bin' in command:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle bin emptied")
    elif 'what time' in command:
        current_time = datetime.now().strftime("%H:%M %p")
        print(current_time)
        speak(current_time)
    elif 'play music' in command or 'play song' in command:
        speak("Now playing...")
        music_dir = "C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\BootCamp25\\Projetos\\assistenteVirtual\\Music\\"
        songs = os.listdir(music_dir)
        if songs:
            playmusic(os.path.join(music_dir, songs[0]))
        else:
            speak("No songs found in the directory.")
    elif 'stop music' in command:
        speak("Stopping playback.")
        stopmusic()
    elif 'exit' in command:
        speak("Goodbye Rodrigo, till next time")
        exit()

def playmusic(song):
    """Plays the specified music file."""
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()

def stopmusic():
    """Stops the music playback."""
    mixer.music.stop()

if __name__ == "__main__":
    while True:
        print("I am listening...")
        user_command = get_audio()
        if user_command:
            respond(user_command)
