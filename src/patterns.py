
char_dict = {"S": "Soft", "T": "Tough"}
valid_chars = set(char_dict.keys())


class OperationOrderError (Exception):
    pass

class PatternConverter:

    def __init__(self, pattern: str, validate = True):
        self.pattern = pattern
        self.__is_pattern_valid = False
        self.__pattern_len = 0
        if validate:
            self.validate_pattern()

    def validate_pattern(self):

        if not isinstance(self.pattern, str):
            raise TypeError("Pattern is not a string")

        if len(self.pattern) == 0:
            raise ValueError("Pattern can not be empty")

        for ch in self.pattern:
            if ch not in valid_chars:
                raise ValueError(f'Pattern contains invalid Character: "{ch}"')
        
        self.__is_pattern_valid = True
        self.__pattern_len = len(self.pattern)
 
    def convert_pattern(self, n: int):
        if not self.__is_pattern_valid:
            raise OperationOrderError("Please validate the pattern first")
        if n <= 0:
            raise ValueError(f"N can not be zero or negative: {n}")
        if n == 1:
            return f'{char_dict[self.pattern[0]]}.'

        part1 = ', '.join((char_dict[self.pattern[i%self.__pattern_len]] for i in range(n-1)))
        part2 = f'{char_dict[self.pattern[(n-1)%self.__pattern_len]]}.'
        return ' and '.join ([part1, part2])