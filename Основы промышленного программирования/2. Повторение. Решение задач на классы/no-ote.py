class Note:
    long_notes = {'до': 'до-о', 'ре': 'ре-э', 'ми': 'ми-и',
                  'фа': 'фа-а', 'соль': 'со-оль', 'ля': 'ля-а', 'си': 'си-и'}

    def __init__(self, octave, is_long=False):
        if is_long:
            self.octave = self.long_notes[octave]
        else:
            self.octave = octave

    def __str__(self):
        return self.octave
