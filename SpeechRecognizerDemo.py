import speech_recognition as sr
from datetime import date
from time import sleep
import pyaudio
import valib

#python method for recognition function
def SpeechRecognitionV2():

    a = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ready')
        #For noise removal
        a.adjust_for_ambient_noise(source, duration=0.5)
        audio=a.record(source, duration=3)
        data=a.recognize_google(audio)
        print(data)
    
    try:
        print('Thinking...')
        data = a.recognize_google(audio, language='en-in')
        print('User said that, ', data)
    except Exception as e:
        print('exception :',e)
        
        speak("Pardon me, I did not hear that properly, would you please repeat that?")
        return "None"
    return data
while True:
    data = SpeechRecognitionV2() #the thing speaker said will be saved to this variable
    print("The test got in program is : ",data)
    valib.audio_playback(data)
    
    break
