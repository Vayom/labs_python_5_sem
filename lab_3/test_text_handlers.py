import os
import unittest
from unittest.mock import patch, Mock
from modules.text_handlers import *

words_list = ['Pharetra', 'diam', 'sit', 'amet', 'nisl', 'suscipit', 'adipiscing', 'bibendum', 'est', 'ultricies',
              'Sem', 'nulla', 'pharetra', 'diam', 'sit', 'amet', 'nisl', 'Est', 'velit', 'egestas', 'dui', 'id',
              'ornare', 'arcu', 'odio',
              'ut']
expected_text = "Pharetra diam sit amet nisl suscipit adipiscing bibendum est ultricies.\n" \
                "Sem nulla pharetra diam sit amet nisl. Est velit egestas dui id ornare arcu odio ut."


class TestTextHandlers(unittest.TestCase):

    def test_split_file_test_with_delimiters(self):
        result = split_file_test('0.0?0,0:0;0\\0/0|0!0(0)[0]0{0}0\'0"0\n0\t0')
        self.assertEqual(len(result), 19)

    def test_split_file_test_without_delimiters(self):
        result = split_file_test(
            'Lorem0ipsum0dolor00sit0amet1consectetuer0adipiscing0elit0Aenean0commodo0ligula0eget0dolor0')
        self.assertEqual(len(result), 1)

    @patch('modules.text_handlers.split_file_test')
    def test_text_is_not_empty(self, mock_return):
        mock_return.return_value = words_list
        result = text_is_empty(expected_text)
        print(result)
        self.assertEqual(result, False)

    @patch('modules.text_handlers.split_file_test')
    def test_text_is_empty(self, mock_return):
        mock_return.return_value = []
        result = text_is_empty(expected_text)
        print(result)
        self.assertEqual(result, True)

    @patch('modules.text_handlers.text_is_empty', return_value=False)
    @patch('modules.text_handlers.split_file_test', return_value=words_list)
    def test_find_most_popular_words(self, mock_is_empty, mock_split):
        result = find_most_popular_words(expected_text)
        self.assertEqual(result, 'nisl')

    @patch('modules.text_handlers.text_is_empty', return_value=True)
    @patch('modules.text_handlers.split_file_test', return_value=words_list)
    def test_find_most_popular_words_empty(self, mock_is_empty, mock_split):
        result = find_most_popular_words(expected_text)
        self.assertEqual(result, None)

    @patch('modules.text_handlers.text_is_empty', return_value=False)
    @patch('modules.text_handlers.split_file_test', return_value=words_list)
    def test_count_words(self, mock_is_empty, mock_split):
        result = count_words(expected_text)
        self.assertEqual(result, 26)

    @patch('modules.text_handlers.text_is_empty', return_value=True)
    @patch('modules.text_handlers.split_file_test', return_value=words_list)
    def test_count_words_empty(self, mock_is_empty, mock_split):
        result = count_words(expected_text)
        self.assertEqual(result, None)

    def test_number_of_characters(self):
        result = number_of_characters(expected_text)
        self.assertEqual(result, 156)


if __name__ == "__main__":
    unittest.main()
