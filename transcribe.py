import speech_recognition as sr
import os

assets_dir = r'C:\Users\User\OneDrive\Desktop\Kyrgyz4x4rentals\assets'

for filename in os.listdir(assets_dir):
    if filename.endswith('.ogg'):
        filepath = os.path.join(assets_dir, filename)
        print(f'\n=== {filename} ===')
        try:
            r = sr.Recognizer()
            with sr.AudioFile(filepath) as source:
                audio = r.record(source)
            text = r.recognize_google(audio, language='ru-RU')
            print(text)
        except Exception as e:
            print(f'Error: {e}')
