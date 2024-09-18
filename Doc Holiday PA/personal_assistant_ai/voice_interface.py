## voice_interface.py

import speech_recognition as sr
import pyttsx3

class VoiceInterface:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Set default speech rate

    def listen(self) -> str:
        """
        Listens to the microphone and returns the recognized text.
        """
        text = ""
        with sr.Microphone() as source:
            print("Listening...")
            audio_data = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio_data)
                print(f"Recognized: {text}")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
        return text

    def speak(self, response: str) -> None:
        """
        Uses the text-to-speech engine to speak out the response.
        """
        self.engine.say(response)
        self.engine.runAndWait()
