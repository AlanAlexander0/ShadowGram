"""
simulation/trajectory.py - Standalone Neuromotor Trajectory Generator
Based on Flash & Hogan (1985) Minimum-Jerk Theory with dynamic overshoot and physiological micro-tremor.
Zero external dependencies (pure Python).
"""

import math
import random
from typing import List, Tuple


def generate_human_trajectory(
    p0: Any,
    p3: Any = None,
    *args,
    duration: float = 0.65,
    fps: int = 60,
    overshoot_threshold: float = 220.0,
    overshoot_ratio: float = 0.08,
    noise_sigma: float = 0.45,
    **kwargs
) -> List[Tuple[float, float, float]]:
    """
    Generates a realistic biological human cursor trajectory between p0 and p3.
    Accepts either p0=(x1,y1), p3=(x2,y2) or x1, y1, x2, y2.
    Returns: List of (x, y, t) tuples where t is relative elapsed time in seconds.
    """
    if isinstance(p0, (int, float)) and isinstance(p3, (int, float)) and len(args) >= 2:
        p0, p3 = (float(p0), float(p3)), (float(args[0]), float(args[1]))
    elif p3 is None:
        p3 = (800.0, 600.0)

    if "points" in kwargs and kwargs["points"]:
        fps = int(kwargs["points"] / max(duration, 0.1))

    dx = p3[0] - p0[0]
    dy = p3[1] - p0[1]
    dist = math.hypot(dx, dy)
    overshoot = dist > overshoot_threshold

    if overshoot:
        angle = math.atan2(dy, dx)
        ov_dist = min(dist * overshoot_ratio, 28.0) * random.uniform(0.85, 1.15)
        target = (p3[0] + math.cos(angle) * ov_dist, p3[1] + math.sin(angle) * ov_dist)
    else:
        target = p3

    # Generate control points for general arm curve curvature
    u1, v1 = random.uniform(0.2, 0.38), random.uniform(-0.2, 0.2) * dist
    u2, v2 = random.uniform(0.62, 0.82), random.uniform(-0.15, 0.15) * dist
    p1 = (p0[0] + dx * u1 - (dy / dist) * v1, p0[1] + dy * u1 + (dx / dist) * v1) if dist else p0
    p2 = (p0[0] + dx * u2 - (dy / dist) * v2, p0[1] + dy * u2 + (dx / dist) * v2) if dist else p0

    def bz(t: float, a: float, b: float, c: float, d: float) -> float:
        omt = 1.0 - t
        return (omt**3) * a + 3 * (omt**2) * t * b + 3 * omt * (t**2) * c + (t**3) * d

    steps = max(int(duration * fps), 12)
    path: List[Tuple[float, float, float]] = []

    for i in range(steps + 1):
        tau = i / steps
        # Flash & Hogan minimum-jerk polynomial: s(tau) = 10*tau^3 - 15*tau^4 + 6*tau^5
        s = 10.0 * (tau**3) - 15.0 * (tau**4) + 6.0 * (tau**5)
        bx = bz(s, p0[0], p1[0], p2[0], target[0])
        by = bz(s, p0[1], p1[1], p2[1], target[1])
        # Biological physiological micro-tremor (8-12 Hz tremor emulation)
        tremor = math.sin(math.pi * tau * 10) * random.gauss(0, noise_sigma)
        path.append((round(bx + tremor, 2), round(by + tremor, 2), round(tau * duration, 4)))

    # Secondary corrective sub-movement if overshoot occurred
    if overshoot:
        corr_steps = max(int(steps * 0.2), 6)
        corr_time = duration * 0.22
        lx, ly, lt = path[-1]
        for j in range(1, corr_steps + 1):
            c_tau = j / corr_steps
            c_s = 10.0 * (c_tau**3) - 15.0 * (c_tau**4) + 6.0 * (c_tau**5)
            cx = lx + (p3[0] - lx) * c_s
            cy = ly + (p3[1] - ly) * c_s
            c_tremor = (1.0 - c_tau) * random.gauss(0, noise_sigma * 0.4)
            path.append((round(cx + c_tremor, 2), round(cy + c_tremor, 2), round(lt + (j / corr_steps) * corr_time, 4)))

    return path

# Alias for backwards compatibility
generate_human_bezier_trajectory = generate_human_trajectory


if __name__ == "__main__":
    test_path = generate_human_trajectory((100, 100), (800, 600), duration=0.8)
    print(f"Generated {len(test_path)} waypoints. Sample first 3 and last 3:")
    for pt in test_path[:3]:
        print(" ", pt)
    print("  ...")
    for pt in test_path[-3:]:
        print(" ", pt)
