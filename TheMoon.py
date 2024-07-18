from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant
m1 = 5.972e24  # mass of the Earth in kg
m2 = 7.348e22  # mass of the Moon in kg
r = 3.844e8  # distance between Earth and Moon in meters

# Classical calculation of gravitational force
F_classical = G * m1 * m2 / r**2

# Quantum calculation setup
qc = QuantumCircuit(1)

# Apply Hadamard gate to put qubit in superposition
qc.h(0)

# Measure the qubit
qc.measure_all()

# Simulate the quantum circuit
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj, shots=1024).result()
counts = result.get_counts()

# Plot the result
plot_histogram(counts)
plt.show()

# Output classical and quantum results
F_classical, counts
