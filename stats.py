def get_num_words(text):
    text = text.split()
     
    i = 0
    for word in text:
        i += 1


    return i


def character_count(c_text):

    dictio = {}
    for char in c_text:
        char = char.lower()
        if char in dictio:
            dictio[char] += 1
        else:
            dictio[char] = 1
    return dictio

def sort_on(dictionary):
    return dictionary["num"]

def reverse_dict(dict):
    dict.sort(reverse=True, key=sort_on)
    return dict