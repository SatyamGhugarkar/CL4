# Develop Mapreduce program to calculate the freq of a given word in a file
# for output input the file name/path eg. C:\Users\Omkar\Documents\ME\CL4\Prac2\test.txt
import re
from multiprocessing import Pool

WORD_RE = re.compile(r"[\w']+")

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def mapper(line):
    word_count = {}
    for word in WORD_RE.findall(line):
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def reducer(mapped_counts):
    reduced_counts = {}
    for word_count in mapped_counts:
        for word, count in word_count.items():
            reduced_counts[word] = reduced_counts.get(word, 0) + count
    return reduced_counts

def main(filename, target_word):
    lines = read_file(filename)
    with Pool() as pool:
        mapped_counts = pool.map(mapper, lines)
    reduced_counts = reducer(mapped_counts)

    # Get the frequency of the target word
    target_frequency = reduced_counts.get(target_word.lower(), 0)
    print(f"The frequency of '{target_word}' in the file is: {target_frequency}")

if __name__ == "__main__":
    filename = input("Enter the file name: ")
    target_word = input("Enter the word to find frequency: ")
    main(filename, target_word)
