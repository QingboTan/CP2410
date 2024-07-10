# import string
# # A sample string
# s = "Hello, World! How are you doing?"
# # Remove punctuation from the string
# s = ''.join(ch for ch in s if ch not in string.punctuation)
# print(s) # Output: "Hello World How are you doing"
import string


def count_words(file_path):
    # Initialize an empty dictionary to store word frequencies
    word_frequency = {}

    # Open the file and read line by line
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            # Remove leading and trailing punctuation and convert to lowercase
            line = ''.join(ch for ch in line if ch not in string.punctuation)
            line = line.lower()

            # Split the line into words and count frequencies
            words = line.split()
            for word in words:
                word = word.strip(string.punctuation)

                if word in word_frequency:
                    word_frequency[word] += 1
                else:
                    word_frequency[word] = 1
    return word_frequency


# Example usage:
print(count_words('countword.txt'))
