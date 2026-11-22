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
from quantumsim_statevector import StateVector
from quantumsim_circuitoperation import CircuitUnitaryOperation, pi_symbol
import numpy as np

class Circuit:
    """
    Class representing a quantum circuit.
    """
    def __init__(self, num_qubits:int, num_bits:int=None):
        self.num_qubits = num_qubits
        if num_bits is None:
            self.num_bits = num_qubits
        else:
            self.num_bits = num_bits
        self.state_vector = StateVector(self.num_qubits)
        self.bit_vector = np.zeros(self.num_bits, dtype=int)
        self.quantum_states = [self.state_vector.get_quantum_state()]
        self.descriptions = []
        self.operations = []

    def identity(self, q):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_identity(self.num_qubits)
        self.descriptions.append(f"Identity on qubit {q}")
        self.operations.append(combined_operation)

    def pauli_x(self, q):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_pauli_x(q, self.num_qubits)
        self.descriptions.append(f"Pauli X on qubit {q}")
        self.operations.append(combined_operation)

    def pauli_y(self, q):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_pauli_y(q, self.num_qubits)
        self.descriptions.append(f"Pauli Y on qubit {q}")
        self.operations.append(combined_operation)

    def pauli_z(self, q):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_pauli_z(q, self.num_qubits)
        self.descriptions.append(f"Pauli Z on qubit {q}")
        self.operations.append(combined_operation)

    def hadamard(self, q):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_hadamard(q, self.num_qubits)
        self.descriptions.append(f"Hadamard on qubit {q}")
        self.operations.append(combined_operation)

    def phase(self, theta, q):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_phase(theta, q, self.num_qubits)
        self.descriptions.append(f"Phase with theta = {theta/np.pi:.3f} {pi_symbol} on qubit {q}")
        self.operations.append(combined_operation)

    def rotate_x(self, theta, q):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_rotate_x(theta, q, self.num_qubits)
        self.descriptions.append(f"Rotate X with theta = {theta/np.pi:.3f} {pi_symbol} on qubit {q}")
        self.operations.append(combined_operation)
    
    def rotate_y(self, theta, q):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_rotate_y(theta, q, self.num_qubits)
        self.descriptions.append(f"Rotate Y with theta = {theta/np.pi:.3f} {pi_symbol} on qubit {q}")
        self.operations.append(combined_operation)
    
    def rotate_z(self, theta, q):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_rotate_z(theta, q, self.num_qubits)
        self.descriptions.append(f"Rotate Z with theta = {theta/np.pi:.3f} {pi_symbol} on qubit {q}")
        self.operations.append(combined_operation)

    def u_gate(self, theta, phi, lam, q):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_u_gate(theta, phi, lam, q, self.num_qubits)
        self.descriptions.append(f"U-gate with (theta,phi,lam) = ({theta/np.pi:.3f} {pi_symbol}, {phi/np.pi:.3f} {pi_symbol}, {lam/np.pi:.3f} {pi_symbol}) on qubit {q}")
        self.operations.append(combined_operation)

    def cnot(self, control, target):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_cnot(control, target, self.num_qubits)
        self.descriptions.append(f"CNOT with control qubit {control} and target qubit {target}")
        self.operations.append(combined_operation)

    def controlled_pauli_y(self, control, target):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_controlled_pauli_y(control, target, self.num_qubits)
        self.descriptions.append(f"Controlled Pauli Y with control qubit {control} and target qubit {target}")
        self.operations.append(combined_operation)

    def controlled_pauli_z(self, control, target):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_controlled_pauli_z(control, target, self.num_qubits)
        self.descriptions.append(f"Controlled Pauli Z with control qubit {control} and target qubit {target}")
        self.operations.append(combined_operation)
    
    def controlled_hadamard(self, control, target):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_controlled_hadamard(control, target, self.num_qubits)
        self.descriptions.append(f"Controlled Hadamard with control qubit {control} and target qubit {target}")
        self.operations.append(combined_operation)

    def controlled_phase(self, theta, control, target):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_controlled_phase(theta, control, target, self.num_qubits)
        self.descriptions.append(f"Controlled phase with theta = {theta/np.pi:.3f} {pi_symbol}, control qubit {control}, and target qubit {target}")
        self.operations.append(combined_operation)

    def controlled_rotate_x(self, theta, control, target):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_controlled_rotate_x(theta, control, target, self.num_qubits)
        self.descriptions.append(f"Controlled rotate X with theta = {theta/np.pi:.3f} {pi_symbol}, control qubit {control}, and target qubit {target}")
        self.operations.append(combined_operation)

    def controlled_rotate_y(self, theta, control, target):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_controlled_rotate_y(theta, control, target, self.num_qubits)
        self.descriptions.append(f"Controlled rotate Y with theta = {theta/np.pi:.3f} {pi_symbol}, control qubit {control}, and target qubit {target}")
        self.operations.append(combined_operation)

    def controlled_rotate_z(self, theta, control, target):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_controlled_rotate_z(theta, control, target, self.num_qubits)
        self.descriptions.append(f"Controlled rotate Z with theta = {theta/np.pi:.3f} {pi_symbol}, control qubit {control}, and target qubit {target}")
        self.operations.append(combined_operation)

    def controlled_u_gate(self, theta, phi, lam, control, target):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_controlled_u_gate(theta, phi, lam, control, target, self.num_qubits)
        self.descriptions.append(f"Controlled U-gate (theta,phi,lam) = ({theta/np.pi:.3f} {pi_symbol}, {phi/np.pi:.3f} {pi_symbol}, {lam/np.pi:.3f} {pi_symbol}), control {control}, and target {target}")
        self.operations.append(combined_operation)

    def swap(self, a, b):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_swap(a, b, self.num_qubits)
        self.descriptions.append(f"SWAP on qubit {a} and qubit {b}")
        self.operations.append(combined_operation)

    def fredkin(self, control, a, b):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_fredkin(control, a, b, self.num_qubits)
        self.descriptions.append(f"Fredkin with control qubit {control} and SWAP on qubit {a} and qubit {b}")
        self.operations.append(combined_operation)
    
    def toffoli(self, control_a, control_b, target):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_toffoli(control_a, control_b, target, self.num_qubits)
        self.descriptions.append(f"Toffoli with control qubit {control_a} and CNOT with control qubit {control_b} and target qubit {target}")
        self.operations.append(combined_operation)

    def multi_controlled_pauli_z(self):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_multi_controlled_pauli_z_operation(self.num_qubits)
        self.descriptions.append(f"Multi-controlled Pauli_Z")
        self.operations.append(combined_operation)

    def multi_controlled_pauli_x(self):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_multi_controlled_pauli_x_operation(self.num_qubits)
        self.descriptions.append(f"Multi-controlled Pauli_X")
        self.operations.append(combined_operation)

    def generic_toffoli(self, controls:list[int], target:int):
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_generic_toffoli(controls, target, self.num_qubits)
        self.descriptions.append(f"Generic Toffoli with controls {controls} and target {target}")
        self.operations.append(combined_operation)

    """
    Create a controlled version of this circuit.
    """
    def create_controlled_circuit(self, control, target, num_qubits):
        # control is control qubit
        # target is qubit in new circuit corresponding to first qubit of current circuit
        # nr_qubits is number of qubits in new circuit
        controlled_circuit = Circuit(num_qubits)
        for operation, description in zip(self.operations, self.descriptions):
            combined_operation = CircuitUnitaryOperation.get_combined_operation_for_controlled_unitary_operation_general(operation, control, target, num_qubits)
            controlled_circuit.operations.append(combined_operation)
            controlled_circuit.descriptions.append(f"Controlled unitary operation {description}")
        return controlled_circuit

    def create_inverse_circuit(self):
        inverse_circuit = Circuit(self.num_qubits, self.num_bits)
        for operation, description in zip(reversed(self.operations), reversed(self.descriptions)):
            inverse_circuit.descriptions.append(description)
            inverse_circuit.operations.append(operation)
        return inverse_circuit
    
    def append_circuit(self, circuit):
        if circuit.num_qubits != self.num_qubits:
            raise ValueError("Function append_circuit: circuit to be appended must have same number of qubits")
        if len(circuit.operations) == len(circuit.descriptions):
            for operation, description in zip(circuit.operations, circuit.descriptions):
                self.operations.append(operation)
                self.descriptions.append(description)
        else:
            raise Exception("Function append_circuit: number of operations and descriptions must be equal")

    def append_circuit_general(self, circuit, start):
        if circuit.num_qubits > self.num_qubits:
            raise ValueError("Function append_circuit_general: circuit to be appended must have less or same number of qubits")
        if len(circuit.operations) == len(circuit.descriptions):
            for operation, description in zip(circuit.operations, circuit.descriptions):
                combined_operation = CircuitUnitaryOperation.get_combined_operation_for_unitary_operation_general(operation, start, self.num_qubits)
                self.operations.append(combined_operation)
                self.descriptions.append(f"Append operation {description}")
        else:
            raise Exception("Function append_circuit_general: number of operations and descriptions must be equal")

    def measurement(self, qubit:int, bit:int):
        if qubit < 0 or qubit >= self.num_qubits:
            raise ValueError("Function measurement: qubit index out of range")
        if bit < 0 or bit >= self.num_bits:
            raise ValueError("Function measurement: bit index out of range")
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_identity(self.num_qubits)
        self.descriptions.append(f"Measurement of qubit {qubit} into classical bit {bit}")
        self.operations.append(combined_operation)

    def reset(self, qubit: int):
        if qubit < 0 or qubit >= self.num_qubits:
            raise ValueError("Function reset: qubit index out of range")
        combined_operation = CircuitUnitaryOperation.get_combined_operation_for_identity(self.num_qubits)
        self.descriptions.append(f"Reset of qubit {qubit}")
        self.operations.append(combined_operation)

    def execute(self, print_state=False):
        self.state_vector = StateVector(self.num_qubits)
        if print_state:
            print("Initial quantum state")
            self.state_vector.print()
        for operation, description in zip(self.operations, self.descriptions):
            if description.startswith("Measurement"):
                qubit = int(description.split()[3])
                bit = int(description.split()[7])
                measured_value = self.state_vector.measure_qubit(qubit)
                self.bit_vector[bit] = measured_value
                self.state_vector.apply_unitary_operation(operation)
            elif description.startswith("Reset"):
                qubit = int(description.split()[3])
                measured_value = self.state_vector.measure_qubit(qubit)
                if measured_value == 1:
                    combined_operation_pauli_x = CircuitUnitaryOperation.get_combined_operation_for_pauli_x(qubit, self.num_qubits)
                    self.state_vector.apply_unitary_operation(combined_operation_pauli_x)
                else:
                    self.state_vector.apply_unitary_operation(operation)
            else:
                self.state_vector.apply_unitary_operation(operation)
            self.quantum_states.append(self.state_vector.get_quantum_state())
            if print_state:
                print(description)
                print(operation)
                print("Current quantum state")
                self.state_vector.print()

    def measure(self, print_state=False):
        self.state_vector.measure()
        if print_state:
            print("Measured state:")
            print(self.state_vector.get_classical_state_as_string())
       
    def get_classical_state_as_string(self):
        return self.state_vector.get_classical_state_as_string()
    