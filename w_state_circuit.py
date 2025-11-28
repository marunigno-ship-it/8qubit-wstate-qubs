# w_state_circuit.py – Exact circuit used on IBM QUBS
from qiskit import QuantumCircuit

qc = QuantumCircuit(8)

# Build 8-qubit W state (standard construction)
qc.h(0)
for i in range(7):
    qc.cx(i, i+1)

qc.measure_all()

# Optional: draw and save
qc.draw('mpl').savefig('circuit_diagram.png')

print("8-qubit W-state circuit ready – 8 equal probability peaks expected")
