import pyaudio
import numpy as np
import pygame


# Constants
CHUNK = 1024  # Number of audio samples per frame
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Mono audio
RATE = 44100  # Sampling rate (samples per second)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open the audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Audio Visualizer : Amplitude - Time")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read audio data
    data = stream.read(CHUNK)
    samples = np.frombuffer(data, dtype=np.int16)

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw audio data
    for i in range(len(samples) - 1):
        x = int(i * 800 / len(samples))
        y = int(200 + samples[i] * 200 / 32768)
        next_y = int(200 + samples[i + 1] * 200 / 32768)
        pygame.draw.line(screen, (0, 255, 0), (x, y), (x + 1, next_y))

    # Update display
    pygame.display.flip()

# Cleanup
stream.stop_stream()
stream.close()
p.terminate()
pygame.quit()
