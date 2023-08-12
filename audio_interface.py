"""
audio_interface.py: 
The audio_interface.py module can be extended to detect the audio system connected, 
such as the TASCAM Model 24 Mixer or any other audio interface. 
This detection can be performed by querying available audio devices,
and identifying the specific device by name, model, or other identifying characteristics.
"""

import sounddevice as sd
from config import Config


class AudioInterface:
    """Handles interactions with the audio system, such as TASCAM Model 24 Mixer."""

    def __init__(self, sample_rate=44100, channels=1, bit_depth=16):
        """Initialize the audio interface with given parameters."""
        self.config = Config()
        self.sample_rate = sample_rate
        self.channels = channels
        self.bit_depth = bit_depth

    def detect_audio_system(self):
        """Detect the audio system (e.g., TASCAM Model 24 Mixer) and return the device if found."""
        devices = sd.query_devices()
        return next((device for device in devices if 'TASCAM Model 24' in device['name']), None)

    def configure_windows_sound_settings(self):
        """Configure Windows sound settings for TASCAM Model 24 using the Config class."""
        self.config.configure_tascam_model_24()

    def connect_to_mixer(self):
        """Connect to the mixer device and configure Windows sound settings if found."""
        device = self.detect_audio_system()
        if device:
            sd.default.device = device['name']
            print(f"Connected to {device['name']}")
            self.configure_windows_sound_settings()
        else:
            print("Audio system not found")

    def read_audio_stream(self, duration):
        """Read audio stream for the specified duration and return the audio data."""
        audio_data, _ = sd.rec(int(duration * self.sample_rate),
                               samplerate=self.sample_rate, channels=self.channels)
        return audio_data

    def close_connection(self):
        """Stop any active audio streams and close the connection."""
        sd.stop()
        print("Connection to TASCAM Model 24 closed")
