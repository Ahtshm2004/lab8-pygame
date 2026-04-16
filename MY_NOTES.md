# Animated Squares — Learning Notes

## Physics

**Size-based speed** — Smaller = faster. Divide a constant by size so small squares zip around while large ones lumber. No physics engine needed, just division.
```
v = K / size × (SPEED / 100)
```

**Frame-rate independence** — Always multiply movement by `dt` (time since last frame). Without it, the sim runs fast on fast machines and slow on slow ones.
```
pos += v × dt × 60
```

---

## Behaviors

**Flee — smooth, not instant** — Don't snap to a new direction. Blend the flee force with current velocity so motion curves rather than jerks. The 80/20 split is a good starting point.
```
v_new = 0.8 × v_current + 0.2 × v_flee
```

**Threat detection trick** — Compare `dist²` to `radius²` instead of computing actual distance. You skip an expensive `sqrt()` and get the same result. Only call `sqrt()` when you actually need the distance value.

**Wander — rotate, don't perturb** — To add jitter, convert velocity to an angle, nudge the angle, then convert back. Speed stays constant and only direction shifts slightly. Direct velocity tweaks cause speed drift over time.
```
angle = atan2(vy, vx) → angle ± rand(10°) → vx/vy
```

---

## Design Lessons

**Constants at the top** — Put all tuneable values as named constants. Changing the feel of the sim becomes a one-liner, not a code hunt.

**One method, one job** — `apply_wander()`, `calculate_flee_force()`, `update()` — each does exactly one thing. Easy to test, easy to swap out.

**Emergent behavior** — There's no "predator" class. The ecosystem just happens from consistent local rules. Small rules + consistent application = surprising complexity.

**Start simple, layer up** — Bouncing squares → size-based speed → flee → wander. Each layer was working before the next was added. Never build on a broken foundation.

---

## Worth Remembering

- `dt × 60` normalizes movement to a 60fps baseline
- `dist²` avoids `sqrt()` — use it for comparisons
- Angle rotation preserves speed magnitude
- Blend ratio controls how snappy steering feels
- 10% wander chance feels natural, 100% feels broken
- Simple rules → complex emergent behavior
