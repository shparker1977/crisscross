class Cell:

    def __init__(self, isBlank=True, value=None, display=None):
        self.isBlank = isBlank
        self.value = value
        self.display = display

    def set_display(self, letter):
        if self.isBlank == False:
            if (isinstance(letter, str)) and (len(letter) == 1) and (letter.isalpha()):
                self.display = letter.upper()

    def check_value(self):
        if self.value == self.display:
            return True
        return False