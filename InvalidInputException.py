class InvalidInputException(Exception):
    def __init__(self, input):
        super().__init__()
        self.input = input

