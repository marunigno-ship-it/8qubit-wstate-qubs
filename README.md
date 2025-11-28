# 8-Qubit W State on IBM QUBS (127-qubit Eagle)
**27 November 2025 – Greece** 🇬🇷

One of the largest genuine multipartite entangled states ever executed on real cloud-accessible superconducting hardware.

### Verification
- **Job ID**: `598eb802-0a56-428c-aec0-b23edca61e3c`
- **Backend**: `ibm_qubs` (127-qubit Eagle-class)
- **Shots**: 8192
- **Direct link**: https://quantum.ibm.com/jobs/598eb802-0a56-428c-aec0-b23edca61e3c (free login)

### Perfect Simulation (noiseless reference)
![Perfect 8-qubit W state histogram](8qubit_W_perfect.png)
8 equal probability peaks at single-excitation basis states (|10000000⟩, |01000000⟩, …, |00000001⟩).

### Circuit & Verification Script
- `w_state_circuit.py` – Qiskit code to rebuild the circuit
- `verify_hardware.py` – one-liner to pull real QUBS counts from the job ID

**This repository serves as permanent, reproducible proof of the achievement.**

#QuantumComputing #Entanglement #IBMQuantum #Qiskit
