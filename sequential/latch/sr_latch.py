from gates.nand_gate import NandGate
from gates.nor_gate import NorGate
from wire import Wire
import warnings

class SrLatch:
    def __init__(self, isNor = True):
        """
        Args:
            isNor (bool): True gives Nor Sr Latch. False gives Nand SR Latch
        """
        self._s = Wire(0)
        self._r = Wire(0)
        self._gate = NorGate if isNor else NandGate
        self._output_lines = [Wire(0) for i in range(2)]

    # def set_s(self, isHigh):
    #     """
    #     Set S line
    #     Args:
    #         isHigh: True sets high and False sets low
    #     Raises:
    #         ValueError: if isHigh is not boolean
    #     """
    #     if type(isHigh) is not bool:
    #         raise ValueError("isHigh should be boolean")
    #     self._s.state = 1 if isHigh else 0
    #     self._r.state = 0

    #     if self._gate == NandGate and not isHigh and self._r.state == 0:
    #         self._r.state = 1

    # def set_r(self, isHigh):
    #     """
    #     Set R line
    #     Args:
    #         isHigh: True sets high and False sets low
    #     Raises:
    #         ValueError: if isHigh is not boolean
    #     """
    #     if type(isHigh) is not bool:
    #         raise ValueError("isHigh should be boolean")
    #     self._r.state = 1 if isHigh else 0
    #     self._s.state = 0

    #     if self._gate == NandGate and not isHigh and self._s.state == 0:
    #         self._s.state = 1
    

    @property
    def s(self):
        return self._s
    
    @s.setter
    def s(self, isHigh):
        """
        Set the S line
        Args:
            isHigh (bool): True sets high and False sets low

        Raises:
            ValueError : if isHigh is not boolean
        """
        if type(isHigh) is not bool:
            raise ValueError("isHigh should be boolean")
        
        self._s.state = 1 if isHigh else 0
        if isHigh and self._r.state == 1 and self._gate == NorGate:
            warnings.warn("Both R and S line should not be high", RuntimeWarning)
        elif not isHigh and self._r.state == 0 and self._gate == NandGate:
            warnings.warn("Both R and S lines should not be low", RuntimeWarning)

    @property
    def r(self):
        return self._r
    
    @r.setter
    def r(self, isHigh):
        """
        Set the R line
        Args:
            isHigh (bool): True sets high and False sets low

        Raises:
            ValueError : if isHigh is not boolean
        """
        if type(isHigh) is not bool:
            raise ValueError("isHigh should be boolean")
        self._r.state = 1 if isHigh else 0
        if isHigh and self._s.state == 1 and self._gate == NorGate:
            warnings.warn("Both R and S should not be high", RuntimeWarning)
        elif not isHigh and self._r.state == 0 and self._gate == NandGate:
            warnings.warn("Buth R and S lines should not be low", RuntimeWarning)

    
    def get_sr_lines(self):
        """
        Returns the S and R lines in list
        """
        return [self._s, self._r]

    def output(self):
        """
        Returns the output lines
        Returns:
            1. List with Q' first then Q
        """
        while True:
            _gateS = self._gate(self._s, self._output_lines[1])
            _gateR = self._gate(self._r, _gateS.output())
            if _gateS.output().state == self._output_lines[0].state and _gateR.output().state == self._output_lines[1].state:
                break

            self._output_lines = [_gateS.output(), _gateR.output()]

        return self._output_lines
    
if __name__ == "__main__":
    def get_output(out):
        for i in out:
            print(i.state, end = " ")
        print()
        print()


    sr_latch = SrLatch(isNor = True)
    states = [[False, False], [True, False], [False, True], [True, True]]

    for i in states:
        sr_latch.s = i[0]
        sr_latch.r = i[1]
        out = sr_latch.output()
        get_output(out)
        sr_latch.s = False
        sr_latch.r = False
        
