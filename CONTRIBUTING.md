# Contributing

Run the local validation command before opening a pull request:

```bash
python tools/validate_registry.py
```

The validator is stdlib-only. It currently checks JSON syntax, Markdown relative
links, and registry path shape when `registry/` exists.
