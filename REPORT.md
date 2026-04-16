# Animated Squares – Project Report

## Overview
A pygame simulation of 20 colored squares bouncing around a 1000×900 canvas, with size-based speed, flee behavior, and organic wandering.

## How It Works

**Physics**
- Each square's speed is inversely proportional to its size: `v = (K / size) × (SPEED / 100)` — smaller squares move faster.
- Movement is frame-rate independent: `position += velocity × dt × 60`.
- Squares bounce off walls by negating the relevant velocity component.

**Flee Behavior**
- Each square checks for larger squares within a threat radius of `3.5 × aggressor_size`.
- A flee force (unit vector pointing away from each threat) is accumulated and blended into the current velocity: `v = 0.8 × v_current + 0.2 × v_flee`.
- Distance-squared comparison avoids expensive `sqrt()` calls until necessary.

**Wander**
- Each frame has a 10% chance to apply a random ±10° rotation to the velocity angle, preserving speed magnitude.

## Key Constants

| Constant | Value | Effect |
|---|---|---|
| `K` | 150 | Base speed scalar |
| `SPEED` | 100 | Global speed multiplier |
| `FLEE_RADIUS_MULTIPLIER` | 3.5 | Threat detection range |
| `FLEE_FORCE_WEIGHT` | 0.2 | Flee/inertia blend ratio |
| `WANDER_CHANCE` | 0.1 | Jitter probability per frame |
| `WANDER_ANGLE_RANGE` | ±10° | Max jitter angle |

## Emergent Behavior
Simple per-square rules produce a natural predator-prey ecosystem: small squares flee from large ones, large squares drift freely, and wander prevents robotic straight-line motion — all without any hard-coded roles.

## Dependency
`pygame` only.
