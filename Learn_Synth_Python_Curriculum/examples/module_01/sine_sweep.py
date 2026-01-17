import math
import struct
import wave
import os

# Config
sample_rate = 44100
duration = 5.0  # seconds
start_freq = 100.0  # Hz
end_freq = 2000.0  # Hz
output_dir = "output"
filename = os.path.join(output_dir, "sine_sweep.wav")

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

print(f"Generating {filename}...")
print(f"Sweep from {start_freq}Hz to {end_freq}Hz over {duration}s")

# Open WAV file
with wave.open(filename, 'w') as wav_file:
    # Set parameters: 1 channel (mono), 2 bytes sample width, 44100 framerate
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    total_samples = int(sample_rate * duration)
    
    for i in range(total_samples):
        # Calculate time t (0.0 to duration)
        t = i / sample_rate
        
        # Calculate current frequency (linear interpolation)
        current_freq = start_freq + (end_freq - start_freq) * (t / duration)
        
        # Calculate amplitude (sine wave)
        # Note: We must integrate frequency over time for a proper sweep,
        # but for a simple "chirp" approximation, we can use this formula:
        # phase = 2 * pi * (start_freq * t + 0.5 * (end_freq - start_freq) / duration * t^2)
        
        phase = 2 * math.pi * (start_freq * t + 0.5 * (end_freq - start_freq) / duration * t * t)
        sample_value = math.sin(phase)
        
        # Scale to 16-bit integer range (-32767 to 32767)
        # We multiply by 32000 to leave a little headroom
        int_sample = int(sample_value * 32000)
        
        # Pack as binary data (little-endian short)
        data = struct.pack('<h', int_sample)
        wav_file.writeframes(data)

print("Done! Play the file to hear the sweep.")
