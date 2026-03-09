from gates import Gate
from wire import Wire
from . import Adder

class HalfAdder(Adder):
    def __init__(self):
        self._w0 = Wire(0)
        self._w1 = Wire(0)
        super().__init__()

    def _circuit(self):
        int_circuit0 = Gate.and_gate(self._w0, self._w1)
        int_circuit1 = Gate.xor_gate(self._w0, self._w1)
        return [int_circuit0.output(), int_circuit1.output()]
    
    def output(self):
        return self._circuit()
    
    @property
    def wire0(self):
        return self._w0
    
    @property
    def wire1(self):
        return self._w1
    
    @wire0.setter
    def wire0(self, wire):
        self._w0 = Wire(wire)

    @wire1.setter
    def wire1(self, wire):
        self._w1 = Wire(wire)

