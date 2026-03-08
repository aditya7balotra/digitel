from gates.gates import LogicGate
from wire import Wire

class XorGate(LogicGate):
    def __init__(self, *wires):
        super().__init__()
        self._typecheck(*wires)
        self._wires = wires


    def output(self):
        result = 0
        for wire in self._wires:
            result ^= wire.state
        return Wire(result)