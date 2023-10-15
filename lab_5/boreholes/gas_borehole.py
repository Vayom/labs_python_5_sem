from .fuel_borehole import FuelBorehole


class GasBorehole(FuelBorehole):
    def __init__(self, level):
        super().__init__(level)
        self.need_water = 3

    def __str__(self):
        return f'Газовая скважина - {self.level} - уровня. Добыто - {self.stats_pump_fuel} единиц газа'


if __name__ == '__main__':
    pass
