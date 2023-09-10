from ctypes import CDLL  # For loading the C++ shared library
from audio_interface import AudioInterface
from bible_api import BibleAPI
from citation_recognition import CitationRecognition
from config import Config
from display import Display
from speech_recognition import SpeechRecognition  # Assuming your Python file is named speech_recognition.py

class MainApp:
    def __init__(self):
        self.config = Config()
        self.audio_interface = AudioInterface()
        self.bible_api = BibleAPI()
        self.citation_recognition = CitationRecognition()
        self.display = Display()

        # Initialize the SpeechRecognition class
        self.speech_recognition = SpeechRecognition()

        # Load the C++ shared library
        self.cpp_module = CDLL('./performance_module.so')

    def run(self):
        # Step 1: Initialize configurations
        self.config.initialize()  # Assuming you have an initialize method in config.py
        
        # Step 2: Setup Audio Interface
        self.audio_interface.setup()  # Assuming you have a setup method in audio_interface.py
        
        # Step 3: Fetch initial Bible verse (e.g., Genesis 1:1)
        initial_verse = self.bible_api.fetch_verse("Genesis", 1, 1)
        
        # Step 4: Display initial verse
        self.display.show_verse(initial_verse)
        
        # Step 5: Run Citation Recognition
        while True:
            text = self.speech_recognition.recognize_speech()
            if text:
                print(f"Recognized text: {text}")

                # Call the process_audio method from the C++ module
                self.cpp_module.PerformanceModule_process_audio(text.encode('utf-8'))

if __name__ == "__main__":
    app = MainApp()
    app.run()
