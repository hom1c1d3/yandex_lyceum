def parchment(string, divisor=' '):
    global snuffbox
    snuffbox = list(snuffbox)
    for ind, i in enumerate(snuffbox):
        snuffbox[ind] = divisor.join(set(i) - set(string))
    snuffbox = tuple(snuffbox)


snuffbox = ('black', 'powder', 'piece', 'parchment')
parchment('caliph stork', divisor=' ')
print(snuffbox)