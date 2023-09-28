import os
import tempfile
import unittest
from unittest.mock import patch, Mock, mock_open
from .modules.file_handlers import *

read_text = "Pharetra diam sit amet nisl suscipit adipiscing bibendum est ultricies.\n" \
            "Sem nulla pharetra diam sit amet nisl. Est velit egestas dui id ornare arcu odio ut."


class TestFileHandlers(unittest.TestCase):
    @patch('builtins.open', read_data=read_text)
    def test_take_file_text(self, mock_file):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(read_text)
        file_path = temp_file.name
        result = take_file_text(file_path)
        self.assertEqual(result, read_text)
        os.remove(file_path)

    """@patch('builtins.open', side_effect=FileNotFoundError)
    def test_take_file_text_with_error(self, mock_file_open):
        file_path = "not_founded_file.txt"

        with self.assertRaises(FileNotFoundError):
            take_file_text(file_path)"""


if __name__ == "__main__":
    unittest.main()
