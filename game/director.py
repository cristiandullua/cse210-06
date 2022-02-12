from game.parachute import Parachute
from game.secret_word import SecretWord
from game.terminal_service import TerminalService

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        # !!!ADD ATTRIBUTES HERE
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._isPlaying = True   

        self._terminalService = TerminalService()
        self._secretWord = SecretWord()
        self._parachute = Parachute()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._isPlaying:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
  
    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
       
        # Display the blanks and guessed letters / adding spacing between characters
        self._terminalService.write_text(" ".join(self._secretWord.display_guess()))
        print()

        # Display the current state of the parachute
        self._parachute.display()
        

    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """

        hint = self._parachute.get_hint()        
        letterGuess = self._terminalService.read_text("Guess a letter [a-z]: ")
        
        if self._secretWord.new_letter_guessed(letterGuess)  ==  False:
            self._parachute.delete_line()
        
        self._terminalService.write_text(hint)  

        
            
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """

        if self._secretWord.check_word_guess() or self._parachute.lost_parachute():
            self._isPlaying = False
            print()
            print('Game is Over. Well played!')