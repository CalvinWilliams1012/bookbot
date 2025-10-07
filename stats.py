def count_book_words(text):
    return len(text.split())

def character_count(text):
    character_count_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in character_count_dict:
                character_count_dict[char] += 1
            else:
                character_count_dict[char] = 1
    return character_count_dict

def sort_on(character_count_dict):
    return character_count_dict["num"]

def sort_character_count(character_count_dict):
    return dict(sorted(character_count_dict.items(), key=lambda item: item[1], reverse=True))