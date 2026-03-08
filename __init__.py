class Wire:
    def __init__(self, bit):
        self._typecheck(bit)
        self._bitState = bit

    @property
    def state(self):
        '''
        getter for bitState
        '''
        return self._bitState
    
    @state.setter
    def state(self, bit):
        '''
        setter for bitState
        '''
        self._typecheck(bit)
        self._bitState = bit

    def _typecheck(self, bit):
        if bit not in [0, 1]:
            raise ValueError("Only 0 and 1 allowed as bit")
        elif type(bit) != int:
            raise TypeError("bit is required to be of type int")