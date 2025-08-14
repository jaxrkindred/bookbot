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

def sorted_list(dictionary):
    


