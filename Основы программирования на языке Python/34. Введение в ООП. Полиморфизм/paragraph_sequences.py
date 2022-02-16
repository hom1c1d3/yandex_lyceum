class LeftParagraph:

    def __init__(self, paragraph_width):
        self.paragraph_width = paragraph_width
        self.words = [[]]
        self.line_last = paragraph_width

    def add_word(self, word):
        if len(word) > self.line_last:
            self.words.append([])
            self.line_last = self.paragraph_width

        self.words[-1].append(word)
        self.line_last -= len(word) + 1

    def end(self):
        for i in self.words:
            print(' '.join(i).ljust(self.paragraph_width))
        self.__init__(self.paragraph_width)


class RightParagraph(LeftParagraph):

    def end(self):
        for i in self.words:
            print(' '.join(i).rjust(self.paragraph_width))
        self.__init__(self.paragraph_width)


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()
