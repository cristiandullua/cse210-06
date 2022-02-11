from email import message


class Parachute:
    def __init__(self):
        
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
     

    # Print parachute
    def display(self):
        print()
        for i in self._parachute:
            print(i)
        print('^^^^^^^')