# 0.3: Functions and Lists

## Quick Info
- **Duration:** 1-2 hours
- **Difficulty:** Beginner
- **Prerequisites:** 0.1 Variables, 0.2 Control Flow
- **Learning Tags:** #python-basics #functions #lists #reusability

---

## Big Idea
**Functions** let you package code into reusable blocks, and **lists** let you store collections of related data. These are essential for organizing audio synthesis code.

---

## Learning Outcomes
- ✅ Define and call functions
- ✅ Use parameters and return values
- ✅ Create and manipulate lists
- ✅ Combine functions with lists

---

## Core Concepts
- **Function**: Reusable block of code with a name
- **Parameters**: Inputs to a function
- **Return value**: Output from a function
- **List**: Ordered collection of items

---

## Main Content

### Part A: Creating Functions

```python
# Simple function
def greet():
    print("Hello, audio programmer!")

# Call the function
greet()  # Output: Hello, audio programmer!

# Function with parameters
def calculate_frequency(note, octave):
    # A4 (440 Hz) is note 9, octave 4
    # Each octave doubles frequency
    base_freq = 440
    steps_from_a4 = note - 9 + (octave - 4) * 12
    freq = base_freq * (2 ** (steps_from_a4 / 12))
    return freq

# Use the function
middle_c_freq = calculate_frequency(0, 4)  # C4
print(f"Middle C: {middle_c_freq:.2f} Hz")
```

### Part B: Working with Lists

```python
# Create a list of frequencies
frequencies = [261.63, 293.66, 329.63, 349.23]

# Access items by index (starts at 0)
first_freq = frequencies[0]  # 261.63
print(f"First frequency: {first_freq} Hz")

# Add to list
frequencies.append(392.00)  # Add G
print(frequencies)

# Get list length
num_notes = len(frequencies)
print(f"We have {num_notes} notes")

# Loop through list
for freq in frequencies:
    print(f"{freq} Hz")
```

### Part C: Functions that Work with Lists

```python
def average_frequency(freq_list):
    """Calculate the average of a list of frequencies."""
    total = sum(freq_list)
    count = len(freq_list)
    return total / count

# Use it
notes = [440, 494, 523]
avg = average_frequency(notes)
print(f"Average: {avg:.2f} Hz")
```

---

## Code Examples

### Example 1: Frequency Converter
```python
def hz_to_midi(frequency):
    """Convert frequency in Hz to MIDI note number."""
    import math
    return 69 + 12 * math.log2(frequency / 440)

# Test it
freq = 523.25  # C5
midi_note = hz_to_midi(freq)
print(f"{freq} Hz = MIDI note {midi_note:.1f}")
```

### Example 2: Generate Chord
```python
def generate_major_chord(root_freq):
    """Generate major chord frequencies (root, major third, fifth)."""
    root = root_freq
    third = root_freq * (2 ** (4/12))  # 4 semitones up
    fifth = root_freq * (2 ** (7/12))  # 7 semitones up
    return [root, third, fifth]

# Generate C major chord
c_major = generate_major_chord(261.63)
print("C Major chord:", c_major)
```

---

## Hands-On Project

Create a script called `chord_builder.py` that:

1. Defines a function `create_scale(root_freq, scale_intervals)`
   - `root_freq`: starting frequency
   - `scale_intervals`: list of semitone steps (e.g., `[0, 2, 4, 5, 7, 9, 11]` for major scale)
2. The function should return a list of frequencies for the scale
3. Test it with C major scale starting at 261.63 Hz

**Example Usage**:
```python
major_intervals = [0, 2, 4, 5, 7, 9, 11, 12]  # Full octave
c_major_scale = create_scale(261.63, major_intervals)
print("C Major Scale:")
for i, freq in enumerate(c_major_scale):
    print(f"  Note {i}: {freq:.2f} Hz")
```

---

## Checkpoint

Can you answer these?
1. What's the difference between defining a function and calling it?
2. How do you add an item to a list?
3. What does a `return` statement do?

---

## Next Steps
- Complete the Hands-On Project
- Move to [0.4: Introduction to NumPy Arrays](./0_4_NumPy_Introduction.md)
