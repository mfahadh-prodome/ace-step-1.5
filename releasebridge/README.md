# ReleaseBridge v1

ReleaseBridge is the orchestration layer between ACE-Step music generation, storage, quality control, metadata, and distribution connectors.

## Goals
- Keep upstream ACE-Step code isolated and easy to sync.
- Generate standardized release packages.
- Store masters, artwork, metadata, rights, and QC results.
- Support future SoundCloud and distributor connectors.

## Package shape

```
RB-YYYY-NNNN/
├── master.wav
├── cover.png
├── release.json
├── rights.json
└── qc.json
```

## Status flow

`draft -> qc -> approved -> ready -> published -> failed`

## Initial modules
- `generation/` ACE-Step adapter
- `metadata/` release schema and validation
- `qc/` audio/package checks
- `storage/` Drive/object-storage adapters
- `connectors/` SoundCloud and distributor connectors
