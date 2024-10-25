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
pygame.display.set_caption('Audio Visualisation : Logarithmic')

#function to calculate absolute frequencies
def get_absolute_frequencies(amplitudes, freq_step):
    num_frequencies = len(amplitudes)
    half_freqs = np.arange(1, num_frequencies // 2 + 1) * freq_step  # Positive frequencies
    negative_freqs = -half_freqs[::-1]  # Negative frequencies (reverse of positive)
    absolute_freqs = np.concatenate((half_freqs, negative_freqs))

    # Handle center frequency if num_frequencies is even
    if num_frequencies % 2 == 0:
        absolute_freqs = np.concatenate((absolute_freqs, [0.0]))  # Add 0.0 for center

    return absolute_freqs

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

    #using the Euclidean distance formula for complex plane to calculate the amplitudes array 
    amplitudes = abs(np.sqrt(real_fft**2 + imag_fft**2))

    total_power = np.sum(amplitudes**2)
    normalized_amplitudes = amplitudes / np.sqrt(total_power)
    


    #picking out the frequency steps from the amplitudes as the data chunk is smaller than the sampling rate
    freq_step  = RATE / len(amplitudes)

    absolute_freqs = get_absolute_frequencies(amplitudes, freq_step)

    #frequency limits
    min_freq = 0 
    max_freq = RATE / 8 #dividing by 2 because real signal has positive and negative values and further dividing by 2 as the higher frequency ranges are not very prominant

    
    
    screen.fill((0, 0, 0, 0.2)) #filling the screen with transparent colour

    # Plotting
    for i in range(len(amplitudes)):
        frequency = absolute_freqs[i]

        if -max_freq <= frequency <= max_freq:  # Check within desired range
            x_component = width * (frequency + max_freq) / (2 * max_freq)

            
            y_component = height* normalized_amplitudes[i]

            #balancing the y_component using logarithmic scaling and a scaling factor
            scaling_factor = 128
            y_component_normalised = np.log10(y_component) * scaling_factor
            
            pygame.draw.line(screen,(0,255,0),(x_component,height - y_component_normalised),(x_component,height - 0))

    pygame.display.flip()

stream.stop_stream()
stream.close()
p.terminate()
pygame.quit()