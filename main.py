import os

def main():
    def read_book(path):
        print(f'--- Begin report of books/{os.path.basename(path)} ---')
        with open(path) as f:
            file_contents = f.read()
        return file_contents


    def count_words(text):
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

    book = read_book('/home/stefano/workspace/github.com/StefanoFaiola/bookbot/books/frankenstein.txt')
    count_w = count_words(book)
    count_l = count_letters(book)
    print(f'{count_w} words found in the document\n')

    for i in count_l:
        if i.isalpha():
            print(f"The '{i}' character was found {count_l[i]} times")


if __name__ == '__main__':
    main()
