"""
Copyright (c) 2026 Nico Kuijpers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import numpy as np

class Dirac:
    """
    Functions for the Dirac notation to describe (quantum) states and (quantum) operators.
    """
    @staticmethod
    def ket(N, a):
        """
        `|a>` is called 'ket' and represents a column vector with `1` in entry `a` and `0` everywhere else.
        """
        ket = np.zeros((N, 1))
        ket[a, 0] = 1
        return ket

    @staticmethod
    def bra(N, a):
        """
        `<a|` is called 'bra' and represents a row vector with `1` in entry `a` and `0` everywhere else.
        """
        bra = np.zeros((1, N))
        bra[0, a] = 1
        return bra

    @staticmethod
    def bra_ket(N, a, b):
        """
        `<a||b>` is the inner product of `<a|` and `|b>`, which is `1` if `a == b` and `0` `if a != b`.
        """
        bra = Dirac.bra(N, a)
        ket = Dirac.ket(N, b)
        return np.inner(bra, ket.T)

    @staticmethod
    def ket_bra(N, a, b):
        """
        `|a><b|` is the outer product of `|a>` and `<b|`, which is a matrix with `1` in entry (a,b) and `0` everywhere else.
        """
        ket = Dirac.ket(N, a)
        bra = Dirac.bra(N, b)
        return np.outer(ket, bra)

    @staticmethod
    def state_as_string(i,N) -> str:
        if i < 0 or i >= 2**N:
            raise ValueError("Input i and N must satisfy 0 <= i < 2^N")

        binary_string = bin(i)
        state_as_string = binary_string[2:].zfill(N)
        return "|" + state_as_string + ">"
