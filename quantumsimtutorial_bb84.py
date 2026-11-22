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
import random

"""
BB84 quantum key distribution protocol simulation.
This code simulates the BB84 quantum key distribution protocol, where Alice and Bob exchange qubits
to establish a shared secret key. The protocol involves Alice preparing qubits in random bases,
Bob measuring them in random bases, and then both parties comparing their bases to determine the shared key.

1. Alice randomly chooses a basis B ∈ {X, Z} and, randomly and privately, picks a bit b ∈ {0, 1}

2. Alice prepares qubit |q⟩ according to:

B b | |ψ⟩
---------
Z 0 | |0⟩
Z 1 | |1⟩
X 0 | |+⟩
X 1 | |−⟩

3. Alice sends the resulting qubit |q⟩ to Bob

B:  X   Z   X   Z   Z   X   X   X   Z   X   X   X
b:  0   1   1   0   0   0   1   0   1   0   1   0
q: |+⟩ |1⟩ |-⟩ |0⟩ |0⟩ |+⟩ |-⟩ |+⟩ |1⟩ |+⟩ |-⟩ |+⟩

4. Bob randomly chooses a basis B' ∈ {X, Z} and measures the received qubit |q⟩ in that basis, 
obtaining a bit b' ∈ {0, 1}. He privately records the basis B' and the bit b'.

B':  Z   Z   X   X   Z   X   Z   X   X   Z   Z   X
b':  1   1   1   0   0   0   0   0   1   1   1   0
q : |+⟩ |1⟩ |-⟩ |0⟩ |0⟩ |+⟩ |-⟩ |+⟩ |1⟩ |+⟩ |-⟩ |+⟩

5. Alice and Bob publicly compare their bases B and B' for each qubit.

6. They discard the bits b and b' for which B ≠ B', keeping only the bits for which B = B'. 
The remaining bits form the shared secret key.

7. Alice and Bob can use the shared secret key for secure communication,
for example, by using it as a one-time pad for encrypting and decrypting messages.

The BB84 protocol is secure against eavesdropping, as any attempt by an eavesdropper to measure the qubits
will introduce detectable errors in the shared key.
"""

N = 12  # Number of qubits to be sent from Alice to Bob

bases_alice = []  # List to store Alice's bases
bits_alice = []  # List to store Alice's bits
bases_bob = []  # List to store Bob's bases
bits_bob = []  # List to store Bob's bits
shared_key = []  # List to store the shared secret key

for i in range(N):
    # Step 1: Alice randomly chooses a basis B ∈ {X, Z} and a bit b ∈ {0, 1}
    B = random.choice(['X', 'Z'])
    bases_alice.append(B)
    b = random.choice([0, 1])
    bits_alice.append(b)

    # Step 2: Alice prepares qubit |q⟩ according to the chosen basis and bit
    circuit = Circuit(1)
    if B == 'Z':
        if b == 0:
            circuit.identity(0)  # Prepare |0⟩
        else:
            circuit.pauli_x(0)  # Prepare |1⟩
    else:  # B == 'X'
        if b == 0:
            circuit.hadamard(0)  # Prepare |+⟩
        else:
            circuit.pauli_x(0)
            circuit.hadamard(0)  # Prepare |−⟩

    # Step 3: Alice sends the resulting qubit |q⟩ to Bob (simulated by executing the circuit)
    circuit.execute()

    # Step 4: Bob randomly chooses a basis B' ∈ {X, Z} and measures the received qubit |q⟩
    B_prime = random.choice(['X', 'Z'])
    bases_bob.append(B_prime)
    if B_prime == 'Z':
        circuit.measure(print_state=False)  # Measure in Z basis
    else:  # B' == 'X'
        circuit.hadamard(0)  # Change to X basis
        circuit.measure(print_state=False)  # Measure in X basis

    classical_state = circuit.get_classical_state_as_string() # Either |0> or |1>
    b_prime = int(classical_state[1])  # Bob's measured bit
    bits_bob.append(b_prime)

    # Step 5: Alice and Bob publicly compare their bases B and B' for each qubit
    print(f"Alice's basis: {B}, Bob's basis: {B_prime}")

    # Step 6: They discard the bits b and b' for which B ≠ B', keeping only the bits for which B = B'
    if B == B_prime:
        print(f"Shared bit: {b}")
        shared_key.append(b)
    else:
        print("Bases do not match, discarding bits.")

# Step 7: Alice and Bob can use the shared secret key for secure communication
print(f"Alice's bases : {bases_alice}")
print(f"Alice's bits  : {bits_alice}")
print(f"Bob's bases   : {bases_bob}")
print(f"Bob's bits    : {bits_bob}")
print(f"Shared key    : {shared_key}")

"""
How to continue?

In the example code above all bits with the same bases are used to construct the shared key.
Now, assume that Alice and Bob want to distribute an initial key of 128 bits long and use 32 bits 
for checking against eavesdropping.

Another protocol for Quantum Key Distribution is the E91 protocol. This protocol is based on 
entanglement of two qubits. In particular, a Bell state is created and the two entangled qubits
are divided over Alice and Bob.

1. Extend the program above such that Alice and Bob use 32 bits for checking against eavesdropping.
2. Extend the program further such that Alice and Bob share an initial key of 128 bits long.
3. Simulate eavesdropper Eve by letting her measure Alice's qubit and generate a new qubit for Bob. 
    Note that Eve does not know the Alice's basis, hence she has to guess the basis!
4. Verify whether you can detect the presence of an eavesdropper.
5. Study the E91 protocol and implement it.
6. Test the E91 protocol against eavesdropping.
"""