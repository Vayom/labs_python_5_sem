class OilField:
    def __init__(self, gas_volume=0, oil_volume=0, water_volume=0):
        self.money = 0
        self.gas_volume = gas_volume
        self.oil_volume = oil_volume
        self.water_volume = water_volume
        self.boreholes = []

    def add_borehole(self, well): #null
        self.boreholes.append(well)

    def remove_borehole(self, well):
        self.boreholes.remove(well)

    def pop_borehole(self, index):
        self.boreholes.pop(index)

    def sleep_for_volume(self):
        add_oil = 0
        add_gas = 0
        add_water = 0
        for borehole in self.boreholes:
            if borehole.borehole_type == 'oil':
                add_oil += borehole.speed
                self.oil_volume += borehole.speed
            elif borehole.borehole_type == 'gas':
                add_gas += borehole.speed
                self.gas_volume += borehole.speed
            elif borehole.borehole_type == 'water':
                add_water += borehole.speed
                self.water_volume += borehole.speed
        return [add_oil, add_gas, add_water]

    def show_boreholes(self):
        count = 1
        for borehole in self.boreholes:
            print(f'{count}) {borehole}')
            count += 1

    def show_boreholes_for_up(self):
        count = 1
        for borehole in self.boreholes:
            if borehole.level < 3:
                print(f'{count}) {borehole}')
                count += 1

    def count_boreholes_for_up(self):
        count = 0
        for borehole in self.boreholes:
            if borehole.level < 3:
                count += 1
        return count

    def give_borehole_for_up(self, number):
        count = 0
        for borehole in self.boreholes:
            if borehole.level < 3:
                count += 1
                if count == number:
                    return borehole


