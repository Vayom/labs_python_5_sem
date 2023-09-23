import os
import unittest
from unittest.mock import patch
from lab_3 import take_file_text


class TestLab(unittest.TestCase):
    @patch('builtins.input', side_effect=['test_lab_3.txt'])
    def test_take_file_text(self, mock_input):
        # Вызываем функцию и проверяем, что она возвращает ожидаемый текст
        expected_text = "Pharetra diam sit amet nisl suscipit adipiscing bibendum est ultricies.\n" \
                        "Sem nulla pharetra diam sit amet nisl. Est velit egestas dui id ornare arcu odio ut."
        result = take_file_text()
        self.assertEqual(result, expected_text)

        # Удаляем временный файл
        os.remove('test.txt')
