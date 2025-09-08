#!/usr/bin/env python3
import json, sys, pathlib
from jsonschema import validate, Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMAS = {
    "intent": json.loads((ROOT/"schemas/intent.schema.json").read_text()),
    "cycle": json.loads((ROOT/"schemas/cycle.schema.json").read_text()),
    "dag": json.loads((ROOT/"schemas/dag.schema.json").read_text()),
    "artifact": json.loads((ROOT/"schemas/artifact.schema.json").read_text()),
}

def ok(msg): print("✅", msg)
def bad(msg): print("❌", msg)

def validate_jsons():
    # Validate any JSON files placed under intents/, plans/, cycles/*, etc. if they match known schema keys in filename
    failures = 0
    for path in ROOT.rglob("*.json"):
        name = path.name.lower()
        schema_key = None
        for key in SCHEMAS:
            if key in name:
                schema_key = key
                break
        if not schema_key:
            continue
        data = json.loads(path.read_text())
        try:
            Draft202012Validator(SCHEMAS[schema_key]).validate(data)
            ok(f"{path} conforms to {schema_key}.schema.json")
        except Exception as e:
            bad(f"{path} invalid: {e}")
            failures += 1
    return failures

if __name__ == "__main__":
    failures = validate_jsons()
    if failures:
        sys.exit(1)
    ok("JSON schema validation complete.")
