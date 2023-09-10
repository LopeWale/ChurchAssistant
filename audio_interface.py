import sounddevice as sd
from config import Config  # Assuming Config class has methods for iRig Pre HD

class AudioInterface:
    def __init__(self, sample_rate=44100, channels=1, bit_depth=16):
        self.config = Config()
        self.sample_rate = sample_rate
        self.channels = channels
        self.bit_depth = bit_depth

    def detect_audio_system(self):
        devices = sd.query_devices()
        return next((device for device in devices if 'iRig Pre HD' in device['name']), None)

    def configure_windows_sound_settings(self):
        self.config.configure_irig_pre_hd()  # Assuming you have this method in Config

    def connect_to_audio_device(self):
        device = self.detect_audio_system()
        if device:
            sd.default.device = device['name']
            print(f"Connected to {device['name']}")
            self.configure_windows_sound_settings()
        else:
            print("Audio system not found")

    def read_audio_stream(self, duration):
        audio_data, _ = sd.rec(int(duration * self.sample_rate),
                               samplerate=self.sample_rate, channels=self.channels)
        return audio_data

    def close_connection(self):
        sd.stop()
        print("Connection to iRig Pre HD closed")
