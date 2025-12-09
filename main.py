import sys
from stats import get_num_words
from stats import get_book_text
from stats import count_letters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book = get_book_text(f'/mnt/c/Users/stepf/workspace/github.com/StefanoFaiola/bookbot/{sys.argv[1]}')
    print("----------- Word Count ----------")
    count_w = get_num_words(book)
    print(f'Found {count_w} total words')
    print("--------- Character Count -------")
    count_l = count_letters(book)
 
    

    for i in count_l:
        if i.isalpha():
            print(f"{i}: {count_l[i]}")
    print("============= END ===============")


if __name__ == '__main__':
    main()
