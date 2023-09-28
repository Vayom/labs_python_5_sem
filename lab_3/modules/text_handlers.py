import re


def split_file_test(file_text):
    pattern = r'[/\\,.1;!?:|\'/(\[\])@\-\+ \\"{}\n\t_]+'
    file_words = re.split(pattern, file_text)
    if '' in file_words:
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
    if not text_is_empty(file_text):
        words_count = {}
        file_words = split_file_test(file_text)
        for word in file_words:
            if word != '':
                if word not in words_count:
                    words_count[word] = 0
                words_count[word] += 1
        sorted_tuple = sorted(words_count.items(), key=lambda x: x[1])
        return sorted_tuple[-1][0]


def count_words(file_text: str) -> int:
    """
    Function for counting the number of words
        :param file_text: str - text file
        :return: int - Number of words
    """
    if not text_is_empty(file_text):
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


if __name__ == '__main__':
    pass
