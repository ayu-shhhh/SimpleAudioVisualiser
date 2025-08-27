# SimpleAudioVisualiser

A Python application for generating real-time audio visualizations using libraries such as PyQt, PyGame, and NumPy. This project captures system audio output and transforms it into dynamic, way & bar-graph style visuals.

This was developed as a semester mini-project with the goal of understanding the fundamentals of sound engineering and signal processing.

## Core Technologies

* **GUI Framework:** PyQt
* **Visualization/Rendering:** PyGame
* **Audio I/O:** PyAudio
* **Data Processing:** NumPy & SciPy

## Features

* **Real-time Audio Capture:** Reads and processes the system's live audio output stream.
* **Frequency Analysis:** Utilizes the Fast Fourier Transform (FFT) to convert the time-domain audio signal into the frequency domain for analysis.
* **Multiple Normalization Techniques:** Includes several methods to process amplitude values for a better visual experience, including:
    * Logarithmic Normalization
    * Logarithmic Sigmoid Normalization
* **High-Performance Rendering:** Employs PyGame for plotting, which provides a high frame rate for smoother animations compared to alternatives like Matplotlib.
* **Clean User Interface:** The graphical user interface, built with PyQt, provides a menu to select and launch different visualizers.

## Technical Workflow

The application follows a structured pipeline to process and visualize audio:

1.  **Audio Capture:** The `PyAudio` library is used to open the system's audio stream and read data in chunks. Key parameters used are a sample rate of 44100 Hz and a chunk size of 2048 frames.

2.  **Data Conversion:** The raw audio data, captured in a hexadecimal format, is converted into a 16-bit integer array using `numpy.frombuffer()` to prepare it for numerical processing.

3.  **Frequency Domain Conversion:** To analyze the frequency components of the signal, a Fast Fourier Transform is applied using `numpy.fft.fft()`. This converts the time-domain audio data into its frequency-domain representation.

4.  **Amplitude Calculation:** The output of the FFT is an array of complex numbers. The absolute value of this array is calculated, and the mean amplitude is determined for several predefined frequency ranges.

5.  **Normalization:** The calculated amplitude values are processed using different normalization functions, such as Logarithmic and Logarithmic Sigmoid, to scale the data for effective visualization.

6.  **Rendering:** The final processed data is plotted in real-time using `PyGame`. This library was chosen specifically for its higher frame rate and the ability to create a clean visual output without labeled axes, which is ideal for a purely cosmetic visualizer.

7.  **GUI Control:** The entire application is wrapped in a GUI created with `PyQt`. This framework provides the main menu for users to interact with and select the desired visualization type.

## Getting Started

### Prerequisites

* Python 3.x
* Pip (Python package installer)

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/ayu-shhhh/SimpleAudioVisualiser.git
    cd SimpleAudioVisualiser
    ```

2.  Install the required dependencies:
    ```bash
    pip install numpy scipy pyaudio pygame PyQt5
    ```
    *(Note: You may need to install PortAudio for PyAudio to function correctly on your system.)*

3.  Run the application:
    ```bash
    python main.py
    ```
    *(Please replace `main.py` with the actual name of your main script.)*

## Future Scope

This project serves as a strong foundation for more advanced applications in signal processing and machine learning. Potential future enhancements include:

* **Music Information Retrieval:** Developing systems for music genre classification or speech emotion recognition.
* **Interactive Controls:** Creating tools for music production or remixing that provide insights into spectral characteristics.
* **Hardware Integration:** Building music-controlled lighting systems that react to the frequency data of the audio.
* **API Integration:** Connecting with streaming services like Spotify or YouTube to visualize music directly from the source.

