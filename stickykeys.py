import ctypes
from nltk.tokenize import word_tokenize
from random import choice
import nltk

class TypoText:
    def __init__(self, text: str):
        self.text = text
        self.max_swap_distance = 3
        self.tokens = self.tokenize(text)

    def tokenize(self, text):
        tokens = word_tokenize(text)
        return tokens
    
    def get_keyboard_layout(self: str):
        pass

    def swap_keys(self, token):
        max_distance = self.max_swap_distance
        token_range = list(range(len(token)))
        swap_source_index = choice(token_range)
        swap_target_index = choice(list(range(max_distance)))+swap_source_index
        if swap_target_index > len(token) - 1:
            swap_target_index = len(token) - 1

        swap_indices = [
            swap_source_index,
            swap_target_index
        ]

        token_range[swap_indices[1]], token_range[swap_indices[0]] = (
            token_range[swap_indices[0]], token_range[swap_indices[1]])
        token = ''.join(
            [token[x] for x in token_range])
        
        return token

    def run(self):
        token = self.swap_keys(self.tokens[3])
        self.tokens[3] = token
        print(' '.join(self.tokens))

TypoText('This is a sentence').run()
