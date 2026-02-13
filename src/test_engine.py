from hemaptrust_engine import HemaTrustEngine

engine = HemaTrustEngine()

sample = {
    "Hb": 11.5,
    "RBC": 4.2,
    "WBC": 7000,
    "Platelets": 250000,
    "MCV": 85,
    "MCH": 28,
    "RDW": 13
}

result = engine.verify_sample(patient_id=1, sample_data=sample)

print(result)
