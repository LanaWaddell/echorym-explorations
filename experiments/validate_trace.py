#!/usr/bin/env python3
"""Validate an Echorym trace data folder against the current schemas.

Usage: python3 validate_trace.py <schemas_dir> <trace_data_dir>
File → schema mapping: events.jsonl → event; */player_state.json → player_state;
*/world_state.json → world_state; other */*.json in state dirs → entity;
memory_trace*.json → memory_trace.
Exit code 0 iff every record validates.
"""
import json, sys, glob, os
from jsonschema import Draft202012Validator as V

def main(schemas_dir, trace_dir):
    S = {k: json.load(open(os.path.join(schemas_dir, f"{k}.schema.json")))
         for k in ["event", "entity", "player_state", "world_state", "memory_trace"]}
    checked, failures = 0, []

    def check(schema, obj, label):
        nonlocal checked
        checked += 1
        errs = list(V(S[schema]).iter_errors(obj))
        if errs:
            failures.append((label, [e.message for e in errs]))

    ev = os.path.join(trace_dir, "events.jsonl")
    if os.path.exists(ev):
        for i, line in enumerate(open(ev), 1):
            if line.strip():
                o = json.loads(line)
                check("event", o, o.get("event_id", f"events.jsonl:{i}"))
    for phase in ("initial_state", "final_state"):
        for f in sorted(glob.glob(os.path.join(trace_dir, phase, "*.json"))):
            name = os.path.basename(f)
            schema = ("player_state" if "player" in name
                      else "world_state" if "world" in name else "entity")
            check(schema, json.load(open(f)), f)
    for f in sorted(glob.glob(os.path.join(trace_dir, "memory_trace*.json"))):
        check("memory_trace", json.load(open(f)), f)

    print(f"{checked} records checked: {len(failures)} failure(s)")
    for label, msgs in failures:
        print(f"  FAIL {label}")
        for m in msgs:
            print(f"       {m}")
    return 1 if failures else 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
