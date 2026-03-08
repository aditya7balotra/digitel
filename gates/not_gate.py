from gates.gates import LogicGate
from wire import Wire

class NotGate(LogicGate):
    def __init__(self, wire):
        super().__init__()
        self._typecheck(wire)
        self._wire = wire

    def output(self):
        return Wire(int(not self._wire.state))