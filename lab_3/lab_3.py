import modules


try:
    file_path = input('Input file path\n')
    text = modules.take_file_text(file_path)
    if not modules.text_is_empty(text):
        most_popular_word = modules.find_most_popular_words(text)
        print(f'The most popular word - {most_popular_word}')
        print(f'Number of words - {modules.count_words(text)}')
        print(f'Number of characters - {modules.number_of_characters(text)}')
    else:
        print('Text is empty')
except FileNotFoundError:
    print('No such file or directory')
except Exception as error:
    print(error)
