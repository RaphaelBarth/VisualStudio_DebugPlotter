from collections import deque

class DataSet:
    data_label = ""
    _Xvalues = None
    _Yvalues = None

    def __init__(self,len):
        self._Xvalues=deque(maxlen=len)
        self._Yvalues=deque(maxlen=len)

    def total_elements(self):
        if bool(self._Xvalues):
             return self._Xvalues[-1]
        else:
            return 0 
    
    def append(self,x,y):
        self._Xvalues.append(x)
        self._Yvalues.append(y)
    
    def X(self):
        return self._Xvalues 
    
    def Y(self):
        return self._Yvalues




