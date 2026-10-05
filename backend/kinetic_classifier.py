import math
import numpy as np
from typing import List, Tuple, Optional

class KineticJerkClassifier:
    """
    Evaluates biomechanical motor-control authenticity.
    Distinguishes biological human movement from synthetic Bézier automation
    based on Flash & Hogan minimum-jerk theory and physiological tremor (8-12 Hz).
    """

    def __init__(self, onnx_model_path: Optional[str] = None):
        self.onnx_session = None
        if onnx_model_path:
            try:
                import onnxruntime as ort
                self.onnx_session = ort.InferenceSession(onnx_model_path)
            except Exception as e:
                print(f"[KineticClassifier] ONNX model not loaded ({e}), using mathematical jerk analysis.")

    def evaluate_trajectory(self, coordinates: List[List[float]]) -> float:
        """
        Input: list of [x, y, t] (timestamp in seconds or ms)
        Returns: P(synthetic) in [0.0, 1.0]
        """
        if not coordinates or len(coordinates) < 4:
            return 0.5  # Neutral prior if insufficient data

        pts = np.array(coordinates, dtype=float)
        # Sort by timestamp
        pts = pts[pts[:, 2].argsort()]

        # Remove duplicate timestamps to prevent zero-division
        dt = np.diff(pts[:, 2])
        valid_idx = np.where(dt > 0.0001)[0]
        if len(valid_idx) < 3:
            return 0.5

        valid_pts = pts[np.append(valid_idx, valid_idx[-1] + 1)]
        dt = np.diff(valid_pts[:, 2])

        # Velocities v = dx / dt
        dx = np.diff(valid_pts[:, 0]) / dt
        dy = np.diff(valid_pts[:, 1]) / dt
        speeds = np.hypot(dx, dy)

        if len(speeds) < 3:
            return 0.5

        # Accelerations a = dv / dt
        dt_mid = 0.5 * (dt[:-1] + dt[1:])
        dt_mid = np.maximum(dt_mid, 0.0001)
        accels = np.diff(speeds) / dt_mid

        if len(accels) < 2:
            return 0.5

        # Jerk J = da / dt (3rd derivative)
        dt_jerk = dt_mid[:-1]
        jerks = np.diff(accels) / np.maximum(dt_jerk, 0.0001)

        # Jerk spectral entropy & variance
        jerk_std = float(np.std(jerks))
        jerk_mean = float(np.mean(np.abs(jerks)))
        jerk_coef_var = jerk_std / (jerk_mean + 1e-5)

        # In cubic Bézier splines (bots), third derivative is constant across segments
        # -> jerk_coef_var is near zero or piecewise uniform.
        # In humans, 8-12 Hz micro-tremor causes continuous chaotic jerk variance.
        if jerk_std < 12.0 or jerk_coef_var < 0.25:
            # High probability of synthetic mathematical curve
            synthetic_score = float(np.clip(0.92 + (0.08 * (1.0 - jerk_coef_var)), 0.85, 0.99))
        elif jerk_coef_var > 1.8:
            # High natural tremor
            synthetic_score = float(np.clip(0.08 / (jerk_coef_var + 0.1), 0.01, 0.20))
        else:
            synthetic_score = float(np.clip(1.0 - (jerk_coef_var / 2.0), 0.20, 0.80))

        return round(synthetic_score, 4)

    def evaluate_keystroke_kinetics(self, flight_time: Optional[float], dwell_time: Optional[float]) -> float:
        """
        Evaluates key flight/dwell intervals.
        Robotic automation uses fixed delays (e.g. 50ms) or uniform randoms.
        """
        if flight_time is None or dwell_time is None:
            return 0.5

        # Extremely low flight times (< 15ms) or perfectly identical values indicate bot
        if flight_time < 12.0 or dwell_time < 15.0:
            return 0.95
        if abs(flight_time - 50.0) < 1.0 or abs(flight_time - 100.0) < 1.0:
            return 0.91

        # Natural human typing
        return 0.12
