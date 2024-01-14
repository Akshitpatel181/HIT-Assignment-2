# This program finds the top 30 most common words and their count in csv_text.txt and store into a csv file. 

import csv

def remove_nonwords(words):
    """Removes nonwords from list `words`"""
    nonwords = ["", ".", ",", "!", "?", ";", ":", "-", "_", "(", ")", "[", "]", "{", "}", "\"", "'"]
    new_list = []
    for word in words:
        if word not in nonwords:
            new_list.append(word)
    return new_list

def count_occurrences(text):
    """Returns dictionary that counts occurrences of each word in argument string `text`"""
    # Preprocessing
    text = text.lower()
    text = text.strip()  # remove excess newlines
    words = text.split()  # split into list of words
    words = remove_nonwords(words)

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

with open('csv_text.txt', 'r') as file1:
    long_string = file1.read()

word_counts = count_occurrences(long_string)
top_words = sorted(word_counts, key=word_counts.get, reverse=True)[:30]

with open('words_counts.csv', 'w', newline='') as file2:
    writer = csv.writer(file2)
    for word in top_words:
        writer.writerow([word, word_counts[word]])
