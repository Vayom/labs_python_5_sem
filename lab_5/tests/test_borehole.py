import io
import unittest
from unittest.mock import patch

from lab_5.boreholes import Borehole


class TestBorehole(unittest.TestCase):
    def setUp(self):
        self.borehole = Borehole("Water", 1)

    def test_turn_on(self):
        self.borehole.turn_on()
        self.assertTrue(self.borehole.is_enabled)

    @patch('lab_5.boreholes.Borehole.turn_on', side_effect=lambda self: setattr(self, 'is_enabled', True))
    def test_turn_off(self, mock_off):
        self.borehole.turn_off()
        self.assertFalse(self.borehole.is_enabled)

    def test_calculate_speed(self):
        self.borehole.level = 1
        self.borehole.calculate_speed()
        self.assertEqual(self.borehole.speed, 5)

        self.borehole.level = 2
        self.borehole.calculate_speed()
        self.assertEqual(self.borehole.speed, 15)

        self.borehole.level = 3
        self.borehole.calculate_speed()
        self.assertEqual(self.borehole.speed, 30)

    def test_set_parameters(self):
        self.borehole.set_parameters(100, 2)
        self.assertEqual(self.borehole.contents_volume, 100)
        self.assertEqual(self.borehole.level, 2)
        self.assertEqual(self.borehole.speed, 15)

    def test_print(self):
        expected_output = "Water - 1, 5"
        self.assertEqual(str(self.borehole), expected_output)
