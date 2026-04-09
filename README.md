# Random Moving Squares (pygame)

A pygame-based animation demo that displays animated squares of varying sizes moving around a canvas with wall bouncing physics. **Smaller squares move faster than larger ones**, simulating realistic inertia-based fleeing behavior.

## Features

- **20 animated squares** with random colors and sizes
- **Size-based speed scaling**: smaller squares move faster, larger squares move slower (inertia effect)
- **Random sizes** between 30–80 pixels
- **Realistic physics**: squares bounce off window edges with velocity reversal
- **Frame-rate independent movement**: uses delta time (dt) to ensure consistent speed regardless of FPS
- **Global speed control**: `SPEED = 100` parameter scales all movement uniformly
- **Smooth 60 FPS animation** on a 1000×900 window

## Configuration

Edit these constants in `main.py` to customize behavior:

```python
WIDTH, HEIGHT = 1000, 900      # Window dimensions
NUM_SQUARES = 20               # Number of animated squares
FPS = 60                       # Target frames per second
MIN_SIZE = 30                  # Minimum square size (pixels)
MAX_SIZE = 80                  # Maximum square size (pixels)
K = 150                        # Size-speed scaling constant (smaller K = slower overall)
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

The animation uses **frame-rate-independent physics with size-based velocity scaling**:

1. Each square has velocity components (`vx`, `vy`) based on its size: `velocity = (K / size) * (SPEED / 100.0)`
2. **Smaller squares** (size=30): `vx = ±(150/30) = ±5.0` — move faster
3. **Larger squares** (size=80): `vx = ±(150/80) = ±1.875` — move slower
4. Every frame, position is updated: `x += vx * dt * 60`
5. The `* 60` factor ensures consistent movement across different frame rates
6. Adjust the `K` constant to change the speed-to-size ratio
7. Adjust the `SPEED` constant to scale all speeds uniformly

**Example**: With `K = 150` and `SPEED = 100`, a small square (size=30) moves about 2.67× faster than a large square (size=80).

## Physics Concept: Inertia

This demo implements a simplified inertia model where:
- **Smaller objects** have less mass and move more quickly
- **Larger objects** have more mass and move more slowly
- This creates a "fleeing" effect where small squares appear more agile
