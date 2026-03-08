from gates.gates import LogicGate
from wire import Wire

class XnorGate(LogicGate):
    def __init__(self, *wires):
        super().__init__()
        self._typecheck(*wires)
        self._wires = wires

    def output(self):
        result = 0
        for wire in self._wires:
            result ^= 1

        return Wire(int(not result))