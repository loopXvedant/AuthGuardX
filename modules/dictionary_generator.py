# Dictionary Generator Module
# This module creates custom wordlists for password testing

import os

def run_dictionary_generator():
    print("\n--- Dictionary Generator ---")

    base_word = input("Enter a base word (e.g. name): ")
    include_numbers = input("Include numbers? (y/n): ").lower()
    include_symbols = input("Include symbols? (y/n): ").lower()

    wordlist = []

    # Basic variations
    wordlist.append(base_word)
    wordlist.append(base_word.lower())
    wordlist.append(base_word.upper())
    wordlist.append(base_word.capitalize())

    # If user wants numbers
    if include_numbers == "y":
        for i in range(0, 100):
            wordlist.append(base_word + str(i))

    # If user wants symbols
    if include_symbols == "y":
        symbols = ["!", "@", "#", "$"]
        for sym in symbols:
            wordlist.append(base_word + sym)

    # Save to file
    output_dir = "output/wordlists"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{output_dir}/{base_word}_wordlist.txt"

    with open(filename, "w") as f:
        for word in wordlist:
            f.write(word + "\n")

    print(f"\nWordlist generated successfully!")
    print(f"Saved at: {filename}")
    print(f"Total words: {len(wordlist)}")

