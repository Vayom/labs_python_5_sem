from .borehole import Borehole


class OilBorehole(Borehole):
    def __init__(self, borehole_type, level):
        super().__init__(borehole_type, level)
