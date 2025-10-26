# Quantum Entanglement Demo – works in VS Code 🧠⚛️

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt   # needed to show plots in VS Code

# 1️⃣ Create 2-qubit circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# 2️⃣ Visualize state before measurement
state = Statevector.from_instruction(qc)
plot_bloch_multivector(state)
plt.show()   # 👈 shows Bloch sphere in VS Code

# 3️⃣ Measure both qubits
qc.measure_all()

# 4️⃣ Simulate using AerSimulator
backend = AerSimulator()
compiled = transpile(qc, backend)
result = backend.run(compiled, shots=1024).result()
counts = result.get_counts()

# 5️⃣ Plot and show histogram
plot_histogram(counts)
plt.show()   # 👈 shows histogram in VS Code
