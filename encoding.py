import random
import re


def shuffle_string(string):
    # This function shuffles a string
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)


def garble_word(word):
    # This function connects original first and last letters with
    # shuffled midst.
    # No operation needed on sufficiently small words
    # (Also, main algorithm requires word length >= 2).
    if len(word) <= 3:
        return word
    # Split word into first & last letter, and middle letters
    first, mid, last = word[0], word[1:-1], word[-1]
    return first + shuffle_string(mid) + last


def garble(sentence):
    # This function return encoded text.
    # The SEPARATROR is separating the original text from encoded text.
    SEPARATOR = "\n-weird-\n"
    # Find all words consist of more than 3 letters and put it into list
    # named "words".
    tokenize_re = re.compile(r'(\w\w\w+)', re.U)
    words = tokenize_re.findall(sentence)
    # Letters in "word" can't be the same, example: "biiiiig"
    words = [word for word in words if (word[1:-1])[1:] != (word[1:-1])[:-1]]
    # Sort words in the "words" list alphabetically
    words_sorted = sorted(words, key=str.lower)
    # Encode items in "words" using  function garble_word(word)
    encoded_part_of_words = [garble_word(word) for word in words if word]
    # If item is the same as before, use "garble_word(word)" again,
    # else replace item in "words" with exact item in "encoded_part_of_words".
    # Replace word containing encoded content with original word in original
    # sentence.
    for i in range(0, len(words)):
        while words[i] == encoded_part_of_words[i]:
            encoded_part_of_words[i] = garble_word(words[i])
        sentence = re.sub(words[i], encoded_part_of_words[i], sentence)
    # Exchange a list "words_sorted" into string and return it.
    words_sorted = ' '.join(words_sorted)
    encoded_text = SEPARATOR + sentence + SEPARATOR + words_sorted
    return encoded_text


text = "'This is a long looong test sentence,\n' 'with some big " \
       "(biiiiig) words!'"
print(garble(text))


def decode(encoded):
    # This function return decoded text.
    # Find text to decode (between two separators: '-weird-').
    start_point = encoded.find('-weird-')+9
    end_point = encoded.rfind('-weird-')-2
    decoding = encoded[start_point:end_point]
    # Find all items consist of 4 or more letters and put it into list
    # named "decoding_list".
    tokenize_re = re.compile(r'(\w\w\w\w+)', re.U)
    decoding_list = tokenize_re.findall(decoding)
    # Find start of original words (arranged alphabetically).
    original_words = encoded[(encoded.rfind('-weird-')+9)::]
    # Find all items in original_words and put it into list named
    # "original_words".
    original_words = tokenize_re.findall(original_words)
    # In decoding_list exchange encoded word with decoded.
    for b in decoding_list:
        for a in original_words:
            if a[0] == b[0] and a[-1] == b[-1] and len(a) == len(b):
                decoding = re.sub(b, a, decoding)
    return decoding


encoded = "'\n-weird-\n' 'Tihs is a lnog loonog tset sntceene,\n' " \
          "'wtih smoe big (biiiiig) wdros!' " \
          "'\n-weird-\n' 'long looong sentence some test This with words'"
print(decode(encoded))
