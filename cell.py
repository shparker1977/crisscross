class Cell:

    def __init__(self, is_blank=False, value=' ', display=' '):
        self.is_blank = is_blank
        if self.is_blank:
            self.value = '-'
        else:
            self.value = value
        self.display = display

    def __str__(self):
        return self.value

    def set_display(self, letter):
        if self.is_blank == False:
            if (isinstance(letter, str)) and (len(letter) == 1) and (letter.isalpha()):
                self.display = letter.upper()

    def check_value(self):
        return self.value == self.display