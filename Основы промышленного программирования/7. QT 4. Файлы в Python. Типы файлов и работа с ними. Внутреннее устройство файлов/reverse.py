def reverse():
    with open('input.dat', 'rb') as fr, open('output.dat', 'wb') as fw:
        fw.write(fr.read()[::-1])
