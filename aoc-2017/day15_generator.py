class Generator():
    def __init__(self, current, factor, modulus=2147483647):
        self._current = current
        self._factor = factor
        self._modulus = modulus

    def generate(self):
        self._current = (self._current * self._factor) % self._modulus
        return self._current


class GeneratorB():
    def __init__(self, current, factor, multiple, modulus=2147483647):
        self._current = current
        self._factor = factor
        self._modulus = modulus
        self._multiple = multiple

    def generate(self):
        found = False
        while not found:
            self._current = (self._current * self._factor) % self._modulus
            found = (self._current % self._multiple) == 0
        return self._current
