def count_words(text):
    new_list = []
    splitted = text.split()
    new_list.append(splitted)
    count = len(splitted)
    return count

def character_count(text):
    count = {}
    lowered = text.lower()
    for character in lowered:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    return count


def sort_on(items):
    return items["num"]

def sorted_list(dictionary):
    list = []
    for key in dictionary:
        num = dictionary[key]
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = num
        list.append(new_dict)
    list.sort(reverse=True, key=sort_on)
    return list







