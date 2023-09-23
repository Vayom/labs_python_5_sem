import re

delimiters = ['\n', '\t', ':', '\'', '\"', '|', ';']
delimiters2 = ",;|"
del_string = ' '.join(delimiters)


def take_file_path() -> str:
    """
    Function for reading the file path
        :return: a file path
    """
    path = input('Input your file path\n')
    return path


def text_is_empty(file_text):
    """
    Function to check the emptiness of the text
        :param file_text: str - text file
        :return: bool - file is empty
    """
    pattern = r'[/\\,.;!?|\'/()@\-\+ \\"{}\n\t_]+'
    file_words = re.split(pattern, text)
    if not file_words:
        return True
    else:
        return False


def find_most_popular_words(file_text: str) -> str:
    """
    Function to search for the most popular word
        :param file_text: str - text file
        :return: str - most popular word
    """
    words_count = {}
    pattern = r'[\[\]/\\,.;!?|\'/()@\-\+ \"{}\n\t\r]+'
    file_words = re.split(pattern, text)
    for word in file_words:
        if word != '':
            if word not in words_count:
                words_count[word] = 0
            words_count[word] += 1
    sorted_tuple = sorted(words_count.items(), key=lambda x: x[1])
    print(sorted_tuple)
    # print(sorted_tuple)
    return sorted_tuple[-1][0]


def count_words(file_text: str) -> int:
    """
    Function for counting the number of words
        :param file_text: str - text file
        :return: int - Number of words
    """
    pattern = r'[/\\,.;!?|\'/()@\-\+ \\"{}\n\t_]+'
    words = re.split(pattern, text)
    return len(words)


def number_of_characters(file_text: str) -> int:
    """
    Function for counting the number of words
        :param file_text: str - text file
        :return: int - Number of characters
    """
    return len(file_text)

file_path = take_file_path()
try:
    with open(file_path) as f:
        text = f.read()
        # print(text)
        if not text_is_empty(text):
            most_popular_word = find_most_popular_words(text)
            print(f'The most popular word - {most_popular_word}')
            print(f'Number of words - {count_words(text)}')
            print(f'Number of characters - {number_of_characters(text)}')
        else:
            print('Text is empty')
except FileNotFoundError:
    print('No such file or directory')
except Exception as error:
    print(error)
