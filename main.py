import sys
from stats import get_num_words
from stats import character_count
from stats import reverse_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def make_report(dictio):
    report = []
    for char, count in dictio.items():
        if char.isalpha():
            report.append({"char": char, "num": count})
    return report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words")

    char_counts = character_count(book_text)
    report = make_report(char_counts)
    sorted_report = reverse_dict(report)

    for entry in sorted_report:
        print(f"{entry['char']}: {entry['num']}")

main()
