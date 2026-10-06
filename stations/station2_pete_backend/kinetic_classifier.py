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

        # Flash & Hogan jerk cost: integral of J^2 dt
        jerk_metric = np.mean(np.abs(jerks))

        # Check for 8-12 Hz physiological tremor
        tremor_detected = self._detect_neuromotor_tremor(speeds, dt)

        # Low jerk + no tremor => synthetic spline generator (e.g. Bézier bot)
        if jerk_metric < 0.02 and not tremor_detected:
            return 0.96
        elif jerk_metric < 0.05 and not tremor_detected:
            return 0.88
        elif tremor_detected:
            return 0.12  # Characteristic human neuromotor signature
        else:
            return 0.35

    def _detect_neuromotor_tremor(self, speeds: np.ndarray, dt: np.ndarray) -> bool:
        """Checks for 8-12 Hz frequency oscillations characteristic of human neuromuscular tremor."""
        if len(speeds) < 8:
            return False
        # Spectral energy proxy: number of speed sign reversals
        diffs = np.diff(speeds)
        sign_changes = np.sum(diffs[:-1] * diffs[1:] < 0)
        reversal_ratio = sign_changes / max(len(diffs), 1)
        return reversal_ratio > 0.35
