# Animated Squares — Learning Notes

## 1. Physics & Math Logic
* **Inverse Scaling**: Making speed inversely proportional to size (`K / size`) creates an immediate visual hierarchy. It gives the "illusion" of mass without a complex physics engine.
* **Delta Time (dt)**: Always multiply movement by `dt`. This ensures that a square moving at 100 pixels per second actually moves that distance whether the computer is running at 30 FPS or 144 FPS.
* **Square of Distance**: When checking if a square is in range, compare `distance_squared` against `radius_squared`. Avoiding `math.sqrt()` inside loops is a classic optimization for real-time simulations.

## 2. Steering & Organic Motion
* **Vector Blending**: Instead of forcing a square to point away from a threat instantly, use a weighted average (`0.8 * current + 0.2 * force`). This creates smooth, curved "steering" paths rather than jagged turns.
* **Wander via Polar Coordinates**: To add jitter without changing speed, convert velocity to an angle (Polar), nudge it, and convert back to (x, y) coordinates (Cartesian). This keeps momentum perfectly preserved.

## 3. The Lifecycle Pattern
* **State-Based Alpha**: Using age and lifespan to calculate transparency (`alpha`) makes the "birth" and "death" of objects feel intentional rather than like a glitchy flicker.
* **Object Pooling (Simplified)**: Instead of letting the list grow indefinitely, the "count dead, then spawn replacements" logic keeps the memory footprint and CPU load constant.

## 4. Software Design Lessons
* **Surface Caching**: Drawing transparency is expensive in Pygame. Storing pre-rendered surfaces in a dictionary (`surface_cache`) based on size and color prevents the CPU from re-calculating pixels every single frame.
* **Type Hinting**: Using `List['Square']` or `Tuple[int, int, int]` acts as "living documentation." It tells the editor exactly what the data is, catching bugs before the code even runs.
* **Emergence**: Complexity doesn't require complex code. By giving squares just three rules (bounce, flee if smaller, wander), you get a simulation that looks like a living ecosystem.

## 5. Quick Reference
| Concept | Code Implementation | Why it matters |
| :--- | :--- | :--- |
| **Normalization** | `dt * 60` | Baselines speed to 60 FPS. |
| **Optimization** | `surface_cache` | Dramatically boosts FPS during rendering. |
| **Steering** | `0.8 * v + 0.2 * f` | Makes movement look "alive" (inertia). |
| **Readability** | `typing` module | Makes Python feel more robust and professional. |