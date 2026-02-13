from fastapi import FastAPI
from pydantic import BaseModel
from src.engine.hemaptrust_engine import HemaTrustEngine



app = FastAPI()
engine = HemaTrustEngine()

class CBCSample(BaseModel):
    patient_id: int
    Hb: float
    RBC: float
    WBC: float
    Platelets: float
    MCV: float
    MCH: float
    RDW: float

@app.post("/verify_sample")
def verify(sample: CBCSample):

    sample_dict = {
        "Hb": sample.Hb,
        "RBC": sample.RBC,
        "WBC": sample.WBC,
        "Platelets": sample.Platelets,
        "MCV": sample.MCV,
        "MCH": sample.MCH,
        "RDW": sample.RDW
    }

    result = engine.verify_sample(sample.patient_id, sample_dict)

    return result
