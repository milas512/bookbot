def count_words(file_contents):
    word_list = file_contents.split()
    return f"Found {len(word_list)} total words"


def get_num_characters(file_contents):
    character_count = {}
    for char in file_contents:
        if char.lower() not in character_count:
            character_count[char.lower()] = 1
        else:
            character_count[char.lower()] += 1
    return character_count


def list_of_dictionaries(character_count):
    new_list = []
    for key in character_count:
        if key.isalpha():
            new_dict = {"char": key, "num": character_count[key]}
            new_list.append(new_dict)
    return new_list


def sort_on(items):
    return items["num"]


def sort_list_of_dicts(list):
    big_string = ""
    for i in list:
        for key in i:
            if key == "char":
                big_string += (str(i["char"]) + ":")
            elif key == "num":
                big_string += (" " + str(i["num"]) + "\n")
    return big_string
