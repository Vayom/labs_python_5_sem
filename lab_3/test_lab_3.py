import os
import re
import unittest
from unittest.mock import patch, Mock
import lab_3

words_list = ['Pharetra', 'diam', 'sit', 'amet', 'nisl', 'suscipit', 'adipiscing', 'bibendum', 'est', 'ultricies',
              'Sem', 'nulla', 'pharetra', 'diam', 'sit', 'amet', 'nisl', 'Est', 'velit', 'egestas', 'dui', 'id',
              'ornare', 'arcu', 'odio',
              'ut']
expected_text = "Pharetra diam sit amet nisl suscipit adipiscing bibendum est ultricies.\n" \
                "Sem nulla pharetra diam sit amet nisl. Est velit egestas dui id ornare arcu odio ut."


class TestLab(unittest.TestCase):

    @patch('builtins.input', side_effect=['test_lab_3.txt'])
    def test_take_file_text(self, mock_input):
        result = lab_3.take_file_text()
        self.assertEqual(result, expected_text)

    def test_split_file_test(self):
        result = lab_3.split_file_test(expected_text)
        self.assertEqual(result, words_list)

    @patch('lab_3.split_file_test')
    def test_text_is_not_empty(self, mock_return):
        mock_return.return_value = words_list
        result = lab_3.text_is_empty(expected_text)
        print(result)
        self.assertEqual(result, False)

    @patch('lab_3.split_file_test')
    def test_text_is_empty(self, mock_return):
        mock_return.return_value = []
        result = lab_3.text_is_empty(expected_text)
        print(result)
        self.assertEqual(result, True)

    @patch('lab_3.split_file_test')
    def test_find_most_popular_words(self, mock_return):
        mock_return.return_value = words_list
        result = lab_3.find_most_popular_words(expected_text)
        self.assertEqual(result, 'nisl')

    @patch('lab_3.split_file_test')
    def test_count_words(self, mock_return):
        mock_return.return_value = words_list
        result = lab_3.count_words(expected_text)
        self.assertEqual(result, 26)

    def test_number_of_characters(self):
        result = lab_3.number_of_characters(expected_text)
        self.assertEqual(result, 156)


if __name__ == "__main__":
    unittest.main()