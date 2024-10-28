def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters

def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")


def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")

from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

# count unique words:EX
def count_unique_words(content):
    words = set(content.lower().split())
    unique_words = set(words)
    return len(unique_words)

# Find the longest word
def longest_word(content):
    words = content.split()
    longest = max(words, key=len)
    return longest, len(longest)

# Count Occurances of specific word
def count_specific_word(content, target_word):
    words = content.lower().split()
    target_word = target_word.lower()
    return words. count(target_word)

#Percentage of words longer than Average word length
def Percentage_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word)> avg_length]
    percentage = (len(longer_words) / len(words)) * 100
    return percentage

#Main Function to combine Everything
def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    unique_words_count = count_unique_words(content)
    longest, length = longest_word(content)
    specific_word = "the"  # Example word to count
    specific_word_count = count_specific_word(content, specific_word)
    percentage_above_avg = Percentage_longer_than_average(content)


    
# Display the results
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Number of unique words: {unique_words_count} ")
    print(f"Longest word:'{longest}'(length:{length}characters)")
    print(f"The word '{specific_word}' appears {specific_word_count}times")
    print(f"Percentage of words longer than the average word length: {percentage_above_avg:.2f}%")



# Run the analysis

analyze_text('sample.txt')