from boreholes.injection_borehole import InjectionBorehole
from boreholes.oil_borehole import OilBorehole
from boreholes.gas_borehole import GasBorehole
from boreholes.oil_field import OilField


class Game:
    """shop_boreholes = {OilBorehole(level=1): 100,
                      GasBorehole(level=1): 50,
                      InjectionBorehole(level=1): 30,
                      OilBorehole(level=2): 250,
                      GasBorehole(level=2): 120,
                      InjectionBorehole(level=2): 80,
                      OilBorehole(level=3): 550,
                      GasBorehole(level=3): 250,
                      InjectionBorehole(level=3): 200,
                      }"""

    def __init__(self, start_borehole):
        self.oil_field = OilField()
        self.oil_field.add_borehole(start_borehole)

    def start(self):
        while True:
            self.navigate(self)

    def navigate_actions(self, choice):
        if choice == 1:
            self.sell_fuel()
        elif choice == 2:
            self.shop()
        elif choice == 3:
            self.sleep_for_volume()
        elif choice == 4:
            self.sell_boreholes()
        elif choice == 5:
            exit()

    def sleep_for_volume(self):
        add_fuel = self.oil_field.sleep_for_volume()
        print(f'+{add_fuel[0]} oil\n'
              f'+{add_fuel[1]} gas\n'
              f'+{add_fuel[2]} water')

    def sell_fuel(self):
        add_coins = 0
        add_coins += self.oil_field.oil_volume * 0.4
        add_coins += self.oil_field.gas_volume * 0.2
        add_coins += self.oil_field.water_volume * 0.1
        print(f'Coins received - {add_coins}')
        print(f'Fuel sold:\n'
              f'{self.oil_field.oil_volume} - oil\n'
              f'{self.oil_field.gas_volume} - gas\n'
              f'{self.oil_field.water_volume} - water')
        self.oil_field.oil_volume = 0
        self.oil_field.gas_volume = 0
        self.oil_field.water_volume = 0
        self.oil_field.money += add_coins

    def take_money_from_sell(self, borehole):
        if borehole.borehole_type == 'oil':
            if borehole.level == 1:
                self.oil_field.money += 50
            elif borehole.level == 2:
                self.oil_field.money += 125
            elif borehole.level == 3:
                self.oil_field.money += 225
        elif borehole.borehole_type == 'gas':
            if borehole.level == 1:
                self.oil_field.money += 25
            elif borehole.level == 2:
                self.oil_field.money += 60
            elif borehole.level == 3:
                self.oil_field.money += 125
        elif borehole.borehole_type == 'water':
            if borehole.level == 1:
                self.oil_field.money += 15
            elif borehole.level == 2:
                self.oil_field.money += 40
            elif borehole.level == 3:
                self.oil_field.money += 100

    def sell_boreholes(self):
        choice = None
        self.oil_field.show_boreholes()
        print('0) Exit\n'
              'Choose a well for sale\n')
        while True:
            try:
                choice = int(input())
                if 0 <= choice <= len(self.oil_field.boreholes):
                    break
                else:
                    print(f'Choose 0 - {len(self.oil_field.boreholes)}')
            except ValueError:
                print('Value Error')
        if choice != 0:
            borehole = self.oil_field.boreholes[choice - 1]
            self.oil_field.pop_borehole(choice - 1)
            self.take_money_from_sell(borehole)

    """def upgrade_boreholes(self):
        self.oil_field.show_boreholes_for_up()
        count_for_up = self.oil_field.count_boreholes_for_up()
        print('0) Exit\n'
              'Choose a well for upgrade\n')
        while True:
            try:
                choice = int(input())
                if 0 <= choice <= count_for_up:
                    break
                else:
                    print(f'Choose 0 - {count_for_up}')
            except ValueError:
                print('Value Error')
        borehole = self.oil_field.give_borehole_for_up(choice)
        self.upgrade(borehole)"""

    @staticmethod
    def navigate(self):
        choice = None
        print('Actions\n'
              '1) Sell all fuel\n'
              '2) Shop\n'
              '3) Sleep\n'
              '4) Sell boreholes\n'
              '5) Exit')
        while True:
            try:
                choice = int(input())
                if 1 <= choice <= 5:
                    break
                else:
                    print('Choose 1 - 5 or 0')
            except ValueError:
                print('Value error\n')
        self.navigate_actions(choice)

    def shop_actions(self, choice):
        if choice == 1 and self.oil_field.money >= 100:
            self.oil_field.add_borehole(OilBorehole(level=1, borehole_type='oil'))
            self.oil_field.money -= 100
        elif choice == 2 and self.oil_field.money >= 50:
            self.oil_field.add_borehole(GasBorehole(level=1, borehole_type='gas'))
            self.oil_field.money -= 50
        elif choice == 3 and self.oil_field.money >= 30:
            self.oil_field.add_borehole(InjectionBorehole(level=1, borehole_type='water'))
            self.oil_field.money -= 30
        elif choice == 4 and self.oil_field.money >= 250:
            self.oil_field.add_borehole(OilBorehole(level=2, borehole_type='oil'))
            self.oil_field.money -= 250
        elif choice == 5 and self.oil_field.money >= 120:
            self.oil_field.add_borehole(GasBorehole(level=2, borehole_type='gas'))
            self.oil_field.money -= 120
        elif choice == 6 and self.oil_field.money >= 80:
            self.oil_field.add_borehole(InjectionBorehole(level=3, borehole_type='water'))
            self.oil_field.money -= 80
        elif choice == 7 and self.oil_field.money >= 550:
            self.oil_field.add_borehole(OilBorehole(level=3, borehole_type='oil'))
            self.oil_field.money -= 550
        elif choice == 8 and self.oil_field.money >= 250:
            self.oil_field.add_borehole(GasBorehole(level=3, borehole_type='gas'))
            self.oil_field.money -= 250
        elif choice == 9 and self.oil_field.money >= 200:
            self.oil_field.add_borehole(InjectionBorehole(level=3, borehole_type='water'))
            self.oil_field.money -= 200
        elif 1 <= choice <= 9:
            print('Not enough coins')

    def shop(self):
        choice = None
        print('Select the object of purchase\n'
              '1) Oil Borehole 1 lvl - 100 coins\n'
              '2) Gas Borehole 1 lvl - 50 coins\n'
              '3) Injections Borehole 1 lvl - 30 coins\n'
              '4) Oil Borehole 2 lvl - 250 coins\n'
              '5) Gas Borehole 2 lvl - 120 coins\n'
              '6) Injections Borehole 2 lvl - 80 coins\n'
              '7) Oil Borehole 3 lvl - 550 coins\n'
              '8) Gas Borehole 3 lvl - 250 coins\n'
              '9) Injections Borehole 3 lvl - 200 coins\n'
              '0) Exit\n'
              f'Your coint - {self.oil_field.money}\n')
        while True:
            try:
                choice = int(input())
                if 0 <= choice <= 9:
                    break
                else:
                    print('Choose 1 - 9 or 0')
            except ValueError:
                print('Value error\n')
        self.shop_actions(choice)
