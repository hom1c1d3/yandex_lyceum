from itertools import groupby


class MinMaxWordFinder:

    def __init__(self):
        self.sentences = []

    def add_sentence(self, string):
        self.sentences.extend(string.split())

    def shortest_words(self):
        res = [sorted(v) for k, v in groupby(sorted(self.sentences, key=len), key=len)]
        return res[0] if res else []

    def longest_words(self):
        res = [sorted(v) for k, v in groupby(sorted(self.sentences, key=len), key=len)]
        return sorted(set(res[-1])) if res else []