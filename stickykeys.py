import ctypes
from nltk.tokenize import word_tokenize
from random import choice
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
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

    def dekonize(self, tokens: list) -> str:
        dekonized_str = TreebankWordDetokenizer().detokenize(tokens)
        return dekonized_str

    def get_modifiable_tokens(self) -> list:
        return [t for t in self.tokens if t.isalpha()]

    def get_random_nearby_list_item(self, target_list: list, target_index: int) -> int:
        operators = ['add', 'sub']
        operation = getattr(
            operator, self.get_random_list_item(operators))
        delta = list(self.generate_random_number())[0]
        index = operation(
            target_index, delta)
        clipped_index = max(min(
            index, len(target_list)-1), 0)
        return clipped_index

    def generate_random_number(self, num_digits=1):
        """Raise current timestamp to the power 2 and return if number is even 
        or odd. Continue for num_digits"""
        seed = int(time.time())
        m = 253
        for i in range(0, num_digits):
            seed **= 2
            rand_num = seed % m
            yield (rand_num % 2) == 0

    def get_random_list_item(self, target_list: list):
        list_length = len(target_list) - 1
        list_item_index = 0
        for num in self.generate_random_number(list_length):
            print(int(num))
            list_item_index += int(num)
        return target_list[list_item_index]

    def mispress_keys(self, token: str) -> str:
        token_range = list(range(len(token)))
        char_index = choice(token_range)
        token_list = list(token)
        char = token[char_index]

        keyboard_layout = Keyboard.layout
        char_row_index = [i for i, x in enumerate(
            keyboard_layout) if char in x][0]
        char_inner_row_index = keyboard_layout[
            char_row_index].index(char)

        press_row_index = self.get_random_nearby_list_item(
            keyboard_layout, char_row_index)
        press_row_key_index = self.get_random_nearby_list_item(
            keyboard_layout[press_row_index], char_inner_row_index)
        pressed_key = keyboard_layout[
            press_row_index][press_row_key_index]
        token_list[char_index] = pressed_key
        token_str = ''.join(
            [token_list[i] for i in token_range])
        return token_str

    def swap_keys(self, token: str) -> list:
        max_distance = self.max_swap_distance
        token_range = list(range(len(token)))
        swap_source_index = choice(token_range)
        swap_target_index = choice(
            list(range(max_distance))) + swap_source_index
        if swap_target_index > len(token) - 1:
            swap_target_index = len(token) - 1

        swap_indices = [
            swap_source_index,
            swap_target_index
        ]

        token_range[swap_indices[1]], token_range[swap_indices[0]] = (
            token_range[swap_indices[0]], token_range[swap_indices[1]])
        token_str = ''.join(
            [token[x] for x in token_range])

        return token_str

    def process(self, num_typos=1, method=None):
        for i in range(0, num_typos):
            if method is None:
                methods = ['swap_keys', 'mispress_keys']
                method_index = list(self.generate_random_number())[0]
                method = getattr(
                    self, methods[method_index])
            token = self.get_random_list_item(
                self.get_modifiable_tokens())
            typo_token = method(token)
            self.tokens[self.tokens.index(token)] = typo_token
        return self.dekonize(self.tokens)