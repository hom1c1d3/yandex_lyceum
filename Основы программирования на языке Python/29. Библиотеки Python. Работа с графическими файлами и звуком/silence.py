import wave
import struct


def break_the_silence():
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")

    dest.setparams(source.getparams())

    # найдем количество фреймов
    frames_count = source.getnframes()

    data = struct.unpack("<" + str(frames_count) + "h",
                         source.readframes(frames_count))

    # собственно, основная строка программы - переворот списка
    newdata = tuple(filter(lambda x: x not in range(-5, 6), data))

    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

    # записываем содержимое в преобразованный файл.
    dest.writeframes(newframes)
    source.close()
    dest.close()
