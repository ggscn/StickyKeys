import ctypes
from nltk.tokenize import word_tokenize
from random import choice
import nltk
import time
import random
import operator

class Keyboard:
    layout = [
        '1234567890',
        'qwertyuiop',
        'asdfghjkl',
        'zxcvbnm'
    ]


class TypoText:
    def __init__(self, text: str, num_typos: int = 1):
        self.text = text
        self.max_swap_distance = 3
        self.tokens = self.tokenize(text)

    def tokenize(self, text: str) -> list:
        tokens = word_tokenize(text)
        return tokens

    def get_random_list_index(self, target_list, target_index):
        operators = ['add', 'sub']
        operation = getattr(
            operator, operators[list(self.generate_random_number())[0]])
        delta = list(self.generate_random_number())[0]
        index = operation(
            target_index, delta)
        clipped_index = max(min(
            index, len(target_list)-1), 0)
        return clipped_index
    
    def mispress_keys(self, token: str):
        token_range = list(range(len(token)))
        char_index = choice(token_range)
        token_list = list(token)
        char = token[char_index]

        keyboard_layout = Keyboard.layout
        char_row_index = [i for i,x in enumerate(
            keyboard_layout) if char in x][0]
        char_inner_row_index = keyboard_layout[
            char_row_index].index(char)

        press_row_index = self.get_random_list_index(
            keyboard_layout, char_row_index)
        press_row_key_index = self.get_random_list_index(
            keyboard_layout[press_row_index], char_inner_row_index)
        pressed_key = keyboard_layout[
            press_row_index][press_row_key_index]
        token_list[char_index] = pressed_key
        return ''.join(
            [token_list[i] for i in token_range])

    def swap_keys(self, token: str):
        max_distance = self.max_swap_distance
        token_range = list(range(len(token)))
        swap_source_index = choice(token_range)
        swap_target_index = choice(list(range(max_distance))) + swap_source_index
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

    def generate_random_number(self, num_digits=1):
        """Raise current timestamp to the power 2 and return if number is even 
        or odd. Continue for num_digits"""
        for i in range(0, num_digits):
            timestamp = time.time()
            num = timestamp ** 2
            yield num % 2 == 0

    def process(self):

        methods = ['swap_keys', 'mispress_keys']
        """token = self.swap_keys(self.tokens[3])
        self.tokens[3] = token
        print(' '.join(self.tokens))
        self.mispress"""
        token = self.mispress_keys(self.tokens[3])
        self.tokens[3] = token
        print(' '.join(self.tokens))

TypoText('This is a sentence').process()
