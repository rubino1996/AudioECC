# AudioECC

A Python project demonstrating audio encryption and decryption using **Elliptic Curve Cryptography (ECC)**. This educational project explores ECC principles applied to audio, transforming audio signals into encrypted waveforms and recovering the original upon decryption. Includes utilities for processing audio files, generating ECC keys, and visualizing signals.

## 📜 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Examples](#examples)
- [Limitations](#limitations)

## ✨ Features
- **Audio Encryption/Decryption**: Encrypt and decrypt audio signals with ECC.
- **Key Generation**: Generate public and private ECC keys for both sender and recipient.
- **Visualization**: Plot original, encrypted, and decrypted audio signals for comparison.
- **Educational Purpose**: Showcases ECC’s application in multimedia security (not optimized for performance).

## 📥 Installation
1. Clone this repository:
https://github.com/rubino1996/AudioECC.git

## 🚀 Usage
1. Prepare an Audio File: Place your audio file (e.g., input_audio.wav) in the data/ directory.
2. Run the Main Script: python main.py
3. View Output: Encrypted and decrypted audio files will be saved in data/output/, and a plot showing the original, encrypted, and decrypted waveforms will be saved and displayed.

## 📁 Project Structure
- AudioECC/
- ├── audio_processing.py        # Audio I/O functions
- ├── ecc_encryption.py          # ECC encryption/decryption functions
- ├── plotting.py                # Plotting functions
- ├── utils.py                   # Utility functions
- ├── main.py                    # Main script
- ├── requirements.txt           # List of required packages
- └── README.md                  # Project documentation

## 🛠 Examples
**Encrypting and Decrypting an Audio File**
1. Load your audio file (input_audio.wav).
2. Run main.py to encrypt and decrypt the audio.
3. View the generated plot and listen to encrypted_audio.wav and decrypted_audio.wav in data/output/.
**Plotting**
1. The plot_signals function in plotting.py generates a side-by-side comparison of the original, encrypted, and decrypted audio signals.

## ⚠️ Limitations
- Performance: ECC is computationally slower for large audio files. This project is intended for educational purposes rather than high-performance encryption of large multimedia data.
