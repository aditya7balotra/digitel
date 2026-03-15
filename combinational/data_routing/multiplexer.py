from wire import Wire

class Multiplexer:
    def __init__(self, n):
        self.n = n
        self._inputs = [Wire(0) for _ in range(2**n)]
        self._select_line = 0

    @property
    def select_line(self):
        return self._select_line
    
    @select_line.setter
    def select_line(self, value):
        if value < 0 or value >= 2**self.n:
            raise ValueError(f"Select line value must be between 0 and {2**self.n - 1}")
        self._select_line = value
    

    def get_input(self, index):
        return self._inputs[index]
   
    def update_input_by_index(self, index, setHigh):
        """
        Update the state of the input at the specified index.
        :param index: The index of the input to update
        :param setHigh: If True, set the input to high (1); otherwise, set it to low (0)
        """
        self._inputs[index].state = 1 if setHigh else 0

    def update_inputs(self, values):
        if len(values) != 2**self.n:
            raise ValueError(f"Expected {2**self.n} inputs, got {len(values)}")
        for i in range(2**self.n):
            self._inputs[i].state = values[i]

    def output(self):
        return self._inputs[self._select_line]

if __name__ == "__main__":
    mux = Multiplexer(2)
    mux.update_inputs([0, 1, 1, 0])
    print(mux.output().state)  # Output: 0
    mux.select_line = 1
    print(mux.output().state)  # Output: 1
    mux.select_line = 2
    print(mux.output().state)  # Output: 1
    mux.select_line = 3
    print(mux.output().state)  # Output: 0