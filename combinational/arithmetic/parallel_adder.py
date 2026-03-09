from . import Adder, FullAdder
from wire import Wire

class ParallelAdder(Adder):
    def __init__(self, n = 4):
        """
        n bit parallel adder
        """
        self.n = n
        self._input0 = 0b0000
        self._input1 = 0b0000
        super().__init__()

    @property
    def input0(self):
        return bin(self._input0)
    
    @property
    def input1(self):
        return bin(self._input1)
    
    @input0.setter
    def input0(self, newInput):
        self._input0 = newInput

    @input1.setter
    def input1(self, newInput):
        self._input1 = newInput

    def output(self):
        out = [Wire(0), Wire(0)]
        result = 0b0
        full_adder = FullAdder()
        for i in range(self.n):
            sub_inp0 = (self._input0 >> i) & 1
            sub_inp1 = (self._input1 >> i) & 1
            full_adder.wire0 = sub_inp0
            full_adder.wire1 = sub_inp1
            full_adder.wire2 = 0 if i == 0 else out[0].state
            out = full_adder.output()
            if out[1].state:
                result |= (1 << i)

        return result

if __name__ == "__main__":
    pa = ParallelAdder(n = 20)
    pa.input0 = 200
    pa.input1 = 100
    out = pa.output()
    print(out)

