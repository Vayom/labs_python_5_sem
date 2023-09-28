def take_file_text(file_path):
    with open(file_path) as file:
        file_text = file.read()
        return file_text
