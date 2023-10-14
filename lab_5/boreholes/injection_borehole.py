
from .borehole import Borehole


class InjectionBorehole(Borehole):
    def __init__(self, level):
        super().__init__(level)

    def calculate_speed(self):
        if self.level == 1:
            self.speed = 15
        elif self.level == 2:
            self.speed = 40
        elif self.level == 3:
            self.speed = 100

    def give_water(self):
        return self.speed
