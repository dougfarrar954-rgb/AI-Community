import numpy as np
import time

# Compare Python list vs NumPy array performance
print("Performance Comparison: Python List vs NumPy Array")
print("=" * 60)

# Python list approach
start = time.time()
python_list = list(range(44100))
doubled_list = [x * 2 for x in python_list]
list_time = time.time() - start

# NumPy approach
start = time.time()
numpy_array = np.arange(44100)
doubled_array = numpy_array * 2
numpy_time = time.time() - start

print(f"Python list: {list_time:.6f} seconds")
print(f"NumPy array: {numpy_time:.6f} seconds")
print(f"NumPy is {list_time / numpy_time:.1f}x faster!")
print()

# Create time array for audio
def create_sample_array(duration, sample_rate=44100):
    """Create time array for audio generation."""
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    return t

# Test with different durations
durations = [0.1, 0.5, 1.0, 2.0]

print("Creating audio time arrays:")
for dur in durations:
    t = create_sample_array(dur)
    print(f"  {dur}s → {len(t)} samples (last value: {t[-1]:.4f}s)")
