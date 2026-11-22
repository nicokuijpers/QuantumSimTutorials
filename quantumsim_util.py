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
import matplotlib.pyplot as plt
from collections import Counter


"""
Supporting functions for execution, measurement, and visualisation of measurements.
"""
class QuantumUtil:

    """
    Function to run a quantum circuit and measure the classical state.
    """
    def run_circuit(circuit:Circuit, nr_runs=1000):
        result = []
        for i in range(nr_runs):
            circuit.execute()
            circuit.measure()
            result.append(circuit.get_classical_state_as_string())
        return result

    """
    Function to run a quantum circuit once and measure the classical state many times.
    """
    def measure_circuit(circuit:Circuit, nr_measurements=1000):
        circuit.execute()
        result = []
        for i in range(nr_measurements):
            circuit.measure()
            result.append(circuit.get_classical_state_as_string())
        return result

    """
    Function to plot a histogram of all classical states after executing the circuit multiple times.
    """
    def histogram_of_classical_states(string_array):
        histogram = Counter(string_array)
        unique_strings = sorted(list(histogram.keys()))
        counts = [histogram[string] for string in unique_strings]
        plt.bar(unique_strings, counts)
        if len(histogram) > 8:
            plt.xticks(rotation='vertical')
        plt.xlabel('Classical states')
        plt.ylabel('Nr occurrences')
        plt.title('Number of occurrences of classical states')
        plt.show()
