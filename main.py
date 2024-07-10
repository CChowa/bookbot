def main():
    file_path = "books/frankenstein.txt"
    text = read_text(file_path)
    word_count = count_words(text)   
    char_count = count_chars(text)
    print_report(word_count, char_count, file_path)

def read_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count
        
def count_chars(text):
    char_counts = {}
    input_text = text.lower()
    for char in input_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def print_report(word_count, char_count, file_path):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    converted_dict = convert_dict(char_count)
    converted_dict.sort(reverse=True, key=sort_on)
    for dict in converted_dict:
        if dict["name"].isalpha():
            print(f"The '{dict['name']}' character was found {dict['num']} times")
    print("--- End report ---")

def convert_dict(dict):
    converted_dict = [{"name":key, "num":value} for key, value in dict.items()]
    return converted_dict

def sort_on(dict):
    return dict["num"]

main()