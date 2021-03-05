import mido
mid = mido.MidiFile('test.mid')
for i, track in enumerate(mid.tracks):
    print('Track {}:{}'.format(i, track.name))
    for msg in track:
        print(msg)
