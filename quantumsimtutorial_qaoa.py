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
from collections import Counter
import math

"""
Function to create a quantum circuit for the Quantum Approximate Optimization Algorithm (QAOA) with p layers.
The circuit consists of alternating cost and mixer layers, where the cost layer is constructed based on the
edges of a graph and the mixer layer applies rotations to all qubits. The parameters gamma and beta control
the angles of the rotations in the cost and mixer layers, respectively.
"""
def qaoa_circuit(gamma:list[float], beta:list[float], nodes:list[int], edges:list[tuple[int, int]], p:int) -> Circuit:
    """
    Creates a quantum circuit of p layers for the Quantum Approximate Optimiziation Algorithm

    Parameters:
    gamma : list of length p containing values for gamma, 0 < gamma < pi
    beta  : list of length p containing values for beta, 0 < beta < pi
    nodes : list of nodes 
    edges : list of edges
    p     : number of layers

    Returns:
    QAOA circuit with p layers
    """

    # Consistency check
    if len(gamma) != p or len(beta) != p:
        raise ValueError(f"Lists gamma and beta should be of length p = {p}")
    
    # Create circuit witn n qubits, where n is the number of nodes
    n = len(nodes)
    circuit = Circuit(n)
    
    # Initialize circuit by applying the Hadamard gate to all qubits
    for q in range(n):
        circuit.hadamard(q)

    # Construct p alternating cost and mixer layers
    for i in range(p):
    
        # Construct cost layer with parameter gamma[i]
        for edge in edges:
            circuit.cnot(edge[0], edge[1])
            circuit.rotate_z(2 * gamma[i], edge[1])
            circuit.cnot(edge[0], edge[1])
        
        # Construct mixer layer with parameter beta[i]
        for q in range(n):
            circuit.rotate_x(2 * beta[i], q)
    
    #return circuit
    return circuit

"""
Function to compute the partition corresponding to the most occurring measurement result from a QAOA circuit.
The function takes as input the nodes and a list of measurement results (as strings) and returns a 
dictionary representing the partition of nodes based on the most frequently measured classical state.
"""
def compute_partition(nodes:list[int], result:list[str]) -> dict:
    """
    Compute partition from the most occurring measurement

    Parameters:
    nodes  : list of nodes
    result : list of strings containing measurements

    Returns:
    Partition corresponding to most occurring result
    """

    # Count occurrences of each string in result
    counter = Counter(result)

    # Get the most occurring string from result
    most_common_string = counter.most_common(1)[0][0]

    # Determine partition corresponding to the most occurring string
    bit_string = most_common_string[1:-1]
    partition = {node: 0 if bit_string[node] == '0' else 1 for node in nodes}

    # Return partition corresponding to the most occurrring string in result
    return partition

"""
Function to compute the cut size of a given partition of nodes in a graph.
The function takes as input a list of edges and a partition dictionary, where the 
keys are node indices and the values are the partition labels (0 or 1). 
It returns the cut size, which is the number of edges that connect nodes in different partitions.
"""
def cut_size(edges, partition):
    return sum(1 for u, v in edges if partition[u] != partition[v])

"""
Example usage of the qaoa_circuit function to create a QAOA circuit for a specific graph and parameters. 
The circuit is then measured multiple times to obtain a histogram of classical states.
The partition corresponding to the most occurring measurement result is computed, and the cut size of 
that partition is calculated and printed.
"""

# Define a graph
nodes = [0, 1, 2, 3, 4]
edges = [(0,1), (0,2), (1,2), (1,3), (2,3), (1,4), (2,4), (3,4)]

# Define number of layers p and parameters gamma and beta for each layer
p = 2
gamma = [math.pi/8] * p
beta = [math.pi/3] * p
print(f"gamma = {gamma}")
print(f"beta = {beta}")

# Create a quantum circuit to solve the Max-Cut problem for the graph defined above
nr_measurements = 10000
circuit = qaoa_circuit(gamma, beta, nodes, edges, p)
result = QuantumUtil.measure_circuit(circuit, nr_measurements=nr_measurements)
partition = compute_partition(nodes, result)
print(f"Partition corresponding to most occurring measurement result: {partition}")
cut = cut_size(edges, partition)
print(f"Cut size of the partition: {cut}")
QuantumUtil.histogram_of_classical_states(result)

"""
How to continue?

In the example above, the number of layers and parameters gamma and beta are defined for each layer.
In practice, values of gamma and beta are found by a classical optimization algorithm.
The value that is being optimized is the weighted average cut size computed from the measurements.
For a function to compute the weighted average cut size and a possible optimization approach, see
https://github.com/nicokuijpers/QuantumSim/blob/main/QuantumSimQAOA.ipynb

Use the example code from the notebook for inspiration:
1. Experiment with p=1 and different values for gamma, and beta.
2. Define a function to compute the weighted average cut size.
3. Use this function to optimize parameters gamma and beta such that the weighted average cut size
   is maximal.
4. Experiment with a different number of layers p. Note that the values for gamma and beta may be
   different per layer, thus the number of parameters to be optimized increases with p.
5. Experiment with different graphs. Keep in mind that the number of nodes should be at most 10 as
   computation time increases exponentially with the number of nodes.
"""