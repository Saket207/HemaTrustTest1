import pandas as pd


class HemaTrustEngine:

    def __init__(self, baseline_path="src/models/frozen_baseline.csv"):
        self.baseline = pd.read_csv(baseline_path)

        # Thresholds
        self.MCV_THRESHOLD = 12
        self.MCH_THRESHOLD = 12
        self.RDW_THRESHOLD = 15

    def verify_sample(self, patient_id, sample_data):

        patient_baseline = self.baseline[self.baseline['patient_id'] == patient_id]

        if patient_baseline.empty:
            return {
                "status": "Patient baseline not found",
                "confidence_score": 0,
                "risk_level": "UNKNOWN",
                "violations": [],
                "deltas": {}
            }

        patient_baseline = patient_baseline.iloc[0]

        deltas = {}
        violations = []

        parameters = ['Hb','RBC','WBC','Platelets','MCV','MCH','RDW']

        # Calculate delta %
        for param in parameters:
            baseline_value = patient_baseline[f"{param}_baseline"]
            current_value = sample_data[param]
            delta = ((current_value - baseline_value) / baseline_value) * 100
            deltas[param + "_delta"] = float(round(delta, 2))

        # Total delta magnitude
        total_delta = sum(abs(deltas[p + "_delta"]) for p in parameters)

        # Count stable violations
        stable_violations = 0

        if abs(deltas["MCV_delta"]) > self.MCV_THRESHOLD:
            stable_violations += 1
            violations.append("MCV deviation")

        if abs(deltas["MCH_delta"]) > self.MCH_THRESHOLD:
            stable_violations += 1
            violations.append("MCH deviation")

        if abs(deltas["RDW_delta"]) > self.RDW_THRESHOLD:
            stable_violations += 1
            violations.append("RDW deviation")

        # -----------------------------
        # Dynamic Confidence Scoring
        # -----------------------------
        score = 100

        # Penalty for stable violations
        score -= stable_violations * 25

        # Penalty for total shift severity
        score -= (total_delta // 20) * 10

        # Bound score between 0 and 100
        score = max(0, min(100, score))

        # Risk classification
        if score >= 90:
            status = "VERIFIED"
            risk_level = "GREEN"
        elif score >= 60:
            status = "REVIEW"
            risk_level = "YELLOW"
        else:
            status = "CRITICAL"
            risk_level = "RED"

        return {
            "status": status,
            "confidence_score": float(round(score, 2)),
            "risk_level": risk_level,
            "violations": violations,
            "deltas": deltas
        }
