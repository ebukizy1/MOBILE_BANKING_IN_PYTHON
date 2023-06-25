class wrong_pin_exception(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.custom_message = message

    def __int__(self):
        return f"Wrong pin exception: {self.custom_message}"
