from wire import Wire

class Encoder:
    def __init__(self, n):
        """
        Args:
            n (int): number of output lines

        Notes:
            the number of input line will be 2^n
        """

        self.n = n
        self._input_lines = [Wire(0) for i in range(2**n)]
        self._input_lines[0].state = 1
        self._output_lines = [Wire(0) for i in range(n)]
        self._enable = True
        self._input_index_high = 0

    @property
    def enable(self):
        return self._enable
    
    @enable.setter
    def enable(self, value):
        """
        Set the enablel line
        Args:
            value (bool): True for high and False for low

        Raises:
            ValueError: if value is not boolean
        """
        if type(value) is not bool:
            raise ValueError("value should be boolean")
        
        if not value:
            for i in range(self.n):
                self._output_lines[i].state = 0

        self._enable = value
        
    
    def set_input_line_by_index(self, index):
        """
        Set an input line to high by index
        Args:
            index: index of the input line

        Raises:
            IndexError: if index is less than 0 or greater then lenght of input lines - 1
        """

        if index < 0 or index >= 2 ** self.n:
            raise IndexError(f"Range should be between 0 and {2**self.n}")
        for i in range(2 ** self.n):
            self._input_lines[i].state = 1 if i == index else 0
        self._input_index_high = index

    def _int_to_nbit_binary(self, num, n):
        return format(num, f'0{n}b')

    def output(self):
        """
        Gives output on the basis of the input lines

        Return:
            List of Wire object
        """
        if self.enable:
            binary = self._int_to_nbit_binary(self._input_index_high, self.n)
            for i in range(self.n):
                self._output_lines[i].state = int(binary[i])
            

        return self._output_lines
    
if __name__ == "__main__":
    def get_output(out):
        for i in out:
            print(i.state, end = " ")
        print()

    enc = Encoder(2)
    # enable high
    for i in range(4):
        enc.set_input_line_by_index(i)
        out = enc.output()
        get_output(out)

    # enable low
    enc.enable = False
    for i in range(4):
        enc.set_input_line_by_index(i)
        out = enc.output()
        get_output(out)