from swift import words
import string
import random


def next_words_gen(curr_word):
    words_iter = iter(words)
    next(words_iter)  # первое слово
    for ind, i in enumerate(words):
        if i == curr_word:
            next_word = next(words_iter)
            if next_word not in string.punctuation:
                yield next_word
        else:
            try:
                next(words_iter)
            except StopIteration:
                pass


def random_sequence_gen(first_word, length=10):
    count = 0
    rand_word = first_word
    yield rand_word
    while count < length:
        next_words = list(next_words_gen(rand_word))
        if not next_words:
            return StopIteration
        rand_word = random.choice(next_words)

        yield rand_word
        count += 1


def text_gen(first_word, length=10):
    for i in range(length):
        sequence = ' '.join(random_sequence_gen(first_word))
        yield sequence
        if len(sequence.split()) < 2:
            first_word = random.choice(words)
        else:
            first_word = random.choice(sequence.split())


def main():
    first_word = random.choice(words)
    while first_word in string.punctuation:
        first_word = random.choice(words)
    res = [i.capitalize() + '.' for i in text_gen(first_word)]
    print(*res)


if __name__ == '__main__':
    main()