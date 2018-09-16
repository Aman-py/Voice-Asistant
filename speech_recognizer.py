import pyaudio
import wave
def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename,'rb')
    pa=pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output=True
    )
    data = wf.readframes(chunk)

    while data:
        stream.write(data)
        data = wf.readframes(chunk)
    
    stream.close()
    pa.terminate()


import speech_recognition as sp
r=sp.Recognizer()

def initspeech():
    print('Listening......')
    
    play_audio('/media/aman-py/New Volume1/LearnCodeOnline/Speech Recognition/maybe-next-time.wav')
    
    with sp.Microphone() as source:
        print('Say Something...')
        audio = r.listen(source)
        
    play_audio('/media/aman-py/New Volume1/LearnCodeOnline/Speech Recognition/maybe-next-time-huh.wav')
    
    text = ''
    
    try:
        text = r.recognize_google(audio)
    except:
        print('Try Next Time')
        
    print(text)

    
initspeech()
