class Parachute:
    def __init__(self):        
        self._counter = 0
        self._parachute = ['  ___ ',
                          ' /___\\',
                          ' \\   /',
                          '  \\ /',
                          '   0',
                          '  /|\\',
                          '  / \\'
                          ]
        
    # Delete first line of the parachute
    def delete_line(self):
        self._parachute.pop(0)
        self._counter += 1
        if self._counter == 4:
            self._parachute[0] = self._parachute[0].replace('0', 'x')
       
    def get_hint(self):
        hint = ''
        if  self._counter > 0 and self._counter < 2: 
            hint = 'Ups! It looks like your parachute is in trouble!'
        elif self._counter > 1 and self._counter < 3:
            hint = 'You are losing your parachute! Try again!'
        elif  self._counter > 2 and self._counter < 4: 
            hint = 'Be carefull jumper, you can lose your parachute!' 
        elif  self._counter == 4: 
            hint = 'No parachute. You lose!'  
        return hint
    
    def lost_parachute(self):
        return self._counter == 4 
    
    # Print parachute
    def display(self):
        for i in self._parachute:
            print(i)
        print('^^^^^^^')
    
    def is_alive(self):
        return self._alive