# Imports
from gtts import gTTS

def getVoice(text):

    # Create TTS
    myobj = gTTS(text=text, lang='en', tld='us', slow=False)
    myobj.save("temp/test.mp3")
