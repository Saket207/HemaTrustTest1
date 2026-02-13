import os
import shutil

print("🚀 Starting Project Restructure...")

# -----------------------------
# 1️⃣ Create Folder Structure
# -----------------------------

folders = [
    "src/engine",
    "src/api",
    "src/utils",
    "src/models",
    "dashboard"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("✅ Folders created")

# -----------------------------
# 2️⃣ Move frozen_baseline.csv
# -----------------------------

if os.path.exists("data/frozen_baseline.csv"):
    shutil.move("data/frozen_baseline.csv", "src/models/frozen_baseline.csv")
    print("✅ Baseline moved")
else:
    print("⚠ Baseline file not found (skipped)")

# -----------------------------
# 3️⃣ Move Engine File
# -----------------------------

if os.path.exists("src/hemaptrust_engine.py"):
    shutil.move("src/hemaptrust_engine.py", "src/engine/hemaptrust_engine.py")
    print("✅ Engine moved")
else:
    print("⚠ Engine file not found (skipped)")

# -----------------------------
# 4️⃣ Move API File
# -----------------------------

if os.path.exists("src/api.py"):
    shutil.move("src/api.py", "src/api/main.py")
    print("✅ API moved")
else:
    print("⚠ API file not found (skipped)")

# -----------------------------
# 5️⃣ Create __init__.py Files
# -----------------------------

init_paths = [
    "src/engine/__init__.py",
    "src/api/__init__.py",
    "src/utils/__init__.py"
]

for path in init_paths:
    with open(path, "w") as f:
        f.write("")

print("✅ __init__.py files created")

# -----------------------------
# 6️⃣ Fix Engine Baseline Path
# -----------------------------

engine_path = "src/engine/hemaptrust_engine.py"

if os.path.exists(engine_path):
    with open(engine_path, "r") as f:
        content = f.read()

    content = content.replace(
        'baseline_path="data/frozen_baseline.csv"',
        'baseline_path="src/models/frozen_baseline.csv"'
    )

    with open(engine_path, "w") as f:
        f.write(content)

    print("✅ Engine baseline path updated")

# -----------------------------
# 7️⃣ Fix API Import Path
# -----------------------------

api_path = "src/api/main.py"

if os.path.exists(api_path):
    with open(api_path, "r") as f:
        content = f.read()

    content = content.replace(
        "from hemaptrust_engine import HemaTrustEngine",
        "from src.engine.hemaptrust_engine import HemaTrustEngine"
    )

    with open(api_path, "w") as f:
        f.write(content)

    print("✅ API import path updated")

print("🎉 Project Restructure Complete!")
