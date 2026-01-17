"""
Audio Helper Functions
Common utilities for audio synthesis and processing.
"""

import numpy as np
import sounddevice as sd
from scipy.io import wavfile

def play_audio(signal, sample_rate=44100):
    """
    Play an audio signal.
    
    Args:
        signal: NumPy array of audio samples
        sample_rate: Sampling rate in Hz (default: 44100)
    """
    sd.play(signal, sample_rate)
    sd.wait()

def save_wav(filename, signal, sample_rate=44100):
    """
    Save audio signal to WAV file.
    
    Args:
        filename: Path to output file
        signal: NumPy array of audio samples
        sample_rate: Sampling rate in Hz (default: 44100)
    """
    # Normalize and convert to 16-bit
    normalized = np.int16(signal / np.max(np.abs(signal)) * 32767)
    wavfile.write(filename, sample_rate, normalized)

def generate_sine(frequency, duration, sample_rate=44100, amplitude=0.5):
    """
    Generate a sine wave.
    
    Args:
        frequency: Frequency in Hz
        duration: Duration in seconds
        sample_rate: Sampling rate in Hz (default: 44100)
        amplitude: Amplitude 0.0-1.0 (default: 0.5)
    
    Returns:
        NumPy array of audio samples
    """
    t = np.linspace(0, duration, int(sample_rate * duration))
    return amplitude * np.sin(2 * np.pi * frequency * t)

def apply_envelope(signal, attack=0.01, decay=0.1, sustain=0.7, release=0.2, sample_rate=44100):
    """
    Apply ADSR envelope to a signal.
    
    Args:
        signal: Input audio signal
        attack: Attack time in seconds
        decay: Decay time in seconds
        sustain: Sustain level (0.0-1.0)
        release: Release time in seconds
        sample_rate: Sampling rate in Hz
    
    Returns:
        Signal with envelope applied
    """
    n_samples = len(signal)
    envelope = np.ones(n_samples)
    
    # Calculate sample counts for each phase
    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    release_samples = int(release * sample_rate)
    sustain_samples = n_samples - attack_samples - decay_samples - release_samples
    
    # Build envelope
    idx = 0
    
    # Attack
    if attack_samples > 0:
        envelope[idx:idx+attack_samples] = np.linspace(0, 1, attack_samples)
        idx += attack_samples
    
    # Decay
    if decay_samples > 0:
        envelope[idx:idx+decay_samples] = np.linspace(1, sustain, decay_samples)
        idx += decay_samples
    
    # Sustain
    if sustain_samples > 0:
        envelope[idx:idx+sustain_samples] = sustain
        idx += sustain_samples
    
    # Release
    if release_samples > 0:
        envelope[idx:idx+release_samples] = np.linspace(sustain, 0, release_samples)
    
    return signal * envelope

def normalize(signal):
    """
    Normalize signal to range [-1, 1].
    
    Args:
        signal: Input audio signal
    
    Returns:
        Normalized signal
    """
    max_val = np.max(np.abs(signal))
    if max_val > 0:
        return signal / max_val
    return signal
