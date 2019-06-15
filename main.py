from gtts import gTTS
from langdetect import detect
from playsound import playsound
text_input = input()
lang = detect(text_input)
print("Text Language: ", lang)
tts = gTTS(text=text_input, lang=lang)
tts.save('speech.mp3')
playsound('speech.mp3', True)
