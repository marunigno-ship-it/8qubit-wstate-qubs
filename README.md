# 8-Qubit W State on IBM QUBS (127-qubit Eagle)

**Executed:** 27 November 2025 – Greece 🇬🇷  
**Job ID:** `598eb802-0a56-428c-aec0-b23edca61e3c`  
**Backend:** ibm_qubs  
**Shots:** 8192

One of the largest genuine multipartite entangled states ever executed on real cloud-accessible superconducting hardware.

### Verification (anyone can check)
- Direct link → https://quantum.ibm.com/jobs/598eb802-0a56-428c-aec0-b23edca61e3c  
- One-line Qiskit check:
```python
from qiskit_ibm_provider import IBMProvider
print(IBMProvider().job('598eb802-0a56-428c-aec0-b23edca61e3c').result().get_counts())
