PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    long_notes = {'до': 'до-о', 'ре': 'ре-э', 'ми': 'ми-и',
                  'фа': 'фа-а', 'соль': 'со-оль', 'ля': 'ля-а', 'си': 'си-и'}

    def __init__(self, sound, is_long=False):
        if is_long:
            self.sound = self.long_notes[sound]
        else:
            self.sound = sound

    def __str__(self):
        return self.sound


class LoudNote(Note):

    def __str__(self):
        return super().__str__().upper()


class DefaultNote(Note):

    def __init__(self, sound=None, is_long=False):
        if sound is None:
            sound = 'до'
        super().__init__(sound, is_long)


class NoteWithOctave(Note):

    def __init__(self, sound, octave, is_long=False):
        self.octave = octave
        super().__init__(sound, is_long)

    def __str__(self):
        return super().__str__() + f' ({self.octave})'
