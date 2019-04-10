# Weird Text
WeirdText encodes and decodes words. Encoded message can be read quite simply by a human. But Machines may find it difficult to read this message (to decode it). 
## Encoding
For each original word in the original text, the first and last character stay in the same position, but all the characters in the middle of the word are shuffled (permutated).
## Decoding
From the encoded the words list are used to decode the text. Decoded output should, as far as possible, be identical to the original text.


Application created for recruitment purposes, used for encoding and decoding text in the Weird Text standard. It was written using Python 3.7 and is compatible with 3.6.

Testing: python -m unittest.

URL: https://weirdtext.herokuapp.com

To use the online api send a POST request to one of the endpoints with text included as data in the request body. 

# Example usage:

/encode

```
"This is a long looong test sentence
with some big (biiiiig) words\!"


---weird---
Tihs is a lnog lonoog tset sctnneee
wtih smoe big (biiiiig) wodrs!
---weird---
long looong sentence some test This with words

/decode

---weird---
Tihs is a lnog lonoog tset sctnneee
wtih smoe big (biiiiig) wodrs!
---weird---
long looong sentence some test This with words"

This is a long looong test sentence
with some big (biiiiig) words!
```
# What to install 

1. Install Python 
2. Fork or clone this repository
``` 
    git clone
```

3. Install and activate virtualenv: 

```
    virtualenv -p python3 virtenvdjango
    source venv/bin/activate
```

4. Install 
``` 
pip install -r requirements.txt
```

# 

