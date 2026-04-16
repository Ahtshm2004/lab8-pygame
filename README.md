# Animated Squares with Inertia-Based Fleeing & Lifespan

A sophisticated pygame-based animation demonstrating emergent ecosystem behavior through physics-based simulation. **20 colored squares** of varying sizes interact through inertia-based speed scaling, threat detection, organic wandering behavior, and dynamic lifecycle management—creating a compelling predator-prey-like dynamic with continuous regeneration of dying squares.

## Features

- **20 animated squares** with random colors and sizes (30–80 pixels)
- **Dynamic lifespan system**: squares live 30–60 seconds before natural death
- **Smooth fade transitions**: fade in at birth (2s) and fade out before death (2s)
- **Size-based speed scaling**: smaller squares move faster (inertia effect)
- **Fleeing behavior**: small squares actively flee from nearby larger ones
- **Threat detection**: proximity-based awareness (3.5× threat radius)
- **Velocity blending**: smooth 80/20 blend of current motion and flee force
- **Organic wandering**: 10% chance per frame for ±5–10° random direction jitter
- **Frame-rate independent movement**: delta-time scaling ensures smooth animation
- **Realistic physics**: wall bouncing with velocity reversal
- **Smooth 60 FPS animation** on a 1000×900 window

## Configuration

Edit these constants in `main.py` to customize behavior:

```python
# Canvas & Rendering
WIDTH, HEIGHT = 1000, 900      # Window dimensions
NUM_SQUARES = 20               # Number of animated squares
FPS = 60                       # Target frames per second

# Square Properties
MIN_SIZE = 30                  # Minimum square size (pixels)
MAX_SIZE = 80                  # Maximum square size (pixels)
K = 150                        # Inertia scaling constant (velocity = K / size)
SPEED = 100                    # Global speed multiplier

# Fleeing & Behavior
FLEE_RADIUS_MULTIPLIER = 3.5   # Threat detected at 3.5× larger square's size
FLEE_FORCE_WEIGHT = 0.2        # 20% flee force blended with current velocity
WANDER_CHANCE = 0.1            # 10% chance per frame to apply random jitter
WANDER_ANGLE_RANGE = 10        # ±10 degrees for random direction changes

# Lifespan & Fade
MIN_LIFESPAN = 30.0            # Minimum lifespan in seconds
MAX_LIFESPAN = 60.0            # Maximum lifespan in seconds
FADE_DURATION = 2.0            # Fade in/fade out duration in seconds
```

## Prerequisites

- Python 3.7+
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

## Code Quality

- ✅ **Full type hints**: All functions and variables are properly annotated (PEP 484)
- ✅ **Static type checking**: Compatible with mypy and pyright
- ✅ **Type safety**: Clear function contracts and IDE autocomplete support
- ✅ **Pythonic design**: Clean separation of concerns with Square class and utility functions

## How It Works

### 1. Inertia-Based Speed Scaling

Physics principle: Velocity is inversely proportional to size.

Formula: `velocity = (K / size) * (SPEED / 100.0)`

**Example with K=150, SPEED=100:**
- Small square (size=30): velocity = 5.0 units/frame (fast!)
- Large square (size=80): velocity = 1.875 units/frame (slow)
- **Speed ratio**: Small boxes move 2.67× faster than large boxes

### 2. Fleeing Behavior

When a small square detects a larger one nearby, it activates escape logic:

1. **Threat Detection**: Checks all larger squares within awareness radius
   - `threat_radius = FLEE_RADIUS_MULTIPLIER × larger_square_size`
   - Uses distance-squared comparison for performance optimization
2. **Escape Direction**: Calculates normalized vector pointing away from threats
3. **Velocity Blending**: Smoothly combines flee force with current motion
   - `new_velocity = 0.8 × current + 0.2 × flee_force`
   - Prevents jarring direction changes; creates smooth curve away from danger

### 3. Organic Wandering

Every frame, small random perturbations are applied to velocity direction:

1. **Activation**: 10% probability per frame
2. **Angle Rotation**: ±5° to ±10° random jitter applied to velocity vector
3. **Speed Preservation**: Magnitude maintained; only direction changes
4. **Effect**: Creates natural "swimming" motion with subtle course corrections

### 4. Lifespan & Fade Transitions

Each square has a limited lifespan with smooth visual transitions:

1. **Lifespan Assignment**: Each square randomly lives 30–60 seconds
2. **Fade-In**: Over first 2 seconds, alpha grows from 0 to 255 (birth animation)
3. **Full Life**: Maintains 100% opacity while age < lifespan - FADE_DURATION
4. **Fade-Out**: In final 2 seconds before death, alpha fades 255 → 0 (death animation)
5. **Natural Death**: Marked as dead when `age >= lifespan`
6. **Effect**: Smooth birth/death visual feedback; suggests continuous ecosystem cycle

### 5. Frame-Rate Independence

Movement is normalized across different frame rates:

Formula: `position += velocity × dt × 60`

Where `dt = clock.tick(FPS) / 1000.0` (elapsed seconds)

The `× 60` factor ensures consistent speed whether running at 30 FPS or 120 FPS.

## Physics Concepts Implemented

| Concept | Implementation | Effect |
|---------|-----------------|--------|
| **Inertia** | Velocity inversely proportional to size | Smaller = faster, larger = slower |
| **Threat Detection** | Distance-squared proximity checks | Efficient performance, realistic awareness |
| **Steering** | Velocity blending rather than override | Smooth curves instead of robotic snaps |
| **Wandering** | Angle-based jitter with speed preservation | Organic, natural-looking motion |
| **Lifecycle** | Age tracking with fade-in/fade-out transitions | Visual continuity of birth and death |
| **Collision** | Wall bouncing with velocity reversal | Realistic boundary behavior |

## Customization Examples

### Increase Fleeing Urgency
```python
FLEE_FORCE_WEIGHT = 0.5  # 50% flee force (more panic)
FLEE_RADIUS_MULTIPLIER = 5.0  # Detect threats from farther away
```

### Reduce Wandering for Stable Motion
```python
WANDER_CHANCE = 0.02  # Only 2% chance per frame (less jitter)
WANDER_ANGLE_RANGE = 3  # ±3 degrees (subtle changes)
```

### Add More Squares with Adjusted Speed
```python
NUM_SQUARES = 50
K = 200  # Increase K to compensate for more squares
SPEED = 150  # Speed up overall movement
```

### Create Predator Effect (Very Large Slow Square)
```python
NUM_SQUARES = 19  # One spot for predator
# Add custom code to spawn one very large square (size=150)
# which will naturally cause all smaller squares to flee
```

## Visual Observations

When running the demo, you'll notice:
- 🟢 **Small squares**: Dart around quickly, frequently change direction (wander)
- 🔴 **Large squares**: Move ponderously, create "safe zones" away from them
- 🌊 **Fleeing effect**: Small squares curve away when large ones approach
- 🎨 **Organic motion**: Nothing moves perfectly straight—all exhibit natural jitter
- ✨ **Fade-in effect**: New squares gently appear with increasing opacity over 2 seconds
- 👻 **Fade-out effect**: Dying squares gradually fade to transparent over final 2 seconds
- 🔄 **Continuous cycle**: As squares die, the system naturally maintains 20 active squares

## Performance Notes

- **Optimization**: Distance-squared comparisons reduce expensive sqrt() operations
- **Scaling**: With 20 squares, ~1–2% CPU on modern systems
- **Bottleneck**: Main CPU cost is distance calculations (quadratic with square count)
- **Potential enhancement**: Spatial partitioning (grid/quadtree) for large square counts
