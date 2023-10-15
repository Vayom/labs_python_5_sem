from .fuel_borehole import FuelBorehole
from .oil_borehole import OilBorehole
from .gas_borehole import GasBorehole
from .injection_borehole import InjectionBorehole


class OilField:
    def __init__(self, gas_volume=0, oil_volume=0, water_volume=0):
        self.money = 0
        self.gas_volume = gas_volume
        self.oil_volume = oil_volume
        self.water_volume = water_volume
        self.fuel_boreholes = []
        self.injection_boreholes = []

    def add_borehole(self, borehole):  # null
        if isinstance(borehole, FuelBorehole):
            self.fuel_boreholes.append(borehole)
        elif isinstance(borehole, InjectionBorehole):
            self.injection_boreholes.append(borehole)

    def remove_borehole(self, well):
        if isinstance(well, FuelBorehole):
            self.fuel_boreholes.remove(well)
        else:
            self.injection_boreholes.remove(well)

    def pump_water(self):
        if self.injection_boreholes:
            for borehole in self.injection_boreholes:
                if borehole.is_enabled:
                    self.water_volume += borehole.give_water()

    def pump_fuel(self):
        for borehole in self.fuel_boreholes:
            if borehole.is_enabled:
                if isinstance(borehole, OilBorehole):
                    if self.water_volume >= borehole.need_water:
                        self.oil_volume += borehole.give_oil(borehole.need_water)
                        self.water_volume -= borehole.need_water
                elif isinstance(borehole, GasBorehole):
                    if self.water_volume >= borehole.need_water:
                        self.gas_volume += borehole.give_oil(borehole.need_water)
                        self.water_volume -= borehole.need_water

    def show_boreholes(self):
        count = 1
        for borehole in self.fuel_boreholes:
            print(f'{count}) {borehole}')
            count += 1
        for borehole in self.injection_boreholes:
            print(f'{count}) {borehole}')
            count += 1


if __name__ == '__main__':
    pass
