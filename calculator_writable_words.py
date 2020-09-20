from requests import get
from string import ascii_letters

def get_weird_words():
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    words_list = get(url).text.split('\r\n')
    return words_list

def get_unix_words():
    url = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
    ascii_letters_set = set(ascii_letters)
    words_list = [i for i in get(url).text.split('\n') if
                  ascii_letters_set.union(i) == ascii_letters_set]
    return words_list

def get_all_words():
    return sorted(list(set(get_weird_words()).union(get_unix_words())))

words_list = get_unix_words()
words_type = 'unix'

letters = dict(zip('oiehsglb', '01345678'))
letters_set = set(letters.keys())

max_length = 8

possible_words = dict()

for word in words_list:
    if (len(word) <= max_length and
       letters_set.union(word) == letters_set):
        possible_words[word] = ''.join(reversed([letters[i] for i in word]))

output = '\n'.join([f'{i} - {possible_words[i]}' for i in possible_words])

print(output)
with open(f'{words_type}_words.txt', 'w') as file:
    file.write(output)
