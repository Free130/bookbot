
def print_intro(count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n")

def print_dico(dico):
    for char in dico:
        print(f"'{char}' character was found {dico[char]} times")

def main():
    path_to_file = "books/frankenstein.txt"
    dico = {}

    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)
        word_count = len(file_contents.split())
        print_intro(word_count)

        for char in file_contents:
            key = char.lower()
            if key.isalpha():
                if key in dico:
                    dico[char.lower()]+=1
                else:
                    dico[char.lower()] = 1


        print_dico(dico)
main()