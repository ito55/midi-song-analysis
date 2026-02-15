import sys
import os
from collections import defaultdict

import mido


NOTE_NAME_CONVENTION = "MIDI note 60 = C4"


NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F",
              "F#", "G", "G#", "A", "A#", "B"]


def note_number_to_name(note_number: int) -> str:
    """
    Convert MIDI note number to note name.
    Convention: MIDI note 60 = C4
    """
    octave = (note_number // 12) - 1
    name = NOTE_NAMES[note_number % 12]
    return f"{name}{octave}"


def analyze_midi_range(midi_path: str) -> dict:
    """
    Analyze lowest and highest note per MIDI channel.
    Returns:
        {
            channel: {
                "lowest_note": int,
                "highest_note": int
            },
            ...
        }
    """
    mid = mido.MidiFile(midi_path)

    channel_notes = defaultdict(list)

    for track in mid.tracks:
        for msg in track:
            if msg.type == "note_on" and msg.velocity > 0:
                channel_notes[msg.channel].append(msg.note)

    results = {}

    for channel, notes in channel_notes.items():
        if not notes:
            continue

        results[channel] = {
            "lowest_note": min(notes),
            "highest_note": max(notes),
        }

    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: python range_analysis.py <midi_file>")
        sys.exit(1)

    midi_path = sys.argv[1]

    if not os.path.isfile(midi_path):
        print(f"Error: file not found: {midi_path}")
        sys.exit(1)

    midi_name = os.path.basename(midi_path)

    try:
        results = analyze_midi_range(midi_path)
    except Exception as e:
        print(f"Analysis failed: {e}")
        sys.exit(1)

    print(f"Analysis succeeded: {midi_name}")
    print(f"Note name convention: {NOTE_NAME_CONVENTION}")
    print()
    print("Results:")

    if not results:
        print("No note data found.")
        return

    for channel in sorted(results.keys()):
        low = results[channel]["lowest_note"]
        high = results[channel]["highest_note"]

        low_name = note_number_to_name(low)
        high_name = note_number_to_name(high)

        print(f"Channel {channel + 1}:")
        print(f"  Highest: {high_name} ({high})")
        print(f"  Lowest : {low_name} ({low})")


if __name__ == "__main__":
    main()
