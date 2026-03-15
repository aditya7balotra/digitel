from wire import Wire
from sequential.latch.sr_latch import SrLatch

class SrFlipFlop:
    def __init__(self):
        self._s = Wire(0)
        self._r = Wire(0)
        self._enable = Wire(1)
        self._output_lines = [Wire(0), Wire(0)] # [Q', Q]
        self._sr_nor_latch = SrLatch(isNor= True)

    def output(self):
        """
        Returns the output line [Q', Q]
        """
        if self._enable:
            pass

        ## else
