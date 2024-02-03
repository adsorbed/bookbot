def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = len(file_contents.split())
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char_counts = {char:0 for char in alphabet}
    for char in file_contents:
        if char.lower() in char_counts:
            char_counts[char.lower()] += 1
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(num_words, "words found in the document")
    char_tuples = [(char_counts[char], char) for char in char_counts.keys()]
    
    char_tuples_sorted = sorted(char_tuples, reverse=True)
    for tup in char_tuples_sorted:
        print(f"The '{tup[1]}' character was found {tup[0]} times")

    print("--- End report ---")

main()