class LogicGate:
    def __init__(self):
        pass

    def _typecheck(self, *wires):
        if not all([type(wire) == Wire for wire in wires]):
            raise TypeError("Input should be of type Wire")
        
        
from gates.and_gate import AndGate
from gates.or_gate import OrGate
from gates.not_gate import NotGate
from gates.nand_gate import NandGate
from gates.nor_gate import NorGate
from gates.xor_gate import XorGate
from gates.xnor_gate import XnorGate
from wire import Wire


class Gate:
    @staticmethod
    def and_gate( *wires):
        return AndGate(*wires)

    @staticmethod
    def or_gate( *wires):
        return OrGate(*wires)
    
    @staticmethod
    def not_gate( wire):
        return NotGate(wire)
    
    @staticmethod
    def nand_gate( *wires):
        return NandGate(*wires)
    
    @staticmethod
    def nor_gate( *wires):
        return NorGate(*wires)
    
    @staticmethod
    def xnor_gate( *wires):
        return XnorGate(*wires)
    
    @staticmethod
    def xor_gate( *wires):
        return XorGate(*wires)