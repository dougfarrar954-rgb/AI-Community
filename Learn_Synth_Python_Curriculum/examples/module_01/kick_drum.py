import math
import struct
import wave
import os

# Config
sample_rate = 44100
duration = 0.5  # seconds (short for a kick)
start_freq = 150.0  # Hz (attack)
end_freq = 50.0    # Hz (body)
decay_rate = 10.0  # How fast the pitch drops
output_dir = "output"
filename = os.path.join(output_dir, "kick_drum.wav")

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

print(f"Generating {filename}...")

# Open WAV file
with wave.open(filename, 'w') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    total_samples = int(sample_rate * duration)
    
    for i in range(total_samples):
        t = i / sample_rate
        
        # --- Pitch Envelope (Exponential Decay) ---
        # Frequency drops quickly from start_freq to end_freq
        curr_freq = end_freq + (start_freq - end_freq) * math.exp(-decay_rate * t)
        
        # --- Amplitude Envelope (Simple Linear Fadedown) ---
        # Volume goes from 1.0 to 0.0 over the duration
        amp = 1.0 - (t / duration)
        if amp < 0: amp = 0
        
        # Generate Sine Wave
        # Since frequency is changing, we technically need to integrate phase,
        # but for short percussive sounds, strict integration is often skipped 
        # in simple tutorials. However, let's do a simple phase accumulator for correctness.
        # (Actually, for a purely static script without a class, we'll use the integral approximation)
        
        # Integral of (A*exp(-kt) + B) dt = -(A/k)*exp(-kt) + Bt
        # Frequency function f(t) = end + (start-end)e^(-decay*t)
        # Phase phi(t) = 2*pi * integral(f(t))
        # phi(t) = 2*pi * [ end*t - ((start-end)/decay) * e^(-decay*t) ]
        
        A = (start_freq - end_freq)
        k = decay_rate
        B = end_freq
        
        phase = 2 * math.pi * (B * t - (A / k) * math.exp(-k * t))
        
        sample_value = math.sin(phase) * amp
        
        int_sample = int(sample_value * 32000)
        data = struct.pack('<h', int_sample)
        wav_file.writeframes(data)

print("Done! Play the file to hear the kick.")
