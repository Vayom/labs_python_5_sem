from .field_borehole import FuelBorehole


class GasBorehole(FuelBorehole):
    def __init__(self, level):
        super().__init__(level)
        self.need_water = 3

    def __str__(self):
        return f'{type(self)} - {self.level} - уровня. Добыто - {self.stats_pump_fuel} единиц газа'
