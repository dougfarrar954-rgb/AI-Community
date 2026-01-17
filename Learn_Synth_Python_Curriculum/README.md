 # Learn Synth Python

> **A self-sufficient, self-guided course for learning Python through audio synthesis**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository is a **complete Python learning curriculum** that teaches programming concepts through the creative lens of **audio synthesis and digital signal processing (DSP)**. Every lesson connects Python skills directly to sound generation, making abstract concepts immediately tangible and audible.

### What Makes This Different?

- 🎵 **Hear Your Code**: Every concept produces sound—turning abstract logic into audible results
- 🤖 **AI-Powered Tutoring**: Designed to work with Google Antigravity agent for guided, scaffolded learning
- 📚 **Self-Guided**: Complete with all curriculum files, examples, and tests—no external dependencies
- 🔧 **Production-Ready**: Professional test suite, validation tools, and audio helpers included
- 🌉 **Skills Transfer**: Final module bridges audio synthesis to general programming (data science, game dev, finance)

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/AI-Community-Shared/Learn_Synth_Python_Curriculum.git
cd Learn_Synth_Python_Curriculum

# Create virtual environment (Optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Start Your Learning Session (CRITICAL)

To begin, run the session initializer. **This script will validate your environment, create your progress tracker, and provide a text block for you to paste into the AI chat to initialize your tutor.**

```bash
python start_session.py
```

### 3. Your First Sound

```bash
python examples/module_01/white_noise.py
```

See [GETTING_STARTED.md](GETTING_STARTED.md) for detailed setup instructions.

## Curriculum Structure

The course is organized into modules progressing from absolute Python basics to complete synthesizers. **Absolute beginners should start with Module 0.**

| Module | Topic | Python Concepts | Audio Concepts |
|--------|-------|----------------|----------------|
| 0 | **Python Foundations** | Variables, Loops, Functions | Audio calculations, logic |
| 1 | **Digital Foundations** | NumPy arrays, types | Sampling, bit depth, white noise |
| 2 | **Waveforms** | Arithmetic, linspace | Sine, square, sawtooth, triangle |
| 3 | **Envelopes** | Class structures | ADSR, amplitude shaping |
| 4 | **Sequencing** | Timing, beat math | Patterns, rhythms, BPM |
| 5 | **Additive Synth** | Iteration, summation | Harmonics, partials, timbre |
| 6 | **Filters** | Signal processing | Low-pass, high-pass, resonance |
| 7 | **LFOs** | Modulation logic | Tremolo, vibrato, depth |
| 8 | **Effects** | Buffers, delays | Echo, reverb, feedback |
| 9 | **Sampling** | File I/O, binary data | WAV files, playback, triggers |
| 10 | **Generative** | Randomness, probability | Procedural composition |
| 11 | **GUI** | Event handling | Real-time parameter control |
| 12 | **MIDI** | Protocols, bitwise math | Note input, velocity, polyphony |
| 13 | **Bridge to General** | **Transfer to**: Data science, game dev, finance | Pattern extraction, abstraction |

**📖 Start Here**: [curriculum/MODULE_00_Python_Foundations/MODULE_00_OVERVIEW.md](curriculum/MODULE_00_Python_Foundations/MODULE_00_OVERVIEW.md)

## Learning Pathways

### With Antigravity Agent (Recommended)

The curriculum is designed to work with **Google Antigravity** as your AI tutor:

1. Open this project in VS Code with Antigravity extension
2. Run `python start_session.py` in the terminal
3. **Copy the 'ACTION REQUIRED' block** from the terminal and paste it into the Antigravity chat
4. The agent will adopt the **Synth-Tutor** persona and guide you through your current module

**Teaching Mode**: The agent uses the [Synth-Tutor system prompt](prompts/synth_tutor_system.md) which emphasizes:
- 🧩 Scaffolding (hints, not answers)
- 🔊 Audio-first learning (always connecting code to sound)
- 🐛 Guided debugging (discovery-based problem solving)

### Self-Guided Learning

You can also follow the curriculum independently:

1. Navigate to `curriculum/MODULE_01_Foundations/`
2. Read `MODULE_01_OVERVIEW.md`
3. Follow lessons sequentially: `1_1`, `1_2`, `1_3`, `1_4`
4. Run corresponding example scripts in `examples/module_01/`
5. Complete checkpoint projects

**Track Progress**: Copy `curriculum/PROGRESS_TRACKER.json` to your own file and update as you complete modules.

## Repository Structure

```
Learn_Synth_Python_Curriculum/
├── curriculum/              # All lesson files and module content
│   ├── MODULE_01_Foundations/
│   ├── MODULE_02_Waveforms/
│   ├── ...
│   ├── MODULE_13_Bridge_to_General_Python/
│   └── CURRICULUM_MASTER.md
├── prompts/                 # AI agent system prompts
│   ├── synth_tutor_system.md
│   ├── week_scaffolding_prompts.md
│   └── listening_test_prompts.md
├── examples/                # Working Python scripts for each module
│   ├── module_01/
│   ├── module_02/
│   └── ...
├── tools/                   # Utilities and helpers
│   ├── validate_environment.py
│   └── audio_helpers.py
├── tests/                   # Automated test suite
│   └── test_examples.py
├── docs/                    # Additional documentation
│   ├── ANTIGRAVITY_SETUP.md
│   └── STUDENT_GUIDE.md
└── outputs/                 # Student portfolios (gitignored)
```

## Key Files

- **[GETTING_STARTED.md](GETTING_STARTED.md)**: Installation and setup guide
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: How to contribute to the project
- **[docs/STUDENT_GUIDE.md](docs/STUDENT_GUIDE.md)**: Learning tips and strategies
- **[docs/ANTIGRAVITY_SETUP.md](docs/ANTIGRAVITY_SETUP.md)**: Full Antigravity integration guide

## Testing

Run the automated test suite to verify all examples work:

```bash
pytest tests/
```

## Contributing

We welcome contributions! Here are ways to help:

- 🐛 Report bugs or suggest improvements via GitHub Issues
- 📝 Add new examples or exercises
- 🎨 Create listening test audio files
- 📚 Improve documentation
- ✅ Add more test coverage

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for the **Google Antigravity** platform
- Curriculum designed by AI community collaboration
- Inspired by the intersection of music, code, and learning

---

**Ready to learn Python through sound?** 🎹🐍

[Get Started →](GETTING_STARTED.md)
