from stats import get_num_words, get_num_chars, get_report_stats
import sys

def get_book_text(path):
    with open(path) as f:
        r = f.read()
    
    return r

def main():
    if 2 != len(sys.argv):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text_link = sys.argv[1]
    text_content = get_book_text(text_link)
    num_words = get_num_words(text_content)
    num_chars = get_num_chars(text_content)
    sorted_chars = get_report_stats(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text_link}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()