
def main():
    #print("hello world")
    path_to_file = "books/frankenstein.txt"
    dico = {}

    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)
        word_count = len(file_contents.split())
        print(word_count)
        for char in file_contents:
            key = char.lower()
            if key in dico:
                dico[char.lower()]+=1
            else:
                dico[char.lower()] = 1

        print(dico)
main()