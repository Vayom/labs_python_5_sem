import re


def split_file_test(file_text):
    pattern = r'[/\\,.;!?|\'/()@\-\+ \\"{}\n\t_]+'
    file_words = re.split(pattern, file_text)
    file_words.remove('')
    return file_words


def text_is_empty(file_text):
    """
    Function to check the emptiness of the text
        :param file_text: str - text file
        :return: bool - file is empty
    """
    file_words = split_file_test(file_text)
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
    file_words = split_file_test(file_text)
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
    words = file_words = split_file_test(file_text)
    print(words)
    return len(words)


def number_of_characters(file_text: str) -> int:
    """
    Function for counting the number of words
        :param file_text: str - text file
        :return: int - Number of characters
    """
    return len(file_text)


def take_file_text():
    file_path = input('Input your file path\n')
    with open(file_path) as file:
        file_text = file.read()
        return file_text


try:
    text = take_file_text()
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
