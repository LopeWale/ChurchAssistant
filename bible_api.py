"""bible_api.py: 
Manages interactions with the getbible.net API to fetch Bible verses.
"""

import requests
import json

class BibleAPI:
    """Handles interactions with the getbible.net API to fetch Bible verses."""

    def __init__(self, base_url="https://getbible.net/json"):
        """Initialize the BibleAPI with an optional base URL."""
        self.base_url = base_url

    def fetch_verse(self, book, chapter, verse):
        """
        Fetch a specific Bible verse by book, chapter, and verse number.

        Args:
            book (str): The name of the book in the Bible.
            chapter (int): The chapter number.
            verse (int): The verse number.

        Returns:
            str: The text of the specified verse, or None if not found.
        """
        url = f"{self.base_url}?p={book} {chapter}:{verse}"
        response = requests.get(url)

        if response.status_code == 200:
            json_str = response.text[1:-2]  # Remove leading and trailing parentheses
            verse_data = json.loads(json_str)
            return verse_data['book'][0]['chapter'][0]['verse'][0]['verse']
        else:
            print(f"Error fetching verse: {response.status_code}")
            return None
