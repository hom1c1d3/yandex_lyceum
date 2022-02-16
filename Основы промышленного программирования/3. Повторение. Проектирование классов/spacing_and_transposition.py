from functools import total_ordering


N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


@total_ordering
class Note:

    def __init__(self, sound, is_long=False):
        self.sound = sound
        self.is_long = is_long
        self.frequency = PITCHES.index(sound)

    def __str__(self):
        if self.is_long:
            return dict(zip(PITCHES, LONG_PITCHES))[self.sound]
        else:
            return self.sound

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __rshift__(self, other: int):
        shift = (other + self.frequency) % len(PITCHES)
        shifted_note = Note(PITCHES[shift], self.is_long)
        return shifted_note

    def __lshift__(self, other: int):
        shift = (self.frequency - other) % len(PITCHES)
        shifted_note = Note(PITCHES[shift], self.is_long)
        return shifted_note

    def get_interval(self, other):
        delta = abs(self.frequency - other.frequency)
        interval = INTERVALS[delta]
        return interval
