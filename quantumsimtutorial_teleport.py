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
Function to create a quantum circuit for quantum teleportation of a qubit state |psi>.
By rotation around the x-axis with angle theta, it holds |psi> = cos(theta/2)|0> - i sin(theta/2)|1>
The circuit has 3 qubits and 3 classical bits.
Qubit 0 is in the possession of Alice and has state |psi>, the state to be teleported
Qubit 1 is Alice's half of the Bell pair
Qubit 2 is Bob's half of the Bell pair and also the destination of the teleportation
The function returns a Circuit object representing the quantum teleportation circuit.
"""
def create_teleport_circuit(theta):

    # Create a circuit of 3 qubits
    # Qubit 0 is in the possession of Alice and has state |psi>, the state to be teleported
    # Qubit 1 is Alice's half of the Bell pair
    # Qubit 2 is Bob's half of the Bell pair and also the destination of the teleportation
    circuit = Circuit(num_qubits=3, num_bits=3)

    # ========================
    # Step 0: Create the state |psi> to be teleported in qubit 0
    # The state |psi> is created by applying a rotation around the x-axis
    circuit.rotate_x(theta, 0)

    # ========================
    # Step 1: create an entangled Bell pair between Alice and Bob (qubits 1 and 2)
    circuit.hadamard(1)
    circuit.cnot(1,2)

    # ========================
    # Step 2: Alice applies a series of operations 
    # between the state to teleport (qubit 0) and her half of the Bell pair (qubit 1)
    circuit.cnot(0, 1)
    circuit.hadamard(0)

    # ========================
    # Step 3: Alice measures both qubits 0 and 1
    circuit.measurement(0, 0)
    circuit.measurement(1, 1)

    # ========================
    # Step 4: Now that Alice has measured the two qubits, their states have collapsed to 0 and 1. 
    # Bob can do operations conditioned on these qubits to his half of the Bell pair
    # Note that while we're conditioning Bob's operation on the collapsed qubits 0 and 1, we can
    # do teleportation over long distances by transmitting the classical information in classical bits 0 and 1
    circuit.cnot(1,2)
    circuit.controlled_pauli_z(0,2)

    # Step 5: Bob's qubit now has state |psi>, the state that was teleported
    return circuit


"""
Create a quantum circuit for quantum teleportation of a qubit state |psi> = cos(theta/2)|0> - i sin(theta/2)|1>
The circuit has 3 qubits and 3 classical bits.
Qubit 0 is in the possession of Alice and has state |psi>, the state to be teleported
Qubit 1 is Alice's half of the Bell pair
Qubit 2 is Bob's half of the Bell pair and also the destination of the teleportation
The circuit is executed 1000 times and a histogram of the classical states is plotted.
For example, when theta = 0 the state is |psi> = |0>, and the histogram should show that the classical states 
000, 010, 100, 110 occur approximately equally often. Thus the third bit is zero, which indicates that the state 
|0> has been successfully teleported to Bob's qubit.
"""
theta = 0
# theta = np.pi
# theta = np.pi/2
# theta = np.pi/3
# theta = np.pi/4
circuit = create_teleport_circuit(theta)
result = QuantumUtil.run_circuit(circuit, nr_runs=1000)
QuantumUtil.histogram_of_classical_states(result)

"""
How to continue?

To confirm successful teleportation you can run and measure the circuit 1000 times.
After each measurement, count the numbers of zeros and ones measured for the third
qubit (Bob's qubit). The ratio between zeros and ones should correspond to the value of theta.

See this notebook for an example:
https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimTeleportation.ipynb

1. In the code above, try different values of theta.
2. Write a loop over values for theta between 0 and 4*pi with steps of pi/8.
3. For each value of theta, run the circuit 1000 times and determine the percentage
    of ones measured for the third qubit.
4. Plot the percentage of ones measured for the third qubit against theta.
5. Does the observed percentage of ones correspond to the expected percentage?
    Hint: keep the Bloch sphere in mind.
"""
