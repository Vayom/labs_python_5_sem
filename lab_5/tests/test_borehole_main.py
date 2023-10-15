import unittest

from lab_5.boreholes import Borehole


class TestBorehole(unittest.TestCase):
    def test_initialization(self):
        borehole = Borehole(1)
        self.assertEqual(borehole.level, 1)
        self.assertEqual(borehole.speed, 5)
        self.assertTrue(borehole.is_enabled)

    def test_turn_on(self):
        borehole = Borehole(2)
        borehole.is_enabled = False
        borehole.turn_on()
        self.assertTrue(borehole.is_enabled)

    def test_turn_off(self):
        borehole = Borehole(3)
        borehole.turn_off()
        self.assertFalse(borehole.is_enabled)

    def test_level_setting(self):
        borehole = Borehole(1)
        borehole.set_parameters(3)
        self.assertEqual(borehole.level, 3)
        self.assertEqual(borehole.speed, 30)

    def test_invalid_level_setting(self):
        borehole = Borehole(1)
        with self.assertRaises(ValueError):
            borehole.set_parameters(4)


if __name__ == '__main__':
    unittest.main()
