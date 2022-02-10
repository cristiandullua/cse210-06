import random

class SecretWord:
    def __init__(self):
        self._word_list=['david','ernesto','benjamin','samuel','gerardo']
        self._word=''
        self._guess=''

        # Choose SecretWord from word list
        self._word_picker()
        # Create blank spaces
        self._create_guess()

    #Retorna una palabra de la lista    
    def _word_picker(self):
        self._word=random.choice(self._word_list)

    def _create_guess(self):
        for i in self._word:
            self._guess+='_'
    
    def display_guess(self):
        print(*self._guess)

    def check_word_guess(self):
        if self._word == self._guess:
            return True
    
    def new_letter_guessed(self, letter):
        # Create list with positions of the letters if found
        letterPositions=[pos for pos, char in enumerate(self._word) if char == letter]
        
        print(letterPositions)
        # If list is not empty means there are letters to reveal
        if letterPositions:
            temp = list(self._guess)
            res = [letter if idx in letterPositions else ele for idx, ele in enumerate(temp)]
            self._guess = ''.join(res)
            
            return True
        else:
            return False    