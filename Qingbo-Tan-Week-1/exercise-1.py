def count_occurrences(word_list, target_word):
    count = 0
    for word in word_list:
        if word == target_word:
            count += 1
    return count
    """
    This function counts the number of times a word appears in a list :param word_list:
    :param target_word:
    :return:
    """

word_list = ["the", "cat", "sat", "on", "the", "mat"]
target_word = "the"
print(count_occurrences(word_list, target_word)) # output: 2
target_word = "cat"
print(count_occurrences(word_list, target_word)) # output: 1
word_list = ["the", "cat", "sat", "on", "the", "mat"]
target_word = "dog"
print(count_occurrences(word_list, target_word)) # output: 0
