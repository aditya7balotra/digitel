from wire import Wire
from combinational.arithmetic import HalfAdder, FullAdder
from gates import Gate

# w0 = Wire(1)
# w1 = Wire(0)

# g0 = Gate.nand_gate(w0).output()
# g1 = Gate.nand_gate(w1).output()
# g3 = Gate.nand_gate(g0, g1)
# print(g3.output().state)

ha = FullAdder()
ha.wire0 = 1
ha.wire1 = 1
ha.wire2 = 1
wires = ha.output()
print(wires[0].state, wires[1].state)