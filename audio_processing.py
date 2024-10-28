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
