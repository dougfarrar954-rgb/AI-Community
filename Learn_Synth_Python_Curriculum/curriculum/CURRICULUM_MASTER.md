# Python Synth Curriculum Master

## Introduction
This master document outlines the 13-module journey from Python basics to advanced synthesizer design.

---

## Level 1: Digital Oscillators — Variables and NumPy Arrays

### Objective
Understand how Python variables and NumPy arrays represent audio data by synthesizing a low-frequency pulse.

### 1.1 The Science of Sample Rates
To generate sound digitally, we represent continuous air pressure as a discrete sequence of numbers. 
- **Sample Rate**: The number of values (samples) we process per second (standard is 44,100 Hz).
- **Arrays**: In Python, we store these sequences in **NumPy Arrays**, which allow us to perform mathematical operations on thousands of samples simultaneously.

### 1.2 Implementation: The Sine Wave
We use the `numpy` library to generate a timeline and a mathematical sine function to create the oscillation.

```python
import numpy as np
import sounddevice as sd

# DATA DEFINITION
# These variables control the properties of our digital signal
sample_rate = 44100  # Samples per second
duration = 0.5       # Duration in seconds
frequency = 50       # Cycles per second (Hz)

# SIGNAL GENERATION
# np.linspace creates an array representing the timeline of our sound
t = np.linspace(0, duration, int(sample_rate * duration))

# The Sine Function: Generates values between -1.0 and 1.0
# Formula: sin(2 * pi * f * t)
signal = np.sin(2 * np.pi * frequency * t)

# AMPLITUDE ENVELOPE
# We apply an exponential decay to avoid digital clicking and shape the sound
envelope = np.exp(-5 * t)
processed_signal = signal * envelope

# OUTPUT
sd.play(processed_signal, sample_rate)
sd.wait()
```

### Technical Tasks for Level 1

1. **Variable Manipulation**: Modify the `frequency` variable. Observe how higher values create more cycles in the same timeframe, resulting in a higher pitch.
2. **Array Exploration**: Print the `t` array to see the raw floating-point values that represent the timeline.
3. **Envelope Shaping**: Change the constant in `np.exp(-5 * t)`. A higher number (e.g., `-20`) will create a sharper, shorter "pluck" sound.

### References
- [Python NumPy: Array Basics](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Digital Audio Fundamentals](https://manual.audacityteam.org/man/digital_audio.html)
- [SoundDevice API Reference](https://python-sounddevice.readthedocs.io/)

---

## Module Index
- [Module 01: Foundations](./MODULE_01_Foundations/README.md)
- [Module 02: Waveforms](./MODULE_02_Waveforms/README.md)
- [Module 03: Envelopes](./MODULE_03_Envelopes/README.md)
- Module 04: Sequencing
- Module 05: Additive Synthesis
- Module 06: Filters
- Module 07: LFOs & Modulation
- Module 08: Effects (Delay/Reverb)
- Module 10: Generative Logic
- Module 11: GUI Design
- Module 12: MIDI Implementation
- Module 13: Final Project: The PolySynth
