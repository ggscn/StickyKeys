import ctypes
from nltk.tokenize import word_tokenize
from random import choice
import nltk

@dataclass
class Keyboard:
    layout: list = [
        '1234567890',
        'qwertyuiop',
        'asdfghjkl',
        'zxcvbnm'
    ]


class TypoText:
    def __init__(self, text: str):
        self.text = text
        self.max_swap_distance = 3
        self.tokens = self.tokenize(text)

    def tokenize(self, text: str) -> list:
        tokens = word_tokenize(text)
        return tokens
    
    def mispress(self, char: str):
        keyboard_layout = Keyboard.layout
        char_row_index = [i for i,x in enumerate(
            keyboard_layout) if char in x][0]
        char_inner_row_index = keyboard_layout[
            char_row_index].index(char)
        
        

    def swap_keys(self, token: str):
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

    def process(self):
        token = self.swap_keys(self.tokens[3])
        self.tokens[3] = token
        print(' '.join(self.tokens))

TypoText('This is a sentence').process()
