# Animated Squares – Project Report

## Overview
A **Pygame** simulation of 20 colored squares on a 1000×900 canvas. The project features type-hinted Python code for improved maintainability, size-based speed, flee behavior, and an organic birth-death cycle.

## How It Works

**Physics & Rebirth**
- **Speed**: Inversely proportional to size: $v = (K / \text{size}) \times (\text{SPEED} / 100)$.
- **Lifecycle**: Squares spawn with a random lifespan (30–60s). They fade in for 2 seconds at birth and fade out for 2 seconds before being replaced.
- **Wall Interaction**: Squares bounce off boundaries by negating the velocity component.

**Flee Behavior**
- **Threat Detection**: Squares flee from any square with a larger `size` within a radius of `3.5 × aggressor_size`.
- **Force Blending**: A flee vector is accumulated and blended: $v = 0.8 \times v_{\text{current}} + 0.2 \times v_{\text{flee}}$.
- **Optimization**: Uses distance-squared comparisons and a **Surface Cache** to efficiently render squares with alpha transparency.

**Wander**
- Each frame has a 10% chance to apply a random $\pm10^\circ$ rotation to the velocity angle, preserving speed magnitude.

## Key Constants

| Constant | Value | Effect |
|---|---|---|
| `NUM_SQUARES` | 20 | Population size |
| `MIN/MAX_LIFESPAN`| 30 / 60 | Duration in seconds before rebirth |
| `FADE_DURATION` | 2.0 | Seconds for alpha fade-in/out |
| `FLEE_FORCE_WEIGHT`| 0.2 | Influence of fleeing vs. momentum |
| `WANDER_CHANCE` | 0.1 | Jitter probability per frame |

## Technical Implementation
- **Type Hinting**: The codebase utilizes the `typing` module (`List`, `Tuple`, `Dict`, `Optional`) for robust static analysis and developer clarity.
- **Rendering**: Implements `pygame.SRCALPHA` surfaces to handle dynamic transparency without sacrificing performance.
- **Emergent Behavior**: Simple per-square rules create a predator-prey ecosystem where small squares dart away from slow-moving giants.

## Dependency
`pygame` and Python 3.5+ (for type hinting support).