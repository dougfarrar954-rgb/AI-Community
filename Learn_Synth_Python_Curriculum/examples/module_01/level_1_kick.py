import numpy as np
import sounddevice as sd
import os

# LEVEL 1: VARIABLE DEFINITION
# These are the "settings" for our sound
sample_rate = 44100  # How many samples per second
duration = 0.5       # The length of the kick in seconds
frequency = 50       # The base frequency of the kick (Low 'G')

print("🥁 LEVEL 1: Creating an 808-style kick drum...")
print(f"Sample Rate: {sample_rate} Hz")
print(f"Duration: {duration} seconds")
print(f"Base Frequency: {frequency} Hz\n")

# CREATING THE TIMELINE (The "Bar")
# np.linspace creates an array of time points from 0 to 0.5 seconds
t = np.linspace(0, duration, int(sample_rate * duration))

# GENERATING THE WAVE (The "Hit")
# A kick is just a sine wave that fades out
kick_wave = np.sin(2 * np.pi * frequency * t)

# APPLYING AN ENVELOPE (The "Fade")
# We multiply by a fading array to stop the sound from clicking
envelope = np.exp(-5 * t)
final_kick = kick_wave * envelope

# Optional: Save to file
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Save as WAV using scipy if available, otherwise just play
try:
    from scipy.io import wavfile
    output_path = os.path.join(output_dir, "level_1_kick.wav")
    # Normalize and convert to 16-bit
    normalized = np.int16(final_kick / np.max(np.abs(final_kick)) * 32767)
    wavfile.write(output_path, sample_rate, normalized)
    print(f"✅ Saved to: {output_path}")
except ImportError:
    print("⚠️  scipy not installed - skipping WAV export")

# PLAY IT
print("🔊 Playing kick drum...")
sd.play(final_kick, sample_rate)
sd.wait()
print("✅ Done!\n")
print("💡 TIP: Try changing the 'frequency' variable to hear different kick tones!")
print("   - Lower frequencies (30-40 Hz) = Sub-bass kick")
print("   - Higher frequencies (60-80 Hz) = Punchy kick")
