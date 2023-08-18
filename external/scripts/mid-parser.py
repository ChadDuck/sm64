import mido

mid = mido.MidiFile('song.mid')
for msg in mid.play():
    mido.port.send(msg)