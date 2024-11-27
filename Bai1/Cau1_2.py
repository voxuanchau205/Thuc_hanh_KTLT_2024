import serial
import pyaudio
import numpy as np


arduino = serial.Serial('COM3', 9600)  
CHUNK = 1024
RATE = 44100


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def get_amplitude(data):
    """Phân tích biên độ âm thanh"""
    samples = np.frombuffer(data, dtype=np.int16)
    amplitude = np.max(np.abs(samples))
    return amplitude

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        amplitude = get_amplitude(data)
        print("Amplitude:", amplitude)

        
        threshold = 5000
        if amplitude > threshold:
            arduino.write(b'1') 
        else:
            arduino.write(b'0')  

except KeyboardInterrupt:
    print("Kết thúc chương trình")
    stream.stop_stream()
    stream.close()
    p.terminate()
    arduino.close()
