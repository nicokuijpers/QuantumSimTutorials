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
from quantumsim_dirac import Dirac
from quantumsim_qubitoperation import QubitUnitaryOperation

class StateVector:
    """
    Class representing a quantum circuit of N qubits.
    """
    def __init__(self, N):
        self.N = N
        self.index = 0
        self.state_vector = np.zeros((2**self.N, 1), dtype=complex)
        self.state_vector[self.index] = 1

    def apply_unitary_operation(self, operation):
        # Check if operation is a unitary matrix
        # Note that this operation is computationally intensive for a larger number of qubits
        if self.N <= 8:
            if not np.allclose(np.eye(2**self.N), np.conj(operation.T) @ operation):
                raise ValueError("Input matrix is not unitary")
        self.state_vector = operation @ self.state_vector

    def measure(self):
        probalities = np.square(np.abs(self.state_vector)).flatten()
        self.index = np.random.choice(len(probalities), p=probalities)

    def measure_qubit(self, q) -> int:
        identity = QubitUnitaryOperation.get_identity()
        ket_bra_00 = Dirac.ket_bra(2,0,0)
        ket_bra_11 = Dirac.ket_bra(2,1,1)
        P0 = np.eye(1,1)
        P1 = np.eye(1,1)
        for i in range(self.N):
            if i == q:
                P0 = np.kron(P0, ket_bra_00)
                P1 = np.kron(P1, ket_bra_11)
            else:
                P0 = np.kron(P0, identity)
                P1 = np.kron(P1, identity)
        prob_0 = np.vdot(self.state_vector, P0.dot(self.state_vector)).real
        prob_1 = np.vdot(self.state_vector, P1.dot(self.state_vector)).real
        r = np.random.random()
        if r <= prob_0:
            self.state_vector = np.dot(P0,self.state_vector)/np.sqrt(prob_0)
            return 0
        else:
            self.state_vector = np.dot(P1,self.state_vector)/np.sqrt(prob_1)
            return 1

    def get_quantum_state(self):
        return self.state_vector
    
    def get_classical_state_as_string(self):
        return Dirac.state_as_string(self.index, self.N)
    
    def print(self):
        for i, val in enumerate(self.state_vector):
            print(f"{Dirac.state_as_string(i, self.N)} : {val[0]}")
