"""
Copyright (c) 2026 Nico Kuijpers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS åPROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from quantumsim_circuit import Circuit
from quantumsim_util import QuantumUtil
import math


"""
Function to build a Grover oracle for multiple marked states. 
The input is a list of bit-strings, each representing a marked state.
The function returns a Circuit object representing the Grover oracle.
"""
def grover_oracle(marked_states):
    """Build a Grover oracle for multiple marked states

    Here we assume all input marked states have the same number of bits

    Parameters:
        marked_states (str or list): Marked states of oracle

    Returns:
        Circuit: Quantum circuit representing Grover oracle
    """
    if not isinstance(marked_states, list):
        marked_states = [marked_states]

    # Determine the number of qubits in circuit
    num_qubits = len(marked_states[0])

    # Create the circuit
    circuit = Circuit(num_qubits)

    # Mark each target state in the input list
    for target in marked_states:
        # Find the indices of all the '0' elements in bit-string
        zero_inds = [ind for ind in range(num_qubits) if target.startswith("0",ind)]

        # Add a multi-controlled Z-gate with pre- and post-applied X-gates (open-controls)
        # where the target bit-string has a '0' entry
        for i in zero_inds:
            circuit.pauli_x(i)
        circuit.multi_controlled_pauli_z()
        for i in zero_inds:
            circuit.pauli_x(i)

    return circuit

"""
Function to build a Grover operator for multiple marked states.
The input is a list of bit-strings, each representing a marked state.
The function returns a Circuit object representing the Grover operator.
"""
def grover_operator(marked_states):
    num_qubits = len(marked_states[0])
    oracle = grover_oracle(marked_states)
    grover = Circuit(num_qubits)
    grover.append_circuit(oracle)
    for q in range (num_qubits):
        grover.hadamard(q)
    for q in range (num_qubits):
        grover.pauli_x(q)
    grover.hadamard(num_qubits - 1)
    grover.multi_controlled_pauli_x() 
    grover.hadamard(num_qubits - 1)
    for q in range (num_qubits):
        grover.pauli_x(q)
    for q in range (num_qubits):
        grover.hadamard(q)
    return grover

"""
Function to compute the optimal number of iterations for Grover's algorithm given the marked states.
The optimal number of iterations is given by the formula:
    optimal_num_iterations = floor(pi / (4 * arcsin(sqrt(M / N))))
where M is the number of marked states and N is the total number of states (2^n for n qubits).
The function returns the optimal number of iterations as an integer.
"""
def optimal_num_iterations(marked_states):
    return max(1,math.floor(math.pi / (4 * math.asin(math.sqrt(len(marked_states) / 2**len(marked_states[0]))))))

"""
Function to create a Grover circuit for multiple marked states.
The input is a list of bit-strings, each representing a marked state.
The function returns a Circuit object representing the Grover circuit.
The Grover circuit consists of an initial Hadamard transform on all qubits, 
followed by the Grover operator applied for the optimal number of iterations.
"""
def create_grover_circuit(marked_states):
    if not isinstance(marked_states, list):
        marked_states = [marked_states]
    nr_iterations = optimal_num_iterations(marked_states)
    num_qubits = len(marked_states[0])
    circuit_grover_operator = grover_operator(marked_states)
    circuit = Circuit(num_qubits)
    for q in range(num_qubits):
        circuit.hadamard(q)
    for i in range(nr_iterations):
        circuit.append_circuit(circuit_grover_operator)
    return circuit

#marked_states = ["0000","0001","0011","0111","1111"] # 1 iteration
#marked_states = ["01010","01011","01110","10101"] # 2 iterarations
marked_states = ["01011","10101"] # 3 iterarations
#marked_states = ["01011"] # 4 iterarations

nr_iterations = optimal_num_iterations(marked_states)
print(f"Nr iterations is {nr_iterations} for marked states {marked_states}")

circuit = create_grover_circuit(marked_states)

result = QuantumUtil.measure_circuit(circuit, nr_measurements=1000)
QuantumUtil.histogram_of_classical_states(result)


"""
How to continue?

The code to create a Grover circuit is based on this notebook:
https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimGroverAlgorithm.ipynb

Note that this code requires the full implementation of quantumsim:
https://github.com/nicokuijpers/QuantumSim/blob/main/quantumsim.py

This implementation of QuantumSim also requires a folder /assets/noise_parameters
https://github.com/nicokuijpers/QuantumSim/tree/main/assets/noise_parameters

The Grover oracle is created for a given set of 'marked states'. In general, an
oracle can be defined as a function that determines whether a given binary string
is valid or not. For example, it is possible to define an oracle that checks whether
a given input string is a valid solution to a Sudoku puzzle.

For example code of solving a 2 x 2 Sudoku puzzle using Grover's algorithm, see
https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimSudokuSolver.ipynb

In principle any classical algorithm can be implemented on a quantum computer.
For example, it is possible to implement a counter that counts the number of ones
in binary string. 

For example code of a counter that counts the number of ones in binary string, see:
https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimCounter.ipynb

Using this counter a Grover search can be applied to find all possible binary strings 
with a given number of ones. See:
https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimCounterGroverSearch.ipynb

Another example is to find all possible combinations of a and b for which a + b = S. 
For this, a quantum implementation of an adder is needed.

For example code of a 3-qubit adder that adds to numbers a and b, 0 <= a,b < 8, see:
https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimThreeQubitAdder.ipynb

Using this 3-qubit adder a Grover search algorithm can be defined to find all possible
a, b with a + b = S for given S. See:
https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimThreeQubitAdderGrover.ipynb

Use the example code from the notebooks for inspiration:
1. Download the full implementation of QuantumSim and the folder /assets/noise_parameters
2. Adapt the code above such that it works with the full implementation of QuantumSim.
3. Implement a 2 x 2 Sudoku solver and test it.
3. Implement a counter and test it.
4. Implement a Grover oracle based on the Counter and test it.
5. Implement a 3-qubit adder and test it.
6. Implement a Grover oracle based on the 3-qubit adder and test it.
"""