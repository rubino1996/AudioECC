'''
main.py

This script performs encryption and decryption of audio signals using Elliptic Curve Cryptography (ECC).
It demonstrates how to apply ECC to multimedia data by encrypting audio waveforms and attempting to
recover the original signal upon decryption. The script also measures encryption and decryption times
and saves the results to files.

Dependencies:
- audio_processing: For loading and saving audio files.
- ecc_encryption: For ECC curve setup, key generation, and encryption/decryption of points.
- utils: For auxiliary calculations, such as computing y-coordinates on the ECC curve.
- plotting: For visualizing the original, encrypted, and decrypted audio signals.

Outputs:
- Encrypted and decrypted audio files are saved to the `data/output/` directory.
- A plot of the original, encrypted, and decrypted signals is saved as an image.
'''


import time
import numpy as np
import tinyec.ec as ec
from audio_processing import load_audio, save_audio
from ecc_encryption import initialize_curve, generate_keys, compute_shared_secret, encrypt_points, decrypt_points
from utils import compute_y_coordinate
from plotting import plot_signals
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# Load and process the audio file
sample_freq, n_samples, signal_array = load_audio(
    "data/input_audio.wav"")
t_audio = n_samples / sample_freq
times = np.linspace(0, t_audio, num=n_samples)

# Initialize the ECC curve
a, b, p, gx, gy, order, cofactor = 56698187605326110043627228396178346077120614539475214109386828188763884139993, \
    17577232497321838841075697789794520262950426058923084567046852300633325438902, \
    76884956397045344220809746629001649093037950200943055203735601445031516197751, \
    63243729749562333355292243550312970334778175571054726587095381623627144114786, \
    38218615093753523893122277964030810387585405539772602581557831887485717997975, \
    115792089210356248762697446949407573529996955224135760342422259061068512044369, 1
curve = initialize_curve(a, b, p, gx, gy, order, cofactor)

# Generate private and public keys for both parties
my_private_key, my_public_key = generate_keys(curve)
recipient_private_key, recipient_public_key = generate_keys(curve)

# Generate shared secret key
shared_secret_key = compute_shared_secret(my_private_key, recipient_public_key)

# Prepare points for encryption
y_audio = signal_array % p
y_coordinates = [compute_y_coordinate(x, a, b, p) for x in y_audio]
plaintext_in_ecc = [(x, y) for x, y in zip(y_audio, y_coordinates)]

# Start the timer for encryption
start_time = time.time()

# Encrypt the points
P1_points = [ec.Point(curve, x=x, y=y) for x, y in plaintext_in_ecc]
encrypted_points = encrypt_points(curve, P1_points, shared_secret_key)

# Measure encryption time
encryption_time = time.time() - start_time

# Start the timer for decryption
start_time = time.time()

# Decrypt the points
shared_secret_recipient = compute_shared_secret(
    recipient_private_key, my_public_key)
decrypted_points = decrypt_points(
    curve, encrypted_points, shared_secret_recipient)

# Measure decryption time
decryption_time = time.time() - start_time

# Prepare arrays for plotting and saving
encrypted_x_values = np.array(
    [(point.x - p) if point.x >= (p / 2 + 1) else point.x for point in encrypted_points])
decrypted_x_values = np.array(
    [(point.x - p) if point.x >= (p / 2 + 1) else point.x for point in decrypted_points])

# Check if decryption was successful
if np.all(decrypted_x_values == signal_array):
    print("Decryption successful: The audio signal has been recovered!")
else:
    print("Decryption failed: The audio signal was not recovered accurately.")

# Print encryption and decryption times
print(f"Encryption time: {encryption_time:.4f} seconds")
print(f"Decryption time: {decryption_time:.4f} seconds")

# Save encrypted and decrypted audio files
scaled_encrypted_signal_array = np.array(
    (encrypted_x_values / np.max(np.abs(encrypted_x_values)) * 32767), dtype=np.int16)
decrypted_signal_array = np.array(decrypted_x_values, dtype=np.int16)
save_audio("data/output/encrypted_audio.wav",
           sample_freq, scaled_encrypted_signal_array)
save_audio("data/output/decrypted_audio.wav",
           sample_freq, decrypted_signal_array)

# Plot the results and save the image
plot_signals(
    times,
    signal_array,
    encrypted_x_values,
    decrypted_x_values,
    save_path="data/output/plot.png"
)
