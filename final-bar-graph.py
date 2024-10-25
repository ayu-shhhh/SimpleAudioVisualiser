import pyaudio
import numpy as np
import pygame

#define constants
CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

#initialise pyaudio object and open streamn for reading data
p = pyaudio.PyAudio()
input_device_index = 0
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

# Pygame setup
pygame.init()
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Audio Visualisation : Bar Graph')

# Frequency ranges
frequency_ranges = [
    (30, 70),
    (70, 120),
    (120, 170),
    (170, 250),
    (250, 350),
    (350, 500),
    (500, 700),
    (700, 1000),
    (1000, 1400),
    (1400, 2000),
    (2000, 2800),
    (2800, 4000),
    (4000, 5600),
    (5600, 7800),
    (7800, 11000),
    (11000, RATE / 2)
]

# Main loop
running = True
while running:

    #check for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #read data
    data = stream.read(CHUNK)  

    #converting hexadecimal array to type decimal int16 so that numpy can process it
    audio_data = np.frombuffer(data, dtype=np.int16)
    
    #perform fft to convert time domain signal to frequency domain
    frequencies = np.fft.fft(audio_data)
    
    
    # Calculate amplitudes for specified frequency ranges
    amplitudes = []
    for start, end in frequency_ranges:
        start_index = int(start / (RATE / CHUNK))
        end_index = int(end / (RATE / CHUNK))
        avg_amplitude = np.mean(np.abs(frequencies[start_index:end_index]))
        amplitudes.append(avg_amplitude)
    
    screen.fill((0, 0, 0)) #filling the screen with black colour

    # Plotting
    for i, amplitude in enumerate(amplitudes):
        x = int(width * (i + 0.5) / len(amplitudes))
        normalized_amplitude = amplitude / max(amplitudes)  # Normalize amplitude
        bar_height = int(normalized_amplitude * (height - 50)) + 1
        pygame.draw.rect(screen, (0, 255, 0) , (x - 25, height - bar_height, 50, bar_height))

    pygame.display.flip()

stream.stop_stream()
stream.close()
p.terminate()
pygame.quit()