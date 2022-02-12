def get_address_span(toponym):
    envelope = toponym['boundedBy']['Envelope']
    left, bottom = envelope["lowerCorner"].split(" ")
    right, top = envelope["upperCorner"].split(" ")
    dx = abs(float(left) - float(right)) / 2.0
    dy = abs(float(top) - float(bottom)) / 2.0
    return round(dx, 5), round(dy, 5)