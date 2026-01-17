# Generate octave series
base_freq = 261.63  # Middle C (C4)

print("Octave series from C4:")
for octave in range(5):
    freq = base_freq * (2 ** octave)
    print(f"  Octave {octave}: {freq:.2f} Hz")

print()

# Classify frequencies
frequencies = [220, 440, 880, 660, 330]

print("Frequency classifications:")
for freq in frequencies:
    if freq < 250:
        classification = "Sub-bass"
    elif freq < 500:
        classification = "Bass"
    elif freq < 2000:
        classification = "Mid"
    else:
        classification = "High"
    
    print(f"  {freq} Hz: {classification}")
