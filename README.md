# HUMMBL Transparency Registry

*Structured, versioned, evidence-backed AI vendor transparency tracking. Maintained by [HUMMBL Research Institute](https://hummbl.io).*

## What this is

A governed replacement for ad-hoc "leaked system prompt" collections. The current bootstrap ships the validation harness and planned registry contract. The intended registry will:

1. **Tracks vendor system prompts** — with version history, change diffs, and provenance evidence
2. **Documents model behavior** — structured observations across safety, bias, refusal, and capability dimensions
3. **Records prompt changes** — when vendors update system prompts, we capture the delta with timestamps and evidence
4. **Provide analysis tools** — stdlib-only Python scripts for diffing, auditing, and comparing vendor transparency practices

## Why this exists

The AI industry's transparency practices are inconsistent. Vendors change system prompts without notice. "Leaked prompt" collections are unstructured, unversioned, and unverifiable. This registry makes transparency **governed**: every entry has provenance, every change has a timestamp, every claim has evidence.

## Structure

```
tools/
  validate_registry.py  # stdlib validation for JSON, Markdown links, and registry shape
```

Planned registry layout:

- `registry/vendors/` - per-vendor prompt archives with change history
- `registry/models/` - per-model behavior documentation
- `registry/diffs/` - prompt change diffs with timestamps
- `evidence/screenshots/` - visual evidence of prompt captures
- `evidence/transcripts/` - full interaction transcripts

Planned analysis tools:

- `tools/audit_prompt.py` - compare current prompt against registry
- `tools/diff_vendor.py` - diff two vendor prompt versions
- `tools/score_transparency.py` - rate vendor transparency practices

## Validation

```bash
python tools/validate_registry.py
```

The validator is intentionally standard-library only and currently checks:

- JSON parseability
- local Markdown link integrity
- future registry files live below a category directory

## Principles

- **Evidence-backed** — every entry links to source evidence
- **Version-controlled** — prompt changes tracked like code
- **Stdlib-only tooling** — zero dependencies, run anywhere
- **Governed** — follows HUMMBL append-only audit standards
- **Vendor-neutral** — rates transparency, not products

## Status

**v0.1 — BOOTSTRAP.** Validation harness established. Registry directories, initial vendor entries, evidence artifacts, and analysis tools are forthcoming.

## Related

- [hummbl-governance](https://github.com/hummbl-dev/hummbl-governance) — governance runtime (kill switch, circuit breaker, cost governor)
- [krineia](https://github.com/hummbl-dev/krineia) — append-only governance receipt chain
- [agent-governance-demo](https://github.com/hummbl-dev/agent-governance-demo) — runtime safety primitives

## License

Apache License 2.0.
