from .borehole import Borehole


class FuelBorehole(Borehole):
    def __init__(self, level):
        super().__init__(level)
        self.need_water = 0
        self.stats_pump_fuel = 0

    def give_oil(self, water):
        if water > self.need_water:
            self.stats_pump_fuel += self.speed
            return self.speed
    def __str__(self):
        return f'{type(self)} - {self.level} - уровня. Добыто - {self.stats_pump_fuel}'
