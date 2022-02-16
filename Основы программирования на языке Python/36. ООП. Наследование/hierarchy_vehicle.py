class Transport:
    pass


class GroundTransport(Transport):
    pass


class WaterTransport(Transport):
    pass


class AirTransport(Transport):
    pass


class RoadTransport(GroundTransport):
    pass


class RailTransport(GroundTransport):
    pass


class AboveWaterTransport(WaterTransport):
    pass


class UnderWaterTransport(WaterTransport):
    pass


class Car(RoadTransport):
    pass


class Bicycle(RoadTransport):
    pass


class Train(RailTransport):
    pass


class Trolley(RailTransport):
    pass


class Boat(AboveWaterTransport):
    pass


class Freighter(AboveWaterTransport):
    pass


class Submarine(UnderWaterTransport):
    pass


class Bathyscap(UnderWaterTransport):
    pass


class Plane(AirTransport):
    pass


class Aerostat(AirTransport):
    pass