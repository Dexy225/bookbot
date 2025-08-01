def get_word_count(text):
    num_words = 0
    file_contents = text

    split_words=file_contents.split()    
    num_words=len(split_words)

    return num_words


def get_char_count(text):
    lowerd = text.lower()

    count = {}

    for char in lowerd:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count

def sort_on(count):
    return count["num"]

def sort_data(count):
    lst = []
    for char, num in count.items():
        if char.isalpha() == True:
            lst.append({"char": char, "num": num})

    lst.sort(reverse = True, key=sort_on)

    return lst
    
