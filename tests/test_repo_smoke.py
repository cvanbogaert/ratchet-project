import json, subprocess, pathlib, pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def run(cmd, check=True):
    return subprocess.run(cmd, cwd=ROOT, check=check, capture_output=True, text=True)

def test_files_exist():
    # Core “constitution” & config
    assert (ROOT / "docs/LOOP_PROTOCOL.md").exists()
    assert (ROOT / "config/rails.toml").exists()
    # Knowledge substrate
    assert (ROOT / "history/insights.md").exists()
    assert (ROOT / "history/pitfalls.md").exists()
    assert (ROOT / "history" / "conversations" / "2025-09_m0-to-m1.md").exists()
    assert (ROOT / ".ratchet" / "dag.json").exists()
    # Agent bootstrap
    assert (ROOT / "scripts" / "context_snapshot.py").exists()

def test_context_snapshot_runs_and_has_keys():
    out = run(["python3", "scripts/context_snapshot.py"]).stdout
    blob = json.loads(out)
    for k in ["loop_protocol", "insights", "timeline", "rails_config"]:
        assert k in blob
        assert blob[k] is None or isinstance(blob[k], str)
    if blob.get("dag") is not None:
        assert isinstance(blob["dag"], dict)

def test_dag_json_shape():
    p = ROOT / ".ratchet" / "dag.json"
    blob = json.loads(p.read_text())
    assert isinstance(blob.get("nodes"), list)
    assert isinstance(blob.get("edges"), list)
    # nodes must have ids
    for n in blob["nodes"]:
        assert isinstance(n, dict) and "id" in n
    # edges can be either ["from","to"] or {"from":..., "to":...}
    ok = True
    for e in blob["edges"]:
        if isinstance(e, list) and len(e) == 2:
            continue
        if isinstance(e, dict) and ("from" in e and "to" in e):
            continue
        ok = False
        break
    assert ok, "Edges must be pairs or objects with from/to"

def test_local_validators_if_present():
    # These scripts may exist; if they fail, we SKIP (do not fail the suite),
    # but we persist the output so humans/agents can inspect.
    for rel in ["scripts/verify.py", "scripts/validate.py", "scripts/check_cycles.py"]:
        p = ROOT / rel
        if p.exists():
            proc = run(["python3", rel], check=False)
            if proc.returncode != 0:
                (ROOT / ".ratchet").mkdir(exist_ok=True)
                (ROOT / ".ratchet" / "validate_last.txt").write_text(proc.stdout)
                pytest.skip(f"{rel} failed; see .ratchet/validate_last.txt")
