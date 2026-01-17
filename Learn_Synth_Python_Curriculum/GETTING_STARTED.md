# Getting Started with Learn Synth Python

Welcome to **Learn Synth Python**! This guide will help you set up your environment and start your journey learning Python through audio synthesis.

## Prerequisites

- **Python 3.8 or higher**
- **Speakers or headphones** (for audio playback)
- **Code editor** (VS Code recommended)
- **Git** (for cloning the repository)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/AI-Community-Shared/Learn_Synth_Python_Curriculum.git
cd Learn_Synth_Python_Curriculum
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Validate Your Environment

```bash
python tools/validate_environment.py
```

You should see:
```
✅ Python 3.x.x detected
✅ numpy x.x.x
✅ sounddevice x.x.x
✅ scipy x.x.x
✅ matplotlib x.x.x
✅ Audio output functional
🎉 All checks passed! You're ready to start learning.
```

## Using with Antigravity

If you're using the **Google Antigravity** AI agent as your tutor:

1. Open this project folder in VS Code with the Antigravity extension
2. The agent will automatically reference the curriculum files
3. Ask the agent: *"I want to start Module 1"*
4. The agent will guide you through the lessons step-by-step

The agent follows these teaching principles:
- **Scaffolding**: Provides hints, not complete solutions
- **Audio-First**: Always connects concepts to sound
- **Hands-On**: Emphasizes experimentation and listening

## Self-Guided Learning (Without Antigravity)

You can also follow the curriculum independently:

1. Navigate to `curriculum/MODULE_01_Foundations/`
2. Open `MODULE_01_OVERVIEW.md` to see the module outline
3. Follow lessons in order: `1_1`, `1_2`, `1_3`, `1_4`
4. Run example scripts in `examples/module_01/`
5. Complete the checkpoint projects

## Running Your First Script

Let's test that everything works:

```bash
python examples/module_01/sine_wave.py
```

You should hear a pure sine tone! 🎵

## Next Steps

- Read the [Student Guide](docs/STUDENT_GUIDE.md) for learning tips
- Explore [Module 1: Foundations](curriculum/MODULE_01_Foundations/)
- Join the community discussions on GitHub

## Troubleshooting

### No Audio Output
- Check your system volume
- Verify your default audio device is set correctly
- Try running `python tools/validate_environment.py` again

### Import Errors
- Make sure you activated your virtual environment
- Run `pip install -r requirements.txt` again
- Check Python version with `python --version` (must be 3.8+)

### Script Errors
- Ensure you're running scripts from the project root directory
- Check that all dependencies are installed
- Open an issue on GitHub if problems persist

## Getting Help

- **GitHub Issues**: Report bugs or ask questions
- **Discussions**: Share your projects and connect with learners
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

Happy learning! 🎹🐍
