class Wire:
    def __init__(self, bit):
        self._typecheck(bit)
        self._bitState = bit

    @property
    def state(self):
        return self._bitState
    
    @state.setter
    def state(self, bit):
        self._typecheck(bit)
        self._bitState = bit

    def _typecheck(self, bit):
        if bit not in [0, 1]:
            raise ValueError("Can be either 0 or 1")
        
        elif type(bit) != int:
            raise TypeError("Type int required")