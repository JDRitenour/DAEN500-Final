class reviseString:
    def __init__(self):
        self.user_input = ''
    
    def getString(self):
        self.user_input = input('Insert String: ')
        
    def printString(self):
        print(self.user_input.upper())

user_string = reviseString()
user_string.getString()
user_string.printString()
