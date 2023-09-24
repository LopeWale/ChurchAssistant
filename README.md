# Church Bible Verse Display Application

## Objective

Creating an application for the church's media team to display Bible verses on a chosen monitor, triggered by the preacher's speech.

## Requirements

### Programming Languages
- Python

### Hardware
- TASCAM Model 24 Mixer
- Compatible USB cable
- Multiple monitors

### Libraries and APIs
- SpeechRecognition (Python library)
- Bible API by getbible.net
- screeninfo (Python library)

## Steps

1. **Hardware Setup**: Connect the TASCAM Model 24 Mixer to your Windows laptop using a compatible USB cable.
2. **Driver Installation**: Install the necessary drivers for the TASCAM Model 24 Mixer.
3. **Speech Recognition**: Install and setup the SpeechRecognition library in Python.
4. **Verse Citation Recognition**: Develop a mechanism to recognize Bible verse citations from the text generated by the speech-to-text system.
5. **Bible API Interface**: Create functionality to fetch the text of corresponding Bible verses using the Bible API.
6. **Display Module**: Implement a feature that displays the fetched Bible verse on a monitor.
7. **Screen Configuration**: Use the screeninfo library to fetch information about all connected screens and allow the user to specify the display monitor.
8. **Testing and Debugging**: Integrate all features and run comprehensive tests. Debug and refine the system as needed.

## Modules

### 1. Speech Recognition Module
- **Libraries**: SpeechRecognition, pocketsphinx, PyAudio

### 2. Verse Citation Recognition Module
- **Libraries**: re, NLTK, spaCy

### 3. Bible API Interface Module
- **Libraries**: requests, JSON parsing

### 4. Display Module
- **Libraries**: PyQt or Tkinter, screeninfo

### 5. Configuration Module
- **Libraries**: configparser

### 6. Test Module
- **Libraries**: pytest, unittest

### 7. Utilities Module
- **Libraries**: General utility libraries

## Task Breakdown

- Implement audio_interface.py
- Implement bible_api.py
- Implement citation_recognition.py
- Implement config.py
- Implement display.py
- Implement speech_recognition.py
- Implement utils.py
- Compile C++ Component (if used)
- Integrate Components
- Testing: Write and run tests
- Configuration and Environment Setup
- Logging and Monitoring
- Run and Evaluate the PoC


Here is my repo "https://github.com/LopeWale/ChurchAssistant"

The new objective is to use the computer's microphone, to which the iRig is connected, as the audio input source. You also want to verify that the iRig is set as the computer's microphone in the sound settings. How do i need to modify the files to work with iRig Pre HD instead of the TASCAM Model 24?