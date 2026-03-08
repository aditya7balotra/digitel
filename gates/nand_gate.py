from gates.gates import LogicGate
from wire import Wire

class NandGate(LogicGate):
    def __init__(self, *wires):
        super().__init__()
        self._typecheck(*wires)
        self._wires= wires

    def output(self):
        return Wire(int(not all([wire.state for wire in self._wires])))
    