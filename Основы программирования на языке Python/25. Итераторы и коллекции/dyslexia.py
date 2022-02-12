import itertools


def isdyslexia(dictionary: set, word):
    word = word.lower()
    perms = {''.join(i) for i in itertools.permutations(word)}
    intersection = perms & dictionary
    if not intersection or intersection == {word}:
        return False
    return True


def main():
    dictionary = {i.lower() for i in input().split()}
    text = input().split()
    res = ('#' * len(x) if isdyslexia(dictionary, x) else x for x in text)
    print(*res)


main()