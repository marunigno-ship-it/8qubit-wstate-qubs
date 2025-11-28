# Hybrid Quantum-Classical Mapping (8 → 8)

Single 8-qubit W state used as decision kernel for humanoid robot.

| Quantum basis state   | Classical robot event                  | Priority |
|-----------------------|----------------------------------------|----------|
| \|10000000⟩           | Left arm obstacle                      | 1        |
| \|01000000⟩           | Right arm obstacle                     | 1        |
| \|00100000⟩           | Human detected (vision)                | 2        |
| \|00010000⟩           | Foot pressure anomaly                  | 3        |
| \|00001000⟩           | Battery critical                       | 4        |
| \|00000100⟩           | Voice command received                 | 2        |
| \|00000010⟩           | Overheating                            | 4        |
| \|00000001⟩           | Balance loss                           | 5        |

One measurement of the W state selects one event with equal quantum probability.  
Classical controller executes the corresponding action.

This is the first prototype of a **quantum-native decision layer** for robotics.
