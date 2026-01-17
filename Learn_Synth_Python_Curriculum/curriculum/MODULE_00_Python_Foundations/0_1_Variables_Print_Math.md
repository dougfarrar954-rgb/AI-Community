# 0.1: Variables, Print, and Basic Math

## Quick Info
- **Duration:** 1-2 hours
- **Difficulty:** Beginner
- **Prerequisites:** None
- **Learning Tags:** #python-basics #variables #print

---

## Big Idea
Python can act as a powerful calculator, and you can store calculation results in **variables** to use them later.

---

## Learning Outcomes
- ✅ Understand what variables are and how to create them
- ✅ Use `print()` to display output
- ✅ Perform basic math operations (+, -, *, /, **)

---

## Core Concepts
- **Variables**: Named containers for storing data
- **Data Types**: Numbers (integers and floats)
- **print() function**: Displays output to the console
- **Math operators**: +, -, *, /, **, %

---

## Main Content

### Part A: Python as a Calculator

Open a Python interactive shell or create a file called `calculator.py`:

```python
# Basic math
5 + 3        # Addition: 8
10 - 4       # Subtraction: 6
7 * 6        # Multiplication: 42
20 / 5       # Division: 4.0
2 ** 3       # Exponent (2 to the power of 3): 8
```

**Try it yourself**: What is 15 * 12?

### Part B: Storing Values in Variables

Instead of just calculating, we can **save** results:

```python
frequency = 440
duration = 2.5
volume = 0.8

print(frequency)  # Output: 440
```

**Variable naming rules**:
- Use lowercase with underscores: `sample_rate`
- No spaces: `my value` ❌ → `my_value` ✅  
- Start with a letter: `1_variable` ❌ → `variable_1` ✅

### Part C: Using Variables in Calculations

Once you have variables, you can do math with them:

```python
sample_rate = 44100
duration = 2

total_samples = sample_rate * duration
print(total_samples)  # Output: 88200
```

This is **exactly** what we'll do for audio: calculate how many sound samples we need!

---

## Code Examples

### Example 1: Audio Calculation (No Sound Yet)
```python
# Calculate how many samples we need for a 3-second audio file
sample_rate = 44100  # Standard audio quality
duration = 3         # Seconds

total_samples = sample_rate * duration
print(f"We need {total_samples} samples for {duration} seconds of audio")
```

**Run this and see**: `We need 132300 samples for 3 seconds of audio`

### Example 2: Note Frequency Calculator
```python
# Calculate frequency of musical notes
middle_c = 261.63  # Hz
octave_ratio = 2

higher_c = middle_c * octave_ratio
print(f"One octave higher: {higher_c} Hz")
```

---

## Hands-On Project

Create a script called `my_calculator.py` that:
1. Stores your age in a variable
2. Calculates how many days you've been alive (approximately: age * 365)
3. Prints the result with a message

**Example output**: `"I am approximately 9125 days old!"`

---

## Checkpoint

Can you answer these?
1. What symbol is used for multiplication in Python?
2. What is the result of `10 / 3`? (Try it!)
3. How do you display a variable's value?

---

## Next Steps
- Complete the Hands-On Project
- Move to [0.2: Control Flow](./0_2_Control_Flow.md)
