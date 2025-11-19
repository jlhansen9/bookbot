def wordCount(book_string):
    book_words = book_string.split()
    return len(book_words)

def characterCount(book_string):
    lower_string = book_string.lower()
    character_tally = [{"char":"a","num":0}]

    # Loop through each character from string
    for i in lower_string:
        if not i.isalpha():
            continue
        
        found = False

        # check if character is currently in list
        for j in character_tally:
            if i == j["char"]:
                j["num"]+=1
                found = True

        if not found:
            character_tally.append({"char": i, "num": 1})

    return character_tally

def sort_on(items):
    return items["num"]

def sort_num(char_dict):
    char_dict.sort(reverse=True, key=sort_on)
    return char_dict