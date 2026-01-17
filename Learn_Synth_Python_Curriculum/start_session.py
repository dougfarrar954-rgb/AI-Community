"""
Session Initialization Script
Run this at the start of each learning session to load your progress and get oriented.
"""

import json
import os
from pathlib import Path

# Get project root and student name
PROJECT_ROOT = Path(__file__).parent
PROGRESS_FILE = PROJECT_ROOT / "curriculum" / "PROGRESS_TRACKER.json"

def load_progress():
    """Load student progress from JSON file."""
    if not PROGRESS_FILE.exists():
        print("⚠️  No progress tracker found. Creating a new one...")
        create_new_tracker()
        return load_progress()
    
    with open(PROGRESS_FILE, 'r') as f:
        return json.load(f)

def create_new_tracker():
    """Create a new progress tracker for a new student."""
    student_name = input("Enter your name: ")
    
    # Load template
    template_path = PROJECT_ROOT / "curriculum" / "PROGRESS_TRACKER.json"
    with open(template_path, 'r') as f:
        tracker = json.load(f)
    
    # Customize
    tracker['student_name'] = student_name
    tracker['start_date'] = input("Start date (YYYY-MM-DD): ")
    
    # Save to outputs folder
    output_dir = PROJECT_ROOT / "outputs" / "student_portfolio" / student_name.lower().replace(" ", "_")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    progress_path = output_dir / "progress.json"
    with open(progress_path, 'w') as f:
        json.dump(tracker, f, indent=2)
    
    print(f"✅ Created progress tracker at: {progress_path}")
    return tracker

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

def display_agent_context():
    """Display information for the Antigravity agent."""
    print("🤖 For Antigravity Agent:")
    print("─" * 60)
    print("This student's progress has been loaded into context.")
    print("Reference this information when providing instruction.")
    print("Adjust difficulty and pacing based on completed modules.")
    print("─" * 60)
    print()

def main():
    """Main session initialization routine."""
    print()
    print("🎹 Learn Synth Python - Session Initializer 🐍")
    print()
    
    # Load progress
    progress = load_progress()
    
    # Display current state
    display_progress(progress)
    
    # Suggest next steps
    suggest_next_steps(progress)
    
    # Agent context
    display_agent_context()
    
    # Helpful commands
    print("📝 Helpful Commands:")
    print("   python tools/validate_environment.py  # Check setup")
    print("   pytest tests/                         # Run tests")
    print("   python start_session.py               # Restart this script")
    print()

if __name__ == "__main__":
    main()
