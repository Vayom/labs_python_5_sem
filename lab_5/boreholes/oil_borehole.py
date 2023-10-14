from lab_5.boreholes.field_borehole import FuelBorehole


class OilBorehole(FuelBorehole):
    def __init__(self, level):
        super().__init__(level)
        self.need_water = 5

    def __str__(self):
        return f'{type(self)} - {self.level} - уровня. Добыто - {self.stats_pump_fuel} единиц воды'
