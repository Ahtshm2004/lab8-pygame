# Random Moving Squares (pygame)

A pygame-based animation demo that displays 100 colorful squares moving randomly around a canvas with wall bouncing physics.

## Features

- **100 animated squares** with random colors
- **Random sizes** between 30–80 pixels
- **Realistic physics**: squares bounce off window edges with velocity reversal
- **Frame-rate independent movement**: uses delta time (dt) to ensure consistent speed regardless of FPS
- **Global speed control**: `SPEED = 100` parameter scales all movement uniformly
- **Smooth 60 FPS animation** on a 1000×900 window

## Configuration

Edit these constants in `main.py` to customize behavior:

```python
WIDTH, HEIGHT = 1000, 900      # Window dimensions
NUM_SQUARES = 100              # Number of animated squares
FPS = 60                       # Target frames per second
MIN_SIZE = 30                  # Minimum square size (pixels)
MAX_SIZE = 80                  # Maximum square size (pixels)
SPEED = 100                    # Global speed multiplier (higher = faster)
```

## Prerequisites

- Python 3.7+ (recommended)
- pip

## Installation (PowerShell)

```powershell
cd 'C:\Users\AIMS TECH\Documents\Studies\Semester - 2\AI for Software development\lab8-pygame'
python -m pip install -r requirements.txt
```

## Run the Demo

```powershell
cd 'C:\Users\AIMS TECH\Documents\Studies\Semester - 2\AI for Software development\lab8-pygame'
python main.py
```

## Controls

- **ESC key**: quit the demo
- **Close window button**: quit the demo

## How Speed Works

The animation uses **frame-rate-independent physics**:

1. Each square has random velocity components (`vx`, `vy`) scaled by `SPEED / 100.0`
2. Every frame, position is updated: `x += vx * dt * 60`
3. The `* 60` factor ensures consistent movement across different frame rates
4. Adjust the `SPEED` constant to make all squares move faster or slower globally

**Example**: With `SPEED = 100` and typical velocities, squares move ~120 pixels/second.
