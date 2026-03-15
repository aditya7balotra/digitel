from wire import Wire

class Decoder:
    def __init__(self, n):
        """
        Args:
            n (int): number of input lines

        Notes:
            number of output lines will be 2**n
        """
        self.n = n
        self._input_lines = [Wire(0) for i in range(self.n)]
        self._output_lines = [Wire(0) for i in range(2**n)]
        self._enable = True

    @property
    def enable(self):
        return self.enable
    
    @enable.setter
    def enable(self, value):
        """
        Set the enable line
        Args:
            value: True or False

        Raises:
            ValueError: if value is either of True or False
        """
        if type(value) is not bool:
            return ValueError("value should be bool")
        if not value:
            for i in range(2**self.n):
                self._output_lines[i].state = 0

        self._enable = value
    


    def change_input_by_index(self, index, setHigh):
        """
        Change the bit value of an input line

        Args:
            index: index of the input line
            setHigh: if True, set the line high else low
        """
        if index < 0 or index >= self.n:
            return ValueError(f"Line index can be only between 0 and {self.n - 1}")
        
        self._input_lines[index].state = 1 if setHigh else 0

    def change_input_lines(self, values):
        """
        Change the bit values of all input lines

        Args:
            values (List<int>): list of integers with corresponding input line value

        Raises:
            ValueError: if length of values is not equals the input lines

        """
        if len(values) != self.n:
            raise ValueError(f"Length should be {self.n}")
        
        for i in range(self.n):
            self._input_lines[i].state = values[i]

    def output(self):
        if self._enable:
            inputStatus = "".join([str(i.state) for i in self._input_lines])
            index = int(inputStatus, 2)
            for i in range(2**self.n):
                self._output_lines[i].state = 0 if i != index else 1
            
            return self._output_lines
        
        return self._output_lines
    
if __name__ == "__main__":
    def get_output(out):
        for i in out:
            print(i.state, end= " ")
        print()
    
    dcdr = Decoder(2)

    # enable true
    for i in ([[0, 0], [0, 1], [1, 0], [1, 1]]):
        dcdr.change_input_lines(i) 
        out = dcdr.output()
        get_output(out)

    # enable false
    dcdr.enable = False
    for i in ([[0, 0], [0, 1], [1, 0], [1, 1]]):
        dcdr.change_input_lines(i) 
        out = dcdr.output()
        get_output(out)

    # changing by index
    dcdr.enable = True
    print('change by index')
    dcdr.change_input_lines([0, 0])
    for i in range(2):
        dcdr.change_input_by_index(i, True)
        out= dcdr.output()
        get_output(out)
    