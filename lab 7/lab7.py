#Task 1
file = open('text1.txt','r', encoding='utf-8')
for row in file:
        print(row)

#Task 2
import random
print('Task 2')
file_path = 'text1.txt'  

with open('text1.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    random_line = random.choice(lines)
    print(random_line)

file.close()

#Task 3
print('Task 3')
def count_uppercase_chars(file_path):
    try:
        file = open(file_path, 'r', encoding='utf-8')
        content = file.read()
        file.close()

        uppercase_count = sum(1 for char in content if char.isupper())
        return uppercase_count
    except FileNotFoundError:
        return -1  
  

uppercase_count = count_uppercase_chars(file_path)
if uppercase_count != -1:
    print(f"The number of uppercase characters in the file is: {uppercase_count}")
else:
    print("File not found. Please check the file path.")

#Task 4
print('Task 4')
def count_lines_not_starting_with_D(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            count = sum(1 for line in lines if not line.startswith('D'))
            return count
    except FileNotFoundError:
        return -1  


line_count = count_lines_not_starting_with_D(file_path)
if line_count != -1:
    print(f"The number of lines not starting with 'D' is: {line_count}")
else:
    print("File not found. Please check the file path.")

#Task 5
def count_words_ending_with_F(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            count = sum(1 for word in words if word.endswith(('F', 'f')))
            return count
    except FileNotFoundError:
        return -1  

word_count = count_words_ending_with_F(file_path)
if word_count != -1:
    print(f"The number of words ending with 'F' or 'f' is: {word_count}")
else:
    print("File not found. Please check the file path.")

#Task 6
print('Task 6')
def count_specific_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            count_all = words.count("all")
            count_none = words.count("none")
            return count_all, count_none
    except FileNotFoundError:
        return -1, -1  
    

all_count, none_count = count_specific_words(file_path)
if all_count != -1 and none_count != -1:
    print(f"Occurrences of 'all': {all_count}")
    print(f"Occurrences of 'none': {none_count}")
else:
    print("File not found. Please check the file path.")

#Task 7
print('Task 7')
from collections import Counter

def count_word_frequency(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            word_freq = Counter(words)
            return word_freq
    except FileNotFoundError:
        return None  

word_frequency = count_word_frequency(file_path)
if word_frequency is not None:
    print("Word frequency in the file:")
    for word, freq in word_frequency.items():
        print(f"{word}: {freq}")
else:
    print("File not found. Please check the file path.")

#Task 8
print('Task 8')
def longest_word_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().split()
        longest_word = max(content, key=len)
        return longest_word

longest_word = longest_word_in_file(file_path)
print(f"The longest word in the file is: {longest_word}")

#Task 9
print('Task 9')
def correct_chars_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().replace('B', 'J').replace('b', 'j')
        return content

corrected_content = correct_chars_in_file(file_path)
print("Corrected content:")
print(corrected_content)

#Task 10
print('Task 10')
def count_a_b_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()
        count_a = content.count('а')
        count_b = content.count('б')
        return count_a, count_b

count_a, count_b = count_a_b_in_file(file_path)
print(f"Occurrences of A: {count_a}, Occurrences of B: {count_b}")
