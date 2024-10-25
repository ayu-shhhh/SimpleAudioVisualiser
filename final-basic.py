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
pygame.display.set_caption('Audio Visualisation : Basic')

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
    audio_data_fft = np.fft.fft(audio_data)

    #breaking audio data into real and imaginary parts
    real_fft = audio_data_fft.real
    imag_fft = audio_data_fft.imag

    #using the pythagoras theorem on the complex numbers logic to calculate the amplitudes array 
    amplitudes = abs(np.sqrt(real_fft**2 + imag_fft**2))

    # total_power = np.sum(amplitudes**2)
    # normalized_amplitudes = amplitudes / np.sqrt(total_power)
    


    #picking out the frequency steps from the amplitudes as the data chunk is smaller than the sampling rate
    freq_step  = RATE / len(amplitudes)

    #frequency limits
    min_freq = 0 
    max_freq = RATE / 8 #dividing by 2 because real signal has positive and negative values and further dividing by 2 as the higher frequency ranges are not very prominant

    
    
    screen.fill((0, 0, 0, 0.2)) #filling the screen with transparent colour

    # Plotting
    for i in range(len(amplitudes)):
        frequency = i * freq_step

        if min_freq <= frequency <= max_freq:
            x_component = (width * (frequency / max_freq))

            scaling_factor = 2
            y_component = ((height-10) * amplitudes[i] //10000000)

            pygame.draw.line(screen,(0,255,0),(x_component,height - y_component),(x_component,height - 0), 1)

    pygame.display.flip()

stream.stop_stream()
stream.close()
p.terminate()
pygame.quit()