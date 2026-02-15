import argparse
from mido import MidiFile

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def note_number_to_name(note_number: int) -> str:
    octave = (note_number // 12) - 1
    name = NOTE_NAMES[note_number % 12]
    return f"{name}{octave}"


def analyze_note_range(midi_path: str, channels: list[int]) -> dict:
    mid = MidiFile(midi_path)

    notes_by_channel = {ch: [] for ch in channels}

    for track in mid.tracks:
        for msg in track:
            if msg.type == "note_on" and msg.velocity > 0:
                if msg.channel in notes_by_channel:
                    notes_by_channel[msg.channel].append(msg.note)

    result = {}

    for ch, notes in notes_by_channel.items():
        if not notes:
            result[ch] = None
            continue

        low = min(notes)
        high = max(notes)

        result[ch] = {
            "lowest": {
                "number": low,
                "name": note_number_to_name(low),
            },
            "highest": {
                "number": high,
                "name": note_number_to_name(high),
            },
        }

    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze note ranges per MIDI channel."
    )
    parser.add_argument(
        "midi_file",
        help="Path to a MIDI file",
    )

    args = parser.parse_args()

    # Default: analyze MIDI channels 1 and 2 (0-based: 0, 1)
    channels = [0, 1]

    ranges = analyze_note_range(args.midi_file, channels)

    for ch, data in ranges.items():
        print(f"Channel {ch + 1}:")
        if data is None:
            print("  No notes found")
        else:
            print(
                f"  Lowest : {data['lowest']['name']} "
                f"({data['lowest']['number']})"
            )
            print(
                f"  Highest: {data['highest']['name']} "
                f"({data['highest']['number']})"
            )


if __name__ == "__main__":
    main()
