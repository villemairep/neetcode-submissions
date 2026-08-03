from typing import List

def count_unique_words(words: List[str]) -> int:
    pass
    length = len(words)
    my_list = set(words)
    dupe = 0

    for i in my_list:
        word = i
        if word in my_list:
            dupe += 1


    return dupe



# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
