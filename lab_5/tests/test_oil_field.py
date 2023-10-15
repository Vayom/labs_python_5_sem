import unittest
from io import StringIO
from unittest.mock import patch

from lab_5.boreholes import OilField, FuelBorehole, InjectionBorehole, GasBorehole, OilBorehole


class TestOilField(unittest.TestCase):
    def test_add_fuel_borehole(self):
        oil_field = OilField()
        fuel_borehole = FuelBorehole(1)
        oil_field.add_borehole(fuel_borehole)
        self.assertIn(fuel_borehole, oil_field.fuel_boreholes)

    def test_add_injection_borehole(self):
        oil_field = OilField()
        injection_borehole = InjectionBorehole(1)
        oil_field.add_borehole(injection_borehole)
        self.assertIn(injection_borehole, oil_field.injection_boreholes)

    def test_add_None(self):
        oil_field = OilField()
        oil_field.add_borehole(None)
        self.assertNotIn(None, oil_field.fuel_boreholes)
        self.assertNotIn(None, oil_field.injection_boreholes)

    def test_remove_borehole(self):
        oil_field = OilField()
        fuel_borehole = FuelBorehole(2)
        oil_field.add_borehole(fuel_borehole)
        oil_field.remove_borehole(fuel_borehole)
        self.assertNotIn(fuel_borehole, oil_field.fuel_boreholes)

    def test_remove_not_exists_borehole(self):
        oil_field = OilField()
        fuel_borehole = FuelBorehole(2)
        fuel_borehole2 = FuelBorehole(3)
        oil_field.add_borehole(fuel_borehole)
        with self.assertRaises(ValueError):
            oil_field.remove_borehole(fuel_borehole2)

    @patch('lab_5.boreholes.InjectionBorehole.give_water', return_value=50)
    def test_pump_water(self, mock_water):
        oil_field = OilField()
        injection_borehole = InjectionBorehole(1)
        oil_field.add_borehole(injection_borehole)
        oil_field.pump_water()
        self.assertEqual(oil_field.water_volume, mock_water.return_value)

    @patch('lab_5.boreholes.GasBorehole.give_oil', return_value=10)
    @patch('lab_5.boreholes.OilBorehole.give_oil', return_value=20)
    def test_pump_fuel_with_enough_water(self, mock_oil, mock_gas):
        oil_field = OilField()
        oil_borehole = OilBorehole(1)
        gas_borehole = GasBorehole(1)
        oil_field.add_borehole(gas_borehole)
        oil_field.add_borehole(oil_borehole)
        oil_field.water_volume = 30
        oil_field.pump_fuel()
        self.assertEqual(oil_field.oil_volume, mock_oil.return_value)
        self.assertEqual(oil_field.gas_volume, mock_gas.return_value)
        self.assertEqual(oil_field.water_volume, 22)

    @patch('lab_5.boreholes.GasBorehole.give_oil', return_value=None)
    def test_pump_fuel_with_not_exists_water(self, mock_gas):
        oil_field = OilField()
        gas_borehole = GasBorehole(1)
        oil_field.add_borehole(gas_borehole)
        oil_field.water_volume = 0
        oil_field.pump_fuel()
        self.assertEqual(oil_field.gas_volume, 0)
        self.assertEqual(oil_field.water_volume, 0)

    def test_show_boreholes(self):
        oil_field = OilField()
        borehole1 = OilBorehole(1)
        borehole2 = GasBorehole(2)
        borehole3 = InjectionBorehole(3)
        oil_field.add_borehole(borehole1)
        oil_field.add_borehole(borehole2)
        oil_field.add_borehole(borehole3)
        oil_field.pump_water()
        oil_field.pump_fuel()

        # Создаем объекты borehole и добавляем их в oil_field.fuel_boreholes и oil_field.injection_boreholes

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            oil_field.show_boreholes()
            output = mock_stdout.getvalue()

        # Проверяем, что вывод соответствует ожиданиям
        expected_output = "1) Нефтяная скважина - 1 - уровня. Добыто - 5 единиц нефти\n" \
                          "2) Газовая скважина - 2 - уровня. Добыто - 15 единиц газа\n" \
                          "3) Нагнетающая скважина - 3 - уровня. Добыто - 100 единиц воды\n"

        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
