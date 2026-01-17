import math

def generate_major_chord(root_freq):
    """Generate major chord frequencies (root, major third, fifth)."""
    root = root_freq
    third = root_freq * (2 ** (4/12))  # 4 semitones up
    fifth = root_freq * (2 ** (7/12))  # 7 semitones up
    return [root, third, fifth]

def create_scale(root_freq, scale_intervals):
    """Create a scale from root frequency and interval pattern."""
    scale = []
    for interval in scale_intervals:
        freq = root_freq * (2 ** (interval / 12))
        scale.append(freq)
    return scale

# Generate C major chord
c_major_chord = generate_major_chord(261.63)
print("C Major Chord:")
for i, freq in enumerate(c_major_chord):
    note_names = ['C', 'E', 'G']
    print(f"  {note_names[i]}: {freq:.2f} Hz")

print()

# Generate C major scale
major_intervals = [0, 2, 4, 5, 7, 9, 11, 12]
c_major_scale = create_scale(261.63, major_intervals)
print("C Major Scale:")
note_names = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
for i, freq in enumerate(c_major_scale):
    print(f"  {note_names[i]}: {freq:.2f} Hz")
