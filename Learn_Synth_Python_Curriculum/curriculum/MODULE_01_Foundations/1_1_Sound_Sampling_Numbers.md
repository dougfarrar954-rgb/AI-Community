# 1.1: How Sound Becomes Numbers

## Quick Info
- **Duration:** 1-2 hours
- **Difficulty:** Beginner
- **Prerequisites:** Module 0 completed
- **Learning Tags:** #audio-basics #digital-signal #sampling #numpy

---

## Big Idea
Sound is continuous waves traveling through air. Computers can't store continuous data—they store discrete numbers. **Digital audio** is the process of measuring (sampling) sound waves at regular intervals and storing those measurements as numbers.

---

## Learning Outcomes
- ✅ Understand how analog sound becomes digital
- ✅ Learn what sample rate and bit depth mean
- ✅ Create and play your first audio: white noise
- ✅ Save audio to a WAV file

---

## Core Concepts

### Sample Rate (Hz)
**How often we measure the wave per second.**

- 44,100 Hz (44.1 kHz): CD quality, 44,100 samples per second
- 48,000 Hz (48 kHz): Video/film standard
- 96,000 Hz (96 kHz): High-resolution audio

**Rule**: Sample rate must be at least 2x the highest frequency you want to capture (Nyquist theorem).

### Bit Depth
**Precision of each sample measurement.**

- 16-bit: 65,536 possible values (CD quality)
- 24-bit: 16,777,216 possible values (professional recording)
- 32-bit float: Virtually unlimited precision (DAW processing)

### Amplitude
**Loudness of the sound.**

In digital audio (float format), amplitude ranges from:
- `-1.0` = maximum negative pressure
- `0.0` = silence (no pressure)
- `+1.0` = maximum positive pressure

**Clipping**: When amplitude exceeds ±1.0, distortion occurs.

---

## Main Content

### Part A: How Many Samples Do We Need?

```python
import numpy as np

# Calculate total samples needed
sample_rate = 44100  # Hz (samples per second)
duration = 3.0       # seconds

total_samples = int(sample_rate * duration)
print(f"For {duration} seconds at {sample_rate} Hz:")
print(f"We need {total_samples} samples")
print(f"That's {total_samples:,} numbers!")
```

**Output**: `For 3.0 seconds at 44100 Hz: We need 132300 samples`

### Part B: Creating an Array of Audio Samples

```python
import numpy as np

# Create 1 second of silence (all zeros)
sample_rate = 44100
duration = 1.0

silence = np.zeros(int(sample_rate * duration))
print(f"Created {len(silence)} samples of silence")
print(f"Shape: {silence.shape}")
print(f"First 10 samples: {silence[:10]}")
```

### Part C: White Noise - Your First Sound!

**White noise** contains all frequencies at equal power. It's pure randomness!

```python
import numpy as np

def generate_white_noise(duration, sample_rate=44100, amplitude=0.3):
    """
    Generate white noise.
    
    Args:
        duration: Length in seconds
        sample_rate: Samples per second
        amplitude: Volume (0.0 to 1.0, typically keep below 0.5)
    
    Returns:
        NumPy array of audio samples
    """
    num_samples = int(duration * sample_rate)
    
    # Random values between -1 and +1
    noise = np.random.uniform(-1.0, 1.0, num_samples)
    
    # Scale by amplitude to avoid it being too loud
    noise = noise * amplitude
    
    return noise

# Generate 2 seconds of white noise
noise = generate_white_noise(duration=2.0, amplitude=0.3)
print(f"Generated {len(noise)} samples")
print(f"Min value: {np.min(noise):.3f}")
print(f"Max value: {np.max(noise):.3f}")
```

---

## Project: White Noise Generator

Create a complete white noise generator that saves to a WAV file.

```python
import numpy as np
from scipy.io import wavfile

def generate_white_noise(duration, sample_rate=44100, amplitude=0.3):
    """Generate white noise array."""
    num_samples = int(duration * sample_rate)
    noise = np.random.uniform(-1.0, 1.0, num_samples)
    return noise * amplitude

def save_to_wav(audio_samples, filename, sample_rate=44100):
    """
    Save audio samples to WAV file.
    
    Audio must be in range [-1.0, 1.0] (float32)
    """
    # Normalize if needed
    max_val = np.max(np.abs(audio_samples))
    if max_val > 1.0:
        print(f"Warning: Normalizing audio (was {max_val:.2f})")
        audio_samples = audio_samples / max_val
    
    # Convert to 16-bit integer format for WAV
    audio_int16 = np.int16(audio_samples * 32767)
    
    # Save
    wavfile.write(filename, sample_rate, audio_int16)
    print(f"✅ Saved: {filename}")

# Generate and save
noise = generate_white_noise(duration=3.0, amplitude=0.3)
save_to_wav(noise, 'white_noise.wav', sample_rate=44100)
```

**Listen to your creation!** Open `white_noise.wav` in your media player.

---

## Listening Test

1. Generate white noise at different amplitudes (0.1, 0.3, 0.7)
2. Listen to each
3. **Describe**: What happens to the loudness?
4. **Predict**: What happens if amplitude > 1.0?

---

## Checkpoint

Can you answer these?
1. How many samples are in 1 second of 48kHz audio?
2. What does "clipping" mean?
3. Why is white noise called "white"? (Hint: it contains all frequencies, like white light)

---

## Next Steps
- Complete the white noise project
- Try different durations and amplitudes
- Move to [1.2: Your First Sine Wave](./1_2_First_Sine_Wave.md)
