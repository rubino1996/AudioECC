'''
audio_processing.py

This module provides functions to load and save audio files.
It uses the `wave` library to read WAV files and `scipy.io.wavfile.write` to save them.
The audio data is returned as a NumPy array, making it suitable for further processing.
'''
import wave
import numpy as np
from scipy.io.wavfile import write

def load_audio(file_path):
    audio = wave.open(file_path)
    sample_freq = audio.getframerate()
    n_samples = audio.getnframes()
    signal_wave = audio.readframes(-1)
    audio.close()
    return sample_freq, n_samples, np.frombuffer(signal_wave, dtype=np.int16)

def save_audio(file_path, sample_freq, signal_array):
    write(file_path, sample_freq, signal_array)
