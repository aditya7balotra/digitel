from wire import Wire

class Demultiplexer:
    def __init__(self, n):
        self.n = n
        self._input = Wire(0)
        self._outputs = [Wire(0) for _ in range(2**n)]
        self._select_line = 0

    @property
    def select_line(self):
        return self._select_line
    
    @select_line.setter
    def select_line(self, value):
        if value < 0 or value >= 2**self.n:
            raise ValueError(f"Select line value must be between 0 and {2**self.n - 1}")
        self._select_line = value

    def output(self):
        for i in range(2**self.n):
            self._outputs[i].state = self._input.state if i == self._select_line else 0
        return self._outputs
    
    @property
    def input(self):
        return self._input
    
    @input.setter
    def input(self, bit):
        self._input.state = bit

if __name__ == "__main__":
    dmux = Demultiplexer(1)
    dmux.input = 1
    dmux.select_line = 0
    outputs = dmux.output()
    print(outputs[0].state)  # Output: 1
    print(outputs[1].state)  # Output: 0
    dmux.input = 1
    dmux.select_line = 1
    outputs = dmux.output()
    print(outputs[0].state)  # Output: 0
    print(outputs[1].state)  # Output: 1