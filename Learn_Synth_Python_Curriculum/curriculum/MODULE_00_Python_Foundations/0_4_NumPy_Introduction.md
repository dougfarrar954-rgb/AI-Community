# 0.4: Introduction to NumPy Arrays

## Quick Info
- **Duration:** 2 hours
- **Difficulty:** Beginner
- **Prerequisites:** 0.1-0.3 completed
- **Learning Tags:** #numpy #arrays #audio-preparation #beginner

---

## Big Idea
**NumPy arrays** are like lists but much faster for numerical operations. They're essential for audio because sound is just arrays of numbers processed very quickly.

---

## Learning Outcomes
- ✅ Understand why NumPy is needed for audio
- ✅ Create NumPy arrays
- ✅ Perform array operations
- ✅ Use NumPy for mathematical operations

---

## Core Concepts
- **NumPy array**: Fast numerical array (vs. Python list)
- **Array operations**: Apply math to entire arrays at once
- **Vectorization**: Processing arrays without loops (much faster)

---

## Main Content

### Part A: Why NumPy for Audio?

**Audio challenge**: 44,100 samples per second means processing 44,100 numbers EVERY SECOND. Python lists are too slow!

**NumPy solution**: Written in C, optimized for speed. Operations on entire arrays at once.

```python
import numpy as np

# Python list (slow)
python_list = [1, 2, 3, 4, 5]

# NumPy array (fast!)
numpy_array = np.array([1, 2, 3, 4, 5])

print(type(python_list))   # <class 'list'>
print(type(numpy_array))   # <class 'numpy.ndarray'>
```

### Part B: Creating NumPy Arrays

```python
import numpy as np

# From a list
frequencies = np.array([440, 494, 523])

# Filled with zeros
silence = np.zeros(100)  # 100 samples of silence

# Filled with ones
ones = np.ones(50)

# Range of values
steps = np.arange(0, 10, 1)  # 0, 1, 2, ..., 9

# Evenly spaced values (VERY important for audio!)
time_points = np.linspace(0, 1, 44100)  # 1 second at 44.1kHz
print(f"Created {len(time_points)} time points")
```

### Part C: Array Operations (The Power of NumPy!)

```python
import numpy as np

# Create array
samples = np.array([0.5, 0.8, 0.3, 0.9])

# Multiply ALL elements at once (no loop needed!)
doubled = samples * 2
print(doubled)  # [1.0, 1.6, 0.6, 1.8]

# Add to ALL elements
shifted = samples + 0.1
print(shifted)  # [0.6, 0.9, 0.4, 1.0]

# Mathematical functions work on entire array
sins = np.sin(samples)
print(sins)
```

**This is MUCH faster than looping!**

### Part D: Audio-Specific NumPy Operations

```python
import numpy as np

# Create 1 second of time points at 44.1kHz
sample_rate = 44100
duration = 1.0
t = np.linspace(0, duration, int(sample_rate * duration))

print(f"Shape: {t.shape}")  # (44100,)
print(f"First value: {t[0]}")  # 0.0
print(f"Last value: {t[-1]}")  # ~1.0
```

---

## Code Examples

### Example 1: Compare List vs NumPy Speed
```python
import numpy as np
import time

# Python list approach (SLOW)
start = time.time()
python_list = list(range(44100))
doubled_list = [x * 2 for x in python_list]
list_time = time.time() - start

# NumPy approach (FAST)
start = time.time()
numpy_array = np.arange(44100)
doubled_array = numpy_array * 2
numpy_time = time.time() - start

print(f"Python list: {list_time:.4f} seconds")
print(f"NumPy array: {numpy_time:.4f} seconds")
print(f"NumPy is {list_time / numpy_time:.1f}x faster!")
```

### Example 2: Prepare for Audio Synthesis
```python
import numpy as np

def prepare_time_array(duration, sample_rate=44100):
    """Create time array for audio generation."""
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    return t

# Use it
t = prepare_time_array(duration=2.0, sample_rate=44100)
print(f"Ready to generate {len(t)} samples ({len(t) / 44100:.1f} seconds)")
```

---

## Hands-On Project

Create a script called `numpy_audio_prep.py` that:

1. Defines a function `create_sample_array(duration, sample_rate)`
2. Returns a NumPy array of time values from 0 to `duration`
3. Test with different durations and sample rates
4. Print array shape and first/last values

**Expected behavior**:
```python
t = create_sample_array(duration=0.5, sample_rate=44100)
# Should create 22050 samples (0.5 * 44100)
print(f"Samples: {len(t)}")  # 22050
print(f"Duration: {t[-1]:.2f} seconds")  # ~0.50
```

---

## Checkpoint

Can you answer these?
1. Why is NumPy faster than Python lists for audio?
2. What does `np.linspace(0, 1, 100)` create?
3. How do you multiply every element in a NumPy array by 2?

---

## Module 0 Complete! 🎉

You now understand:
- ✅ Python variables and math
- ✅ Control flow (if/else, loops)
- ✅ Functions and lists
- ✅ NumPy arrays

**Next**: [Module 1: Foundations](../../MODULE_01_Foundations/MODULE_01_OVERVIEW.md) - Now you'll use these skills to generate your FIRST SOUNDS!
