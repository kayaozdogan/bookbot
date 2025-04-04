from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()



        return file_contents


def main():
        book_text = get_book_text("/home/kaya/workspace/github.com/kayaozdogan/bookbot/books/frankenstein.txt")
        i = get_num_words(book_text)
        print(f"{i} words found in the document")
        

main()