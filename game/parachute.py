class Parachute:
    def __init__(self):
        self._alive = True
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

    # Print parachute
    def display(self):
        for i in self._parachute:
            print(i)
        print('^^^^^^^')

    # Is this the last opportunity?
    def is_the_head(self):
        return '0' in self._parachute[0]

    # Kill parachute man
    def kill(self):
        self._alive = False
        self._parachute[0] = self._parachute[0].replace('0', 'x')

    def is_alive(self):
        return self._alive