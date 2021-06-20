import librosa as lr
import matplotlib.pyplot as plt
import numpy as np
import pygame
audio, sfreq=lr.load('a1.wav')
x=lr.get_duration(y=audio, sr=sfreq)
x=int(len(audio)/x)
print(x)
time = np.arange(0, len(audio)) / sfreq
fig,ax = plt.subplots()
plt.show(block=False)
pygame.mixer.init()
my_sound = pygame.mixer.Sound('a1.wav')
my_sound.play()
for i in range(0, len(audio), x):
    pygame.time.wait(600)
    chunk = audio[i:i + x]
    t = time[i:i + x] 
    ax.plot(t, chunk,color='green')
    ax.set(xlabel='Time(s)',ylabel='Sound Amplitude')
    fig.canvas.draw()
    fig.canvas.flush_events()