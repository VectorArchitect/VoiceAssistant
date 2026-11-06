# VoiceAssistant
I'm trying to build a voice assistant which listens to your voice commands via microphone , analyses it and replies.

## The modules and APIs I will be using are:<br>
<br>
  -pyttsx3          &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;     # To convert text to speech <br>
  -speech recognition  &emsp;&emsp;  # To convert speech to text<br>
  -pyAudio             &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;  # Gives out the audio via the speaker of the device<br>
  -setuptools          &emsp;&emsp;  <br>
  -webbrowser          &emsp;&emsp;  <br>
  -NewsAPI.org         &emsp;&emsp;   # News API <br>
  -google-genai        &emsp;&emsp;   # Gemini API <br>
  -requests            &emsp;&emsp;   # To fetch data from APIs <br>

  


## Development tests

The Gemini request and response validation live in `ai_service.py`, separate
from microphone, text-to-speech, and GUI/device initialization.

Run the hardware-independent tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

The assistant needs a working Google GenAI API key and microphone/audio
dependencies for a full interactive run. The tests use a fake client and do
not make network requests.
