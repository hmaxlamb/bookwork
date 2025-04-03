def main():
    sentence = "the quick brown box jumps over a lazy dog"
    char = find_missing_letter(sentence)
    print(char)

def find_missing_letter(statement: str):
    alp = ["a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","q",
           "r","s","t","u","v","w","x","y","z"]
    
    index = {}

    for letter in statement:
        index[letter] = True

    for letter in alp:
        if index.get(letter) == None:
            return letter





main()