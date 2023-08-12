"""
citation_recognition.py: 
Contains logic for recognizing Bible verse citations from speech-to-text output.
"""
import re
import speech_recognition as sr

class CitationRecognition:
    """Recognizes Bible verse citations from speech-to-text output."""

    def __init__(self):
        """Initialize the CitationRecognition with a speech recognizer."""
        self.recognizer = sr.Recognizer()

    def recognize_speech(self, audio_data):
        """
        Convert audio data to text using a speech recognition library.

        Args:
            audio_data: The audio data to be recognized.

        Returns:
            str: The recognized text, or None if recognition failed.
        """
        try:
            return self.recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            print("Speech recognition failed")
            return None

    def extract_citations(self, text):
        """
        Extract Bible verse citations from the given text.

        Args:
            text (str): The text containing potential citations.

        Returns:
            list: A list of citations in the format (book, chapter, verse).
        """
        # Define a regular expression pattern for citations (e.g., "John 3:16")
        pattern = r'(\b[A-Za-z\s]+)\s+(\d+):(\d+)\b'
        return re.findall(pattern, text)
