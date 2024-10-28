import matplotlib.pyplot as plt


def plot_signals(times, original, encrypted, decrypted, save_path=None):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 6))

    ax1.plot(times, original)
    ax1.set_title("Original Signal")
    ax1.set_ylabel("Signal wave")
    ax1.set_xlabel("Time (s)")

    ax2.plot(times, encrypted)
    ax2.set_title("Encrypted Signal")
    ax2.set_ylabel("Signal wave")
    ax2.set_xlabel("Time (s)")

    ax3.plot(times, decrypted)
    ax3.set_title("Decrypted Signal")
    ax3.set_ylabel("Signal wave")
    ax3.set_xlabel("Time (s)")

    plt.tight_layout()

    # Save the plot if a save path is provided
    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved as {save_path}")

    # Display the plot
    plt.show()
