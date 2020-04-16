class TerminalException(Exception):
    """
    Raised when top of stack is terminal and not equal to value at ip
    """
    def __init__(self, arg):
        self.arg = arg

class RuleNotFoundException(Exception):
    """
    Raised when top of stack is terminal and not equal to value at ip
    """
    def __init__(self, arg):
        self.arg = arg