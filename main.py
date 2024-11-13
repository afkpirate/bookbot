def character_count(file_contents):
    lower_string = file_contents.lower()
    dictionary = {}
    for char in lower_string:
        dictionary[char] = dictionary.get(char, 0) + 1
    return dictionary

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print("- Begin Report -")
        print (f"This copy of Frankenstein contains {word_count} words.")

        chars = character_count(file_contents)
        for char, count in sorted(chars.items(), key=lambda x: x[1], reverse=True):
            if char.isalpha():
                print(f"The '{char}' character was found {count} times.")
        print("- End Report -")

main()