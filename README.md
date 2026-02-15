# midi-song-analysis

A CLI tool for analyzing MIDI files to support band rehearsals and vocal performance preparation.

---

## Overview

**midi-song-analysis** is a command-line tool designed to analyze MIDI files as *songs*, focusing on practical information useful for musicians.

The primary goal is to support:
- Band rehearsal preparation
- Vocal range checking and transposition planning
- Instrumental playability analysis

This tool is **not** intended for MIDI device benchmarking, real-time performance evaluation, or DAW replacement.  
Instead, it aims to extract musically meaningful insights from existing MIDI files in a simple, scriptable way.

---

## Key Features (Planned / In Progress)

- Analyze note ranges per MIDI channel or track
- Detect lowest and highest notes used in a song
- Evaluate playability against predefined vocal or instrumental ranges
- Support transposition and re-analysis
- Export analysis results as structured JSON for reuse and extension

---

## Design Philosophy

- **Song-oriented analysis**  
  MIDI files are treated as musical pieces, not just technical data streams.

- **Incremental extensibility**  
  New analyses can be added without breaking existing results by extending the JSON output.

- **CLI-first**  
  Designed to work well in terminal-based workflows and scripts.

- **Legally conscious**  
  The tool analyzes MIDI files only. Users are responsible for complying with copyright laws when using MIDI data.

---

## Output Format

Analysis results are stored as JSON files.

This allows:
- Easy inspection by humans
- Reuse by other tools or scripts
- Gradual extension as new analysis features are added

Example (simplified):

```json
{
  "meta": {
    "source_file": "song.mid",
    "ticks_per_beat": 480
  },
  "analysis": {
    "channels": {
      "1": {
        "lowest_note": { "number": 53, "name": "F3" },
        "highest_note": { "number": 72, "name": "C5" }
      }
    }
  }
}
```
Both MIDI note numbers and note names are intentionally included.

---

### Assets

This repository includes only non-copyrighted sample files.

Purchased or copyrighted music data (e.g. MIDI, MusicXML)
must be placed under `assets/private/`, which is excluded
from version control via `.gitignore`.

---

## Technology

- Python
- mido (for MIDI parsing)

---

## Project Status

This project is in an early development stage.

The initial focus is on:
- Reliable MIDI parsing
- Accurate range analysis
- A clean and extensible JSON schema

APIs and output formats may evolve as the project grows.

---

## License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.
