"""
Session Initialization Script
Run this at the start of each learning session to load your progress and get oriented.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

# Get project root and student name
PROJECT_ROOT = Path(__file__).parent
# Get project root and search path for student progress
PROJECT_ROOT = Path(__file__).parent
TEMPLATE_FILE = PROJECT_ROOT / "curriculum" / "PROGRESS_TRACKER.json"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

def load_progress():
    """Load student progress, searching in outputs folder first."""
    # Search for any progress.json files in student portfolios
    personal_files = list(OUTPUTS_DIR.glob("**/progress.json"))
    
    if personal_files:
        if len(personal_files) == 1:
            progress_path = personal_files[0]
        else:
            print("Found multiple student portfolios:")
            for i, path in enumerate(personal_files):
                print(f"  {i+1}. {path.parent.name}")
            choice = input("\nSelect your profile number (or type 'new' for a new one): ")
            if choice.lower() == 'new':
                return create_new_tracker()
            try:
                progress_path = personal_files[int(choice)-1]
            except (ValueError, IndexError):
                print("Invalid choice, starting new tracker...")
                return create_new_tracker()
        
        with open(progress_path, 'r') as f:
            return json.load(f), progress_path
            
    print("⚠️  No progress tracker found. Creating a new one...")
    return create_new_tracker()

def create_new_tracker():
    """Create a new progress tracker for a new student."""
    print("\n--- New Student Setup ---")
    student_name = input("Enter your name: ")
    if not student_name:
        student_name = "Learner"
    
    # Load template
    with open(TEMPLATE_FILE, 'r') as f:
        tracker = json.load(f)
    
    # Customize
    tracker['student_name'] = student_name
    tracker['start_date'] = input("Start date (YYYY-MM-DD) [today]: ") or "2026-01-17"
    
    # Save to outputs folder
    student_dir = OUTPUTS_DIR / student_name.lower().replace(" ", "_")
    student_dir.mkdir(parents=True, exist_ok=True)
    
    progress_path = student_dir / "progress.json"
    with open(progress_path, 'w') as f:
        json.dump(tracker, f, indent=2)
    
    print(f"✅ Created progress tracker at: {progress_path}")
    return tracker, progress_path

def display_progress(progress):
    """Display current progress in a readable format."""
    print("\n" + "="*60)
    print(f"🎓 Welcome back, {progress['student_name']}!")
    print("="*60)
    print()
    
    # Find current module
    current_module = None
    completed_count = 0
    
    for module_id, module_data in progress['modules'].items():
        status = module_data['status']
        
        if status == 'completed':
            completed_count += 1
        elif status == 'in_progress' and current_module is None:
            current_module = (module_id, module_data)
    
    # Summary
    total_modules = len(progress['modules'])
    print(f"📊 Progress: {completed_count}/{total_modules} modules completed")
    print()
    
    # Current work
    if current_module:
        mod_id, mod_data = current_module
        print(f"📍 Currently Working On: Module {mod_id[-2:]} - {mod_data['name']}")
        print(f"   Lessons Completed: {len(mod_data['lessons_completed'])}")
        if mod_data['notes']:
            print(f"   Notes: {mod_data['notes']}")
    else:
        # Find next module to start
        for module_id, module_data in progress['modules'].items():
            if module_data['status'] == 'not_started':
                print(f"🚀 Next Up: Module {module_id[-2:]} - {module_data['name']}")
                break
    
    print()
    print("="*60)
    print()

def suggest_next_steps(progress):
    """Suggest what the student should do next."""
    print("💡 Suggested Next Steps:")
    print()
    
    # Find current module
    for module_id, module_data in progress['modules'].items():
        if module_data['status'] == 'in_progress':
            mod_num = module_id.split('_')[1]
            print(f"1. Continue with Module {mod_num}: {module_data['name']}")
            print(f"   📂 Navigate to: curriculum/MODULE_{mod_num}_{module_data['name'].replace(' ', '_')}/")
            print(f"   💻 Run examples in: examples/module_{mod_num}/")
            print()
            return
        elif module_data['status'] == 'not_started':
            mod_num = module_id.split('_')[1]
            print(f"1. Start Module {mod_num}: {module_data['name']}")
            print(f"   📂 Navigate to: curriculum/MODULE_{mod_num}_{module_data['name'].replace(' ', '_')}/")
            print(f"   📖 Read: MODULE_{mod_num}_OVERVIEW.md")
            print()
            return
    
    print("🎉 All modules completed! Consider working on your capstone project.")
    print()

def display_agent_context(progress):
    """Display information for the Antigravity agent with clear student instructions."""
    
    # Find active or next module
    current_module_name = "Module 00 - Python Foundations"
    for mod_id, mod_data in progress['modules'].items():
        if mod_data['status'] in ['in_progress', 'not_started']:
            current_module_name = f"Module {mod_id[-2:]} - {mod_data['name']}"
            break

    context_block = f"""
🤖 ACTION REQUIRED: COPY AND PASTE THE BLOCK BELOW INTO THE AI CHAT
────────────────────────────────────────────────────────────
Hello! Please adopt the persona of the 'Synth-Tutor Agent' as defined 
in 'prompts/synth_tutor_system.md'. 

I am your student, {progress['student_name']}. 
I am currently on: {current_module_name}

Reference my progress in 'outputs/{progress['student_name'].lower().replace(" ", "_")}/progress.json' 
and guide me through the next lesson in the curriculum. 
Remember to use scaffolding—no full solutions!
────────────────────────────────────────────────────────────
"""
    print(context_block)

def run_preflight_checks():
    """Run environment validation and offer to install missing packages."""
    print("🔍 Running pre-flight environment checks...")
    
    required_packages = ['numpy', 'sounddevice', 'scipy', 'matplotlib']
    missing_packages = []
    
    for pkg in required_packages:
        try:
            __import__(pkg)
        except ImportError:
            missing_packages.append(pkg)
    
    if missing_packages:
        print(f"⚠️  Missing required packages: {', '.join(missing_packages)}")
        choice = input("Would you like me to install them for you? (y/n): ").lower()
        if choice == 'y':
            print("Installing requirements...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
                print("✅ Dependencies installed successfully!")
            except subprocess.CalledProcessError:
                print("❌ Failed to install dependencies. Please run 'pip install -r requirements.txt' manually.")
                return False
        else:
            print("Skipping installation. Note: Some curriculum scripts may not work.")
    else:
        print("✅ Environment looks good!")
    
    print("-" * 60)
    return True

def main():
    """Main session initialization routine."""
    print("🎹 Learn Synth Python - Session Initializer 🐍")
    print()
    
    # 1. Pre-flight checks
    if not run_preflight_checks():
        return
    
    # 2. Load progress
    progress, progress_path = load_progress()
    
    # Display current state
    display_progress(progress)
    
    # Suggest next steps
    suggest_next_steps(progress)
    
    # Agent context
    display_agent_context(progress)
    
    # Helpful commands
    print("📝 Helpful Commands:")
    print("   python tools/validate_environment.py  # Check setup")
    print("   pytest tests/                         # Run tests")
    print("   python start_session.py               # Restart this script")
    print()

if __name__ == "__main__":
    main()
