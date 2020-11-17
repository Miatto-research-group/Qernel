import numpy as np

class Tensor:
    def __init__(self, tensor: np.array):
        self._array = tensor

    def __array__(self):
        return self._array

    def __add__(self, other: Tensor) -> Tensor:
        """
        sum of two tensors
        """
        return Tensor(self._array + other._array)
        # or return Tensor(np.add([self, other]) ?