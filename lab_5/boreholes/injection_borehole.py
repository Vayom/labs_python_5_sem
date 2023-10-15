from .borehole import Borehole


class InjectionBorehole(Borehole):
    def __init__(self, level):
        super().__init__(level)
        self.stats_pump_fuel = 0

    def calculate_speed(self):
        if self.level == 1:
            self.speed = 15
        elif self.level == 2:
            self.speed = 40
        elif self.level == 3:
            self.speed = 100

    def give_water(self):
        self.stats_pump_fuel += self.speed
        return self.speed

    def __str__(self):
        return f'Нагнетающая скважина - {self.level} - уровня. Добыто - {self.stats_pump_fuel} единиц воды'


if __name__ == "__main__":
    pass
