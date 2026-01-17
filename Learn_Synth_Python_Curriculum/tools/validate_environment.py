"""
Environment Validation Tool
Checks if the student's development environment is correctly configured.
"""

import sys
import subprocess
import importlib.util

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    version = sys.version_info
    if version >= (3, 8):
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} detected")
        print("   Minimum Python 3.8 required")
        return False

def check_package(package_name):
    """Check if a package is installed."""
    spec = importlib.util.find_spec(package_name)
    if spec is not None:
        try:
            module = importlib.import_module(package_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"✅ {package_name} {version}")
            return True
        except ImportError:
            print(f"❌ {package_name} (import failed)")
            return False
    else:
        print(f"❌ {package_name} (not installed)")
        return False

def check_audio_output():
    """Test if audio playback works."""
    try:
        import sounddevice as sd
        import numpy as np
        
        # Generate a brief silent test tone
        sample_rate = 44100
        duration = 0.1
        t = np.linspace(0, duration, int(sample_rate * duration))
        test_tone = np.sin(2 * np.pi * 440 * t) * 0.001  # Very quiet
        
        # Try to play it
        sd.play(test_tone, sample_rate)
        sd.wait()
        print("✅ Audio output functional")
        return True
    except Exception as e:
        print(f"❌ Audio output failed: {e}")
        print("   Check your system audio settings")
        return False

def main():
    """Run all validation checks."""
    print("=" * 50)
    print("Synth Python Environment Validator")
    print("=" * 50)
    print()
    
    checks = []
    
    # Check Python version
    print("Checking Python version...")
    checks.append(check_python_version())
    print()
    
    # Check required packages
    print("Checking required packages...")
    required_packages = ['numpy', 'sounddevice', 'scipy', 'matplotlib']
    for package in required_packages:
        checks.append(check_package(package))
    print()
    
    # Check audio output
    print("Testing audio output...")
    checks.append(check_audio_output())
    print()
    
    # Summary
    print("=" * 50)
    if all(checks):
        print("🎉 All checks passed! You're ready to start learning.")
    else:
        print("⚠️  Some checks failed. Please install missing dependencies:")
        print("   pip install -r requirements.txt")
    print("=" * 50)

if __name__ == "__main__":
    main()
