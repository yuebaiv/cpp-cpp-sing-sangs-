# -*- coding: gbk -*-
import mido
import mido

def get_midi_notes(filename):
    try:
        mid = mido.MidiFile(filename)
        notes = []
        for track in mid.tracks:
            for msg in track:
                if msg.type == 'note_on':
                    note = msg.note
                    velocity = msg.velocity
                    time = msg.time
                    notes.append((note, velocity, time))
        return notes
    except FileNotFoundError:
        print("File not found.")
    except mido.MidiParseError:
        print("Invalid MIDI file.")

# 使用示例
midi_file = 'D:/360安全浏览器下载/圈住你.mid'
midi_notes = get_midi_notes(midi_file)
if midi_notes:
    for note in midi_notes:
        note = ','.join([f"{x[0]}, {x[1]}, {x[2]}" for x in midi_notes])

print(note )

      



