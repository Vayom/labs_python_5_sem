from lab_5.boreholes.field_borehole import FuelBorehole
from lab_5.boreholes.oil_borehole import OilBorehole


class OilField:
    def __init__(self, gas_volume=0, oil_volume=0, water_volume=0):
        self.money = 0
        self.gas_volume = gas_volume
        self.oil_volume = oil_volume
        self.water_volume = water_volume
        self.fuel_boreholes = []
        self.injection_boreholes = []

    def add_fuel_borehole(self, borehole):  # null
        if isinstance(borehole, FuelBorehole):
            self.fuel_boreholes.append(borehole)
        else:
            self.injection_boreholes.append(borehole)

    def remove_borehole(self, well):
        if isinstance(well, FuelBorehole):
            self.fuel_boreholes.remove(well)
        else:
            self.injection_boreholes.remove(well)

    def pump_water(self):
        if self.injection_boreholes:
            for borehole in self.injection_boreholes:
                self.water_volume += borehole.give_water

    def pump_fuel(self):
        for borehole in self.fuel_boreholes:
            if isinstance(borehole, OilBorehole):
                if self.water_volume >= borehole.need_water:
                    self.oil_volume += borehole.give_oil(borehole.need_water)
            else:
                if self.water_volume >= borehole.need_water:
                    self.gas_volume += borehole.give_oil(borehole.need_water)
                else:
                    print('Вода закончилась')
                    break

    def show_boreholes(self):
        count = 1
        for borehole in self.fuel_boreholes:
            print(f'{count}) {borehole}')
            count += 1
        for borehole in self.injection_boreholes:
            print(f'{count}) {borehole}')
            count += 1
