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

def sort_on(character_num_dict):
    return character_num_dict["num"]

def sort_character_count(character_count_dict):
    sorted_characters = []
    for char in character_count_dict:
        count = character_count_dict[char]
        sorted_characters.append({"char": char, "num": count})
    sorted_characters.sort(key=sort_on, reverse=True)
    return sorted_characters