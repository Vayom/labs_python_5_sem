from .fuel_borehole import FuelBorehole


class OilBorehole(FuelBorehole):
    def __init__(self, level):
        super().__init__(level)
        self.need_water = 5

    def __str__(self):
        return f'Нефтяная скважина - {self.level} - уровня. Добыто - {self.stats_pump_fuel} единиц нефти'


if __name__ == '__main__':
    pass
