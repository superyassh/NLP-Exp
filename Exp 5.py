import speech_recognition as sr
import pyttsx3

# Convert speech to text
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Speech recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

# Convert text to speech
engine = pyttsx3.init()
engine.say("Hello, how are you?")
engine.runAndWait()
