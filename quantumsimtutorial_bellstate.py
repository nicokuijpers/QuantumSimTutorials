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
from quantumsim_circuit import Circuit
from quantumsim_util import QuantumUtil

"""
Create a quantum circuit with 2 qubits, apply a Hadamard gate to the first qubit, 
then a CNOT gate with the first qubit as control and the second qubit as target. 
Run the circuit 1000 times and plot a histogram of the classical states.
The circuit should produce the Bell state (|00> + |11>)/sqrt(2), so the histogram 
should show approximately equal occurrences of |00> and |11>.
"""
circuit = Circuit(2)
circuit.hadamard(0)
circuit.cnot(0, 1)

"""
Run the circuit once and measure the classical state. Print the quantum state 
before and after measurement. The circuit should produce the Bell state 
(|00> + |11>)/sqrt(2), so if you run this code multiple times, you should measure 
|00> as ofen as |11>, but never |01> or |10>.
"""
circuit.execute(print_state=True)
circuit.measure(print_state=True)

"""
Run the circuit 1000 times and plot a histogram of the classical states.
The circuit should produce the Bell state (|00> + |11>)/sqrt(2), so the histogram 
should show approximately equal occurrences of |00> and |11>.
"""
result = QuantumUtil.run_circuit(circuit, nr_runs=1000)
QuantumUtil.histogram_of_classical_states(result)

"""
How to continue?

Above we studied a circuit to obtain the Phi+ Bell state. 
In total, there are four Bell states. See:
https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimBellStates.ipynb

Above we only used the Hadamard and the CNOT operations.
There are many more. See these notebook for operations supported by QuantumSim:
https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimIntroduction.ipynb

https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimMoreOperations.ipynb

The following single-qubit operations are supported:
identity(q)
pauli_x(q)
pauli_y(q)
pauli_z(q)
hadamard(q)
phase(theta, q)
rotate_x(theta, q)
rotate_y(theta, q)
rotate_z(theta, q)
u_gate(self, theta, phi, lam, q)

The following two-qubit operations are supported:
cnot(control, target)
controlled_pauli_y(control, target)
controlled_pauli_z(control, target)
controlled_hadamard(control, target)
controlled_phase(theta, control, target)
controlled_rotate_x(theta, control, target)
controlled_rotate_y(theta, control, target)
controlled_rotate_z(theta, control, target)
controlled_u_gate(theta, phi, lam, control, target)
swap(a, b)

The following three-qubit operations are supported:
fredkin(control, a, b)
toffoli(control_a, control_b, target)

The following multi-qubit operations are supported:
multi_controlled_pauli_z()
multi_controlled_pauli_x()
generic_toffoli(controls:list[int], target:int)

It is possible to measure a single qubit or reset a single qubit in QuantumSim.
See these notebooks for more information:
https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimQubitMeasurement.ipynb

https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimQubitReset.ipynb


1. Implement the four Bell-states
2. Create circuits of one, two, three, four and five qubits and try several combinations of 
    the operations listed above.
3. Create a circuit implementing one of the Bell states and experiment with resetting a 
    qubit before and after applying CNOT.
"""
