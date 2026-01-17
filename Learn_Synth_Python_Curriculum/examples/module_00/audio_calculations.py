# Calculate how many samples we need for a 3-second audio file
sample_rate = 44100  # Standard audio quality
duration = 3         # Seconds

total_samples = sample_rate * duration
print(f"We need {total_samples} samples for {duration} seconds of audio")

print()

# Calculate frequency of musical notes
middle_c = 261.63  # Hz
octave_ratio = 2

higher_c = middle_c * octave_ratio
print(f"Middle C: {middle_c} Hz")
print(f"One octave higher: {higher_c} Hz")
