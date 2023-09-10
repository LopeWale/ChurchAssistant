from audio_interface import AudioInterface
from bible_api import BibleAPI
from citation_recognition import CitationRecognition
from config import Config
from display import Display

class MainApp:
    def __init__(self):
        self.config = Config()
        self.audio_interface = AudioInterface()
        self.bible_api = BibleAPI()
        self.citation_recognition = CitationRecognition()
        self.display = Display()
        
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
        audio_data = self.audio_interface.capture_audio()  # Assuming you have a capture_audio method
        citation = self.citation_recognition.recognize_speech(audio_data)
        
        # Step 6: Fetch and Display new verse based on citation
        book, chapter, verse = citation.split(":")  # Assuming citation is in "Book:Chapter:Verse" format
        new_verse = self.bible_api.fetch_verse(book, chapter, verse)
        self.display.show_verse(new_verse)
        
if __name__ == "__main__":
    app = MainApp()
    app.run()
