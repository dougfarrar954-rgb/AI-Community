# 0.2: Control Flow (if/else, for loops)

## Quick Info
- **Duration:** 1-2 hours
- **Difficulty:** Beginner
- **Prerequisites:** 0.1 Variables and Math
- **Learning Tags:** #python-basics #control-flow #conditionals #loops

---

## Big Idea
Programs need to make decisions and repeat actions. **Conditionals** (`if/else`) let code choose different paths, and **loops** (`for`) let code repeat tasks automatically.

---

## Learning Outcomes
- ✅ Use `if/else` to make decisions in code
- ✅ Write `for` loops to iterate through lists
- ✅ Understand indentation rules in Python
- ✅ Combine conditionals and loops

---

## Core Concepts
- **if/else**: Execute code based on conditions
- **Comparison operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **for loops**: Repeat code for each item in a sequence
- **Indentation**: Python uses spaces/tabs to define code blocks

---

## Main Content

### Part A: Making Decisions with if/else

```python
# Simple if statement
frequency = 440

if frequency > 400:
    print("This is a high note")

# if/else
if frequency == 440:
    print("This is concert A (A4)")
else:
    print("This is not A4")

# if/elif/else for multiple conditions
if frequency < 300:
    print("Bass range")
elif frequency < 1000:
    print("Mid range")
else:
    print("Treble range")
```

**Audio Example**:
```python
# Classify a note based on frequency
note_freq = 523.25  # C5

if note_freq >= 440:
    print("Higher than concert A")
else:
    print("Lower than concert A")
```

### Part B: Repeating with for Loops

```python
# Loop through a list of frequencies
frequencies = [261.63, 293.66, 329.63, 349.23]  # C, D, E, F

for freq in frequencies:
    print(f"Frequency: {freq} Hz")
```

**Output**:
```
Frequency: 261.63 Hz
Frequency: 293.66 Hz
Frequency: 329.63 Hz
Frequency: 349.23 Hz
```

### Part C: Combining Conditionals and Loops

```python
# Filter frequencies above a threshold
frequencies = [100, 440, 880, 200, 1000]

print("High frequencies:")
for freq in frequencies:
    if freq > 400:
        print(f"  {freq} Hz")
```

---

## Code Examples

### Example 1: Octave Calculator
```python
# Check if two frequencies are an octave apart
freq1 = 440
freq2 = 880

if freq2 == freq1 * 2:
    print("These frequencies are exactly one octave apart!")
else:
    print("Not an octave relationship")
```

### Example 2: Generate Octave Series
```python
# Generate 4 octaves above middle C
base_freq = 261.63  # Middle C (C4)

print("Octave series:")
for octave in range(5):  # 0, 1, 2, 3, 4
    freq = base_freq * (2 ** octave)
    print(f"Octave {octave}: {freq:.2f} Hz")
```

---

## Hands-On Project

Create a script called `note_classifier.py` that:

1. Takes a list of frequencies: `[220, 440, 880, 660, 330]`
2. Uses a `for` loop to iterate through each frequency
3. Uses `if/elif/else` to classify each as:
   - "Sub-bass" (< 250 Hz)
   - "Bass" (250-500 Hz)  
   - "Mid" (500-2000 Hz)
   - "High" (> 2000 Hz)
4. Print the classification for each frequency

**Expected Output**:
```
220 Hz: Sub-bass
440 Hz: Bass
880 Hz: Mid
660 Hz: Mid
330 Hz: Bass
```

---

## Checkpoint

Can you answer these?
1. What happens if you forget the `:` after an `if` statement?
2. How do you check if two values are equal? (Hint: Not `=`)
3. What does `range(5)` generate?

---

## Next Steps
- Complete the Hands-On Project
- Move to [0.3: Functions and Lists](./0_3_Functions_Lists.md)
