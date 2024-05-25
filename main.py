def main():
    with open("books/frankenstein.txt") as file:
        text = file.read()
        letters = letter_stats(text)
        sorted = sort_dict(letters)

        print("--- Begin report of books/frankenstein.txt ---")
        print()
        print(f"{number_of_words(text)} words found in the document")
        for stat in sorted:
            print(
                f"Character '{stat["letter"]}' appeared {stat["value"]} times."
            )
        print()
        print("--- End report ---")


def number_of_words(text):
    words = text.split()
    return len(words)


def letter_stats(text: str):
    stats = dict()
    for letter in text.lower():
        if letter == " " or letter == "\n":
            continue
        curr = stats.get(letter, 0)
        stats.update({letter: curr + 1})
    return stats



def sort_dict(dict: dict):
    def sort_on(dict):
        return dict["value"]
    array = []
    for letter in dict.keys():
        array.append({"letter": letter, "value": dict[letter]})

    array.sort(reverse=True, key=sort_on)

    return array


main()
