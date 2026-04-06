# Development Journal

All interactions logged in chronological order (oldest first).

---

### **Interaction 1: Project Initialization & First Updates**
- **Agent Version**: 2.2
- **Date**: 30-03-2026 14:30
- **User**: Ahtshm2004
- **Prompt**: "implement a simple python application that will displays 10 squares moving around randomly on the canvas"
- **CoPilot Mode**: Edit
- **CoPilot Model**: GitHub Copilot
- **Socratic Mode**: OFF
- **Changes Made**: Created `main.py` with pygame demo (10 moving squares), added `requirements.txt` (pygame), created `README.md` with setup instructions.
- **Context and Reasons for Changes**: Initial project implementation to demonstrate random square movement with wall bouncing physics. Used frame-rate-independent movement (`dt` scaling) for consistent animation across different FPS.

---

### **Interaction 2: Scaling to 100 Squares**
- **Agent Version**: 2.2
- **Date**: 30-03-2026 14:45
- **User**: Ahtshm2004
- **Prompt**: "Increment the number of boxes to 100"
- **CoPilot Mode**: Edit
- **CoPilot Model**: GitHub Copilot
- **Socratic Mode**: OFF
- **Changes Made**: Updated `NUM_SQUARES` from 10 to 100 in `main.py`.
- **Context and Reasons for Changes**: Simple configuration update to demonstrate animation with larger number of objects.

---

### **Interaction 3: Configuration Adjustments**
- **Agent Version**: 2.2
- **Date**: 30-03-2026 15:00
- **User**: Ahtshm2004
- **Prompt**: "The global min size should be 300, and the global max size should be 600. and the speed should be around 100"
- **CoPilot Mode**: Edit
- **CoPilot Model**: GitHub Copilot
- **Socratic Mode**: OFF
- **Changes Made**: Added global constants `MIN_SIZE=300`, `MAX_SIZE=600`, `SPEED=100` to `main.py`. Updated Square instantiation to use these ranges. Applied speed scaling factor to velocity calculations.
- **Context and Reasons for Changes**: User requested explicit global configuration. Added configuration constants for maintainability. Initially noted that large squares (300-600px) would be oversized for 800x600 window.

---

### **Interaction 4: Window & Size Optimization**
- **Agent Version**: 2.2
- **Date**: 30-03-2026 15:15
- **User**: Ahtshm2004
- **Prompt**: "I think just increase the window size a bit and also reduce the square size a little"
- **CoPilot Mode**: Edit
- **CoPilot Model**: GitHub Copilot
- **Socratic Mode**: OFF
- **Changes Made**: Updated window dimensions from 800x600 to 1200x900. Adjusted size range from 300-600px to 30-80px. Maintained `SPEED=100` constant.
- **Context and Reasons for Changes**: Balanced visual aesthetics: larger canvas accommodates 100 squares without extreme overlap; moderate square sizes (30-80px) provide good visibility and movement dynamics.

---

### **Interaction 5: Git Commit & Push**
- **Agent Version**: 2.2
- **Date**: 30-03-2026 15:30
- **User**: Ahtshm2004
- **Prompt**: "Commit for me" → "Now, push it to github"
- **CoPilot Mode**: Edit
- **CoPilot Model**: GitHub Copilot
- **Socratic Mode**: OFF
- **Changes Made**: Initialized git repo, configured user (ahtshm2004@epita.fr), committed `main.py`, `requirements.txt`, `README.md`. Pushed to remote (origin/master).
- **Context and Reasons for Changes**: Version control and backup. User requested explicit commit and push operations.

---

### **Interaction 6: Speed Explanation**
- **Agent Version**: 2.2
- **Date**: 06-04-2026 10:00
- **User**: Ahtshm2004
- **Prompt**: "How can we explain the speed in this scenario?"
- **CoPilot Mode**: Ask
- **CoPilot Model**: GitHub Copilot
- **Socratic Mode**: OFF
- **Changes Made**: No code changes. Provided detailed explanation of speed mechanics.
- **Context and Reasons for Changes**: Educational clarification on frame-rate-independent physics, delta-time scaling, and the `SPEED` parameter's role as a global multiplier.

---

### **Interaction 7: README Update**
- **Agent Version**: 2.2
- **Date**: 06-04-2026 10:15
- **User**: Ahtshm2004
- **Prompt**: "Update the readme file according to the details or changes in the code."
- **CoPilot Mode**: Edit
- **CoPilot Model**: GitHub Copilot
- **Socratic Mode**: OFF
- **Changes Made**: Rewrote `README.md` to include accurate feature list, configuration section with all tunable constants, and detailed "How Speed Works" section explaining physics.
- **Context and Reasons for Changes**: README previously listed "10 squares" but code had 100. Updated to reflect current implementation. Added configuration documentation and speed mechanics explanation for user clarity.

---

### **Interaction 8: Journal Logger Activation**
- **Agent Version**: 2.2
- **Date**: 06-04-2026 10:20
- **User**: Ahtshm2004
- **Prompt**: "Activate the journal logger"
- **CoPilot Mode**: Edit
- **CoPilot Model**: GitHub Copilot
- **Socratic Mode**: OFF
- **Changes Made**: Created `JOURNAL.md` at repository root with comprehensive chronological log of all 8 interactions.
- **Context and Reasons for Changes**: Per copilot-instructions.md requirement: maintain JOURNAL.md tracking all interactions, edits, and rationale in chronological order (oldest first).
