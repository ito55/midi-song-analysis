A CLI tool for analyzing MIDI files to support band rehearsals and vocal performance preparation.

---

## Overview

**midi-song-note-range-analyzer** is a command-line tool designed to analyze MIDI files as songs, focusing on practical information useful for musicians.

The primary goal is to support:

- Band rehearsal preparation  
- Vocal range checking and transposition planning  
- Instrumental playability analysis  

This tool is not intended for MIDI device benchmarking, real-time performance evaluation, or DAW replacement.  
Instead, it aims to extract musically meaningful insights from existing MIDI files in a simple, scriptable way.

---

## Usage

Run the tool from the command line and provide a MIDI file path as an argument.

```bash
python src/range_analysis.py path/to/song.mid
```

Example:
```bash
python src/range_analysis.py assets/sample.mid
```

---

## Example Output

```text
Analysis succeeded: sample.mid
Note name convention: MIDI note 60 = C4

Results:
Channel 1:
  Highest: A#5 (82)
  Lowest : F4 (65)
Channel 2:
  Highest: C6 (84)
  Lowest : F4 (65)

```

- MIDI note numbers are always included.  
- Note names follow the scientific pitch notation convention:  
  MIDI note 60 = C4  

Some DAWs (e.g., Cubase) may display MIDI note 60 as C3.  
This is a naming convention difference only.  
MIDI note numbers should be considered authoritative.

---

## Key Features (Planned / In Progress)

- Analyze note ranges per MIDI channel  
- Detect lowest and highest notes used in a song  
- Evaluate playability against predefined vocal or instrumental ranges  
- Support transposition and re-analysis  
- Export analysis results as structured JSON for reuse and extension  

---

## Design Philosophy

- **Song-oriented analysis**  
  MIDI files are treated as musical pieces, not just technical data streams.

- **Incremental extensibility**  
  New analyses can be added without breaking existing results.

- **CLI-first**  
  Designed to work well in terminal-based workflows and scripts.

- **Legally conscious**  
  The tool analyzes MIDI files only. Users are responsible for complying with copyright laws when using MIDI data.

---

### Assets

This repository includes only non-copyrighted sample files.

Purchased or copyrighted music data (e.g. MIDI, MusicXML) must be placed under `assets/private/`, which is excluded from version control via `.gitignore`.

---

## Technology

- Python  
- mido (for MIDI parsing)

---

## Project Status

This project is in an early development stage.

The current focus is:

- Reliable MIDI parsing  
- Accurate range analysis  
- Clear and consistent CLI output  

JSON export and advanced analysis features are planned for future versions.

---

## License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.
