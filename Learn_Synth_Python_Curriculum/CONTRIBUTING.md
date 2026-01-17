# Contributing to Learn Synth Python

Thank you for your interest in contributing to this project! This curriculum is designed to be a community-driven resource for learning Python through audio synthesis.

## How to Contribute

### 1. Report Issues
If you find bugs, typos, or have suggestions:
- Open an issue on GitHub
- Describe the problem clearly
- Include which module/lesson is affected
- Provide steps to reproduce (if applicable)

### 2. Improve Documentation
- Fix typos or clarify explanations
- Add additional examples
- Improve code comments
- Enhance README files

### 3. Add New Content
- Create new example scripts
- Develop additional exercises
- Add audio examples (via external links)
- Contribute listening test materials

### 4. Code Contributions
- All Python code should follow PEP 8 style guidelines
- Include docstrings for functions and classes
- Test your code before submitting
- Run `pytest` to ensure all tests pass

## Submission Guidelines

### Pull Request Process
1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test your changes locally
5. Commit with a clear message: `git commit -m "Add: description of changes"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Open a Pull Request

### Code Standards
- **Python Version**: 3.8+
- **Dependencies**: Use only libraries in `requirements.txt`
- **Audio Files**: Do NOT commit `.wav`/`.mp3` files directly
  - Instead, provide external links (Google Drive, Dropbox, etc.)
- **Documentation**: Update relevant README files when adding features

### Module Structure
When adding new lessons, follow this structure:
```
curriculum/MODULE_XX_Name/
├── X_Y_Lesson_Title.md
├── MODULE_XX_OVERVIEW.md
└── examples/
    └── example_script.py
```

### Testing
- Run all example scripts to ensure they execute without errors
- Test on Python 3.8, 3.9, 3.10, 3.11
- Verify audio output sounds correct

## Community Standards
- Be respectful and inclusive
- Provide constructive feedback
- Help others learn
- Celebrate diverse perspectives

## Questions?
- Open a GitHub Discussion
- Tag issues with `question` label
- Reach out to maintainers

Thank you for helping make Python accessible through sound! 🎹🐍
