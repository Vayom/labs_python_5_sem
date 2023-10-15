import unittest

from lab_5.boreholes import FuelBorehole


class TestFuelBorehole(unittest.TestCase):
    def test_initialization(self):
        fuel_borehole = FuelBorehole(2)
        self.assertEqual(fuel_borehole.level, 2)
        self.assertEqual(fuel_borehole.speed, 15)
        self.assertTrue(fuel_borehole.is_enabled)
        self.assertEqual(fuel_borehole.need_water, 0)
        self.assertEqual(fuel_borehole.stats_pump_fuel, 0)

    def test_give_oil_with_enough_water(self):
        fuel_borehole = FuelBorehole(3)
        fuel_borehole.need_water = 20
        fuel_borehole.speed = 30
        oil_pumped = fuel_borehole.give_oil(25)
        self.assertEqual(oil_pumped, 30)
        self.assertEqual(fuel_borehole.stats_pump_fuel, 30)

    def test_give_oil_with_insufficient_water(self):
        fuel_borehole = FuelBorehole(1)
        fuel_borehole.need_water = 5
        oil_pumped = fuel_borehole.give_oil(3)
        self.assertIsNone(oil_pumped)
        self.assertEqual(fuel_borehole.stats_pump_fuel, 0)

    def test_string_representation(self):
        fuel_borehole = FuelBorehole(1)
        fuel_borehole.need_water = 5
        fuel_borehole.give_oil(5)
        expected_string = "Добывающая скважина - 1 - уровня. Добыто - 5"
        self.assertEqual(str(fuel_borehole), expected_string)


if __name__ == "__main__":
    unittest.main()
