# HUMMBL Transparency Registry

*Structured, versioned, evidence-backed AI vendor transparency tracking. Maintained by [HUMMBL Research Institute](https://hummbl.io).*

## What this is

A governed replacement for ad-hoc "leaked system prompt" collections. This registry:

1. **Tracks vendor system prompts** — with version history, change diffs, and provenance evidence
2. **Documents model behavior** — structured observations across safety, bias, refusal, and capability dimensions
3. **Records prompt changes** — when vendors update system prompts, we capture the delta with timestamps and evidence
4. **Provides analysis tools** — stdlib-only Python scripts for diffing, auditing, and comparing vendor transparency practices

## Why this exists

The AI industry's transparency practices are inconsistent. Vendors change system prompts without notice. "Leaked prompt" collections are unstructured, unversioned, and unverifiable. This registry makes transparency **governed**: every entry has provenance, every change has a timestamp, every claim has evidence.

## Structure

```
registry/
  vendors/          # Per-vendor prompt archives with change history
    anthropic/
    openai/
    google/
    ...
  models/           # Per-model behavior documentation
  diffs/            # Prompt change diffs with timestamps
tools/
  audit_prompt.py   # Compare current prompt against registry
  score_transparency.py  # Rate vendor transparency practices
evidence/
  ...               # Source notes and capture references
```

## Principles

- **Evidence-backed** — every entry links to source evidence
- **Version-controlled** — prompt changes tracked like code
- **Stdlib-only tooling** — zero dependencies, run anywhere
- **Governed** — follows HUMMBL append-only audit standards
- **Vendor-neutral** — rates transparency, not products

## Status

**v0.1 — BOOTSTRAP COMPLETE.** The registry includes an initial
Anthropic Claude Opus 4.7 transparency entry, model behavior documentation,
schema-aware validation, prompt auditing, transparency scoring, and CI.

Run local checks:

```bash
python tools/validate_registry.py
python tools/audit_prompt.py registry/vendors/anthropic/claude-opus-4.7-2026-04-16.json
python tools/score_transparency.py
```

## Related

- [hummbl-governance](https://github.com/hummbl-dev/hummbl-governance) — governance runtime (kill switch, circuit breaker, cost governor)
- [krineia](https://github.com/hummbl-dev/krineia) — append-only governance receipt chain
- [agent-governance-demo](https://github.com/hummbl-dev/agent-governance-demo) — runtime safety primitives

## License

Apache License 2.0.
