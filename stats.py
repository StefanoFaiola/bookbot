import os


def get_book_text(path):
    print(f'Analyzinbg book found at books/{os.path.basename(path)}...')
    with open(path, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents


def get_num_words(text):
    count_words = len(text.split())
    return count_words

def count_letters(text):
    
    unique_char = set(text.lower())
    text_low = text.lower()
    char_count = {}

    for i in unique_char:
        c = text_low.count(i)
        char_count[i] = c
    
    sorted_char = dict(sorted(char_count.items(), key = lambda item: item[1], reverse=True))

    return sorted_char