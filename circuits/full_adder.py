from wire import Wire
from gates import Gate
from . import AddSub

class FullAdder(AddSub):
    def __init__(self):
        self._wire0 = Wire(0)
        self._wire1 = Wire(0)
        self._wire2 = Wire(0)
        super().__init__()

    def _circuit(self):
        int_circuit0 = Gate.and_gate(self._wire0, self._wire1).output()
        int_circuit1 = Gate.and_gate(self._wire1, self._wire2).output()
        int_circuit2 = Gate.and_gate(self._wire0, self._wire2).output()
        out0 = Gate.or_gate(int_circuit0, int_circuit1, int_circuit2).output()

        out1 = Gate.xor_gate(self._wire0, self._wire1, self._wire2).output()

        return [out0, out1]
    
    def output(self):
        return self._circuit()
    
    @property
    def wire0(self):
        return self._wire0
    
    @property
    def wire1(self):
        return self.wire1
    
    @property
    def wire2(self):
        return self.wire2
    
    @wire0.setter
    def wire0(self, wire):
        self._wire0 = Wire(wire)

    @wire1.setter
    def wire1(self, wire):
        self._wire1 = Wire(wire)

    @wire2.setter
    def wire2(self, wire):
        self._wire2 = Wire(wire)