# Authors: Marco Urbano & Ciro Brandi.
from abc import ABCMeta, abstractmethod
import numpy as np

# La classe Error descrive oggetti che hanno il metodo per il calcolo della
# derivata della funzione di errore. PATTERN STRATEGY


class Error(metaclass=ABCMeta):

    @abstractmethod
    def fun(self, Y, T):
        pass


class TSS(Error):
    def fun(self, Y, T):
        return Y - T

class CrossEntropy(Error):
    def softmax(self, Y):
        t_sum = sum(np.exp(Y))
        z_exp = np.exp(Y)

        return [(i / t_sum) for i in z_exp]

    def fun(self, Y, T):
        return self.softmax(Y) - T