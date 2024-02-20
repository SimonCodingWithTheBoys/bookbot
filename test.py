def main():
    path = "books/frankenstein.txt"
    text_book = get_book_path(path)
    count_of_words = word_count_of_book(text_book)
    dic_of_letters = letter_count_of_book(text_book)
    sorted_dic = sorted_list_of_dic(dic_of_letters)

    print("--- Begin report of Frankenstein ---")
    print(f"{count_of_words} words detected")
    print()
    print()
    for item in sorted_dic:
        if not item["char"].isalpha():
            continue
        print(f"The {item["char"]} character appears {item['num']} times")

    print()
    print()

    print("--- End report of report ---")


def get_book_path(path):
    with open(path) as f:
        return f.read()


def word_count_of_book(book):
    splitted_word_list = book.split()
    return len(splitted_word_list)


def letter_count_of_book(book):
    dic_with_letters = {}
    for letter in book:
        lowered = letter.lower()
        if lowered not in dic_with_letters:
            dic_with_letters[lowered] = 1
        else:
            dic_with_letters[lowered] += 1
    return dic_with_letters


def sort_on(dic_with_letters):
    return dic_with_letters["num"]

def sorted_list_of_dic(dic_with_letters):
    sorted_list_dic_with_letters = []
    for ch in dic_with_letters:
        sorted_list_dic_with_letters.append({"char": ch, "num": dic_with_letters[ch]})

    sorted_list_dic_with_letters.sort(key=sort_on, reverse=True)
    return sorted_list_dic_with_letters


main()