import numpy as np
from scipy.io import wavfile
import os

# Create output directory
os.makedirs('output', exist_ok=True)

def generate_white_noise(duration, sample_rate=44100, amplitude=0.3):
    """
    Generate white noise.
    
    Args:
        duration: Length in seconds
        sample_rate: Samples per second  
        amplitude: Volume (0.0 to 1.0)
    
    Returns:
        NumPy array of audio samples
    """
    num_samples = int(duration * sample_rate)
    noise = np.random.uniform(-1.0, 1.0, num_samples)
    return noise * amplitude

def save_to_wav(audio_samples, filename, sample_rate=44100):
    """Save audio samples to WAV file."""
    # Normalize if needed
    max_val = np.max(np.abs(audio_samples))
    if max_val > 1.0:
        print(f"⚠️  Normalizing audio (was {max_val:.2f})")
        audio_samples = audio_samples / max_val
    
    # Convert to 16-bit for WAV
    audio_int16 = np.int16(audio_samples * 32767)
    
    # Save
    wavfile.write(filename, sample_rate, audio_int16)
    print(f"✅ Saved: {filename}")

# Generate white noise at different amplitudes
print("Generating white noise samples...")
print()

for amp in [0.1, 0.3, 0.7]:
    noise = generate_white_noise(duration=2.0, amplitude=amp)
    filename = f'output/white_noise_amp{int(amp*10)}.wav'
    save_to_wav(noise, filename)
    print(f"   Amplitude: {amp}, Samples: {len(noise)}")
    print()

print("Done! Listen to the files in the output/ folder.")
