import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# use the microphone as source for input
with sr.Microphone() as source:
    print("Listening...")
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)

# save the text to a .txt file
with open('output.txt', 'w') as f:
    f.write(text)

