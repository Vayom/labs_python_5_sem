import unittest

from lab_5.boreholes import InjectionBorehole


class TestInjectionBorehole(unittest.TestCase):
    def test_initialization(self):
        borehole = InjectionBorehole(2)
        self.assertEqual(borehole.level, 2)
        self.assertEqual(borehole.speed, 40)
        self.assertTrue(borehole.is_enabled)
        self.assertEqual(borehole.stats_pump_fuel, 0)

    def test_give_water(self):
        borehole = InjectionBorehole(3)
        water_pumped = borehole.give_water()
        self.assertEqual(water_pumped, 100)
        self.assertEqual(borehole.stats_pump_fuel, 100)