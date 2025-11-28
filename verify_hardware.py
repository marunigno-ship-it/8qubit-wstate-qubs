# verify_hardware.py – Fetch real QUBS results (run in any Python with Qiskit)
from qiskit_ibm_provider import IBMProvider

job_id = '598eb802-0a56-428c-aec0-b23edca61e3c'
provider = IBMProvider()
job = provider.job(job_id)
counts = job.result().get_counts()

print("Real 8-qubit W-state counts from IBM QUBS:")
print(counts)
# Expected: 8 symmetric peaks ~1024 each
