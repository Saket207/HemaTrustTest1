🩸 HemaTrust
Decentralized AI Framework for Detecting Wrong Blood in Tube (WBIT)
📌 Problem Statement

In clinical laboratories, Wrong Blood in Tube (WBIT) is a serious pre-analytical error where a blood sample from one patient is mistakenly labeled as another.

This can lead to:

Wrong blood transfusion

Misdiagnosis

Delayed treatment

Legal liability

HemaTrust detects such errors by creating a Biological Fingerprint for every patient and verifying new reports against it.

🧠 How HemaTrust Works

Load patient’s historical baseline (biological fingerprint)

Compare new CBC report with baseline

Calculate percentage change (delta)

Detect biologically impossible shifts

Generate:

Confidence Score (0–100)

Risk Level (GREEN / YELLOW / RED)

Violations explanation

🏗 Project Structure
HemaTrust/
│
├── src/
│   ├── engine/          # Core biological verification logic
│   ├── api/             # FastAPI backend server
│   ├── models/          # Frozen patient baseline data
│   └── utils/
│
├── dashboard/           # Streamlit frontend
│
├── requirements.txt
└── README.md

🚀 HOW TO RUN THIS PROJECT (VERY BASIC STEPS)

Follow these steps exactly.

✅ STEP 1 — Install Python

Install Python 3.10 or above.

Check installation:

python --version


If it prints version → OK.

✅ STEP 2 — Clone This Repository
git clone https://github.com/Saket207/HemaTrust.git
cd HemaTrust

✅ STEP 3 — Install Required Libraries

Run this:

pip install -r requirements.txt


If that does not work, run:

python -m pip install -r requirements.txt


Wait until installation finishes.

✅ STEP 4 — Run Backend API

Run this command:

python -m uvicorn src.api.main:app --reload


You should see:

Uvicorn running on http://127.0.0.1:8000


Now open browser:

http://127.0.0.1:8000/docs


This opens interactive API testing page.

Backend is now running.

✅ STEP 5 — Run Frontend Dashboard

Open a NEW terminal window.

Run:

streamlit run dashboard/app.py


Browser will open automatically at:

http://localhost:8501


Now you can:

Enter patient ID

Enter CBC values

Click Verify

See confidence score

See risk level

See radar visualization

Full system is now running.

🧪 Example API Test Input

You can test inside /docs with:

{
  "patient_id": 1,
  "Hb": 11.5,
  "RBC": 4.2,
  "WBC": 7000,
  "Platelets": 250000,
  "MCV": 85,
  "MCH": 28,
  "RDW": 13
}

📊 Output Example
{
  "status": "CRITICAL",
  "confidence_score": 40,
  "risk_level": "RED",
  "violations": [
    "MCV deviation",
    "MCH deviation"
  ],
  "deltas": {
    "Hb_delta": 18.27,
    ...
  }
}

🎯 Risk Classification
Score	Risk Level	Meaning
90–100	GREEN	Verified
60–89	YELLOW	Review Required
<60	RED	High Probability of WBIT
🏥 Clinical Significance

HemaTrust prevents:

Sample mix-ups

Incorrect transfusions

Diagnostic errors

Legal liability

👨‍💻 Tech Stack

Python

FastAPI

Uvicorn

Pandas

Streamlit

Plotly

🛑 Important Notes

Backend must be running before frontend.

Always run API first.

No database required.

Fully local execution.

🔮 Future Scope

Blockchain-based immutable logging

Smart contract integration

Real hospital LIS integration

Hybrid ML + Rule model

👥 Hackathon Usage

To run full system:

pip install -r requirements.txt
python -m uvicorn src.api.main:app --reload
streamlit run dashboard/app.py


That’s it.
