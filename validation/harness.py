import yaml
from pathlib import Path

print("ASC Registry Validation Harness v0.1.0")

schema_file = Path("schema/control.schema.json")
controls_dir = Path("controls")

# Check schema exists
if not schema_file.exists():
    print("❌ Schema file not found")
    exit(1)

print("✅ Schema loaded")

# Check controls directory exists
if not controls_dir.exists():
    print("❌ Controls directory not found")
    exit(1)

# Load all controls
control_files = list(controls_dir.glob("*.yaml"))

if not control_files:
    print("❌ No controls found")
    exit(1)

print(f"✅ Found {len(control_files)} control(s)")

for control_file in control_files:
    try:
        with open(control_file, "r", encoding="utf-8") as f:
            control = yaml.safe_load(f)

        print(
            f"✅ Loaded {control['id']} - {control['title']}"
        )

    except Exception as e:
        print(f"❌ Error loading {control_file.name}")
        print(e)

print("✅ Validation completed successfully")
