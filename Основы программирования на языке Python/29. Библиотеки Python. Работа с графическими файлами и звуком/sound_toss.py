import wave
import struct


def pitch_and_toss():
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")

    dest.setparams(source.getparams())

    frames_count = source.getnframes()

    data = struct.unpack("<" + str(frames_count) + "h",
                         source.readframes(frames_count))

    quoter = len(data) // 4
    a, b, c, d = data[:quoter], data[quoter:quoter * 2], data[quoter * 2:quoter * 3], data[
                                                                                      quoter * 3:]
    newdata = c + d + a + b

    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

    dest.writeframes(newframes)
    source.close()
    dest.close()
