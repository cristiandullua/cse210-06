from email import message

class Parachute:
    def __init__(self):
        self._counter = 0
        self._parachute = [' ___ ',
                          '/___\\',
                          '\\   /',
                          ' \\ /',
                          '  0',
                          ' /|\\',
                          ' / \\'
                          ]
        
    # Delete first line of the parachute
    def delete_line(self):
        self._parachute.pop(0)
        self._counter += 1
    
    def get_hint(self):
        hint = " "
        if  self._counter > 0 and self._counter < 2: 
            hint = "Ups! I looks like your parachute is in trouble!"
        elif  self._counter > 2 and self._counter < 4: 
            hint = "Be carefull jumper, you can lose your parachute!" 
        elif  self._counter == 4: 
            hint = "No parachute. You lose!"
        return hint  
                           
    def lost_parachute(self):
        return self._counter == 5 
    
    # Print parachute
    def display(self):
        print()
        for i in self._parachute:
            print(i)
        print('^^^^^^^')