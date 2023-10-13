import io
import unittest
from unittest.mock import patch, Mock, mock_open

from lab_5.boreholes import Borehole
from lab_5.boreholes.oil_field import OilField


class TestOilField(unittest.TestCase):

    def setUp(self):
        self.field = OilField()
        self.borehole1 = Borehole('oil', 3)
        self.borehole2 = Borehole('gas', 2)

    def test_add_borehole(self):
        borehole = Borehole('oil', 3)
        self.field.add_borehole(borehole)
        self.assertIn(borehole, self.field.boreholes)

    def test_remove_borehole(self):
        self.field.boreholes.append(self.borehole1)
        self.field.remove_borehole(self.borehole1)
        self.assertNotIn(self.borehole1, self.field.boreholes)

    def test_pop_borehole(self):
        self.field.boreholes.append(self.borehole1)
        self.field.boreholes.append(self.borehole2)
        self.field.pop_borehole(0)
        self.assertNotIn(self.borehole1, self.field.boreholes)
        self.assertIn(self.borehole2, self.field.boreholes)

    def test_show_boreholes(self):
        self.field.boreholes.append(self.borehole1)
        self.field.boreholes.append(self.borehole2)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.field.show_boreholes()  # Вызываем метод

            output = mock_stdout.getvalue()  # Получаем вывод

        # Проверяем, что вывод содержит ожидаемую строку
        expected_output = "1) oil - 3, 30\n2) gas - 2, 15\n"
        self.assertEqual(output, expected_output)
