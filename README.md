# Quantum Computer Simulator with Pygame

A fun and interactive visual simulation of a quantum computer built using Python and Pygame. This project lets you play around with qubits, apply quantum gates, and see how quantum states change in real-time.

---

## What It Does

- **Qubits**: Visualize qubits as circles that can be in superposition or classical states.
- **Quantum Gates**:
  - **Hadamard (H) Gate**: Puts qubits into superposition.
  - **Pauli-X (X) Gate**: Flips the qubit state (|0⟩ to |1⟩ and vice versa).
- **Measurement**: Collapse qubits to either |0⟩ or |1⟩ randomly, based on their probabilities.
- **Reset**: Reset qubits back to their initial state (|0⟩).
- **Probabilities**: See the probabilities of |0⟩ and |1⟩ states when qubits are in superposition.

---

## How to Run It

1. **Clone the repo**:
   ```bash
   git clone https://github.com/deniscraciungabriel/qbitsSimulation.git
   cd qbitsSimulation
   ```

2. **Install dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install pygame numpy
   ```

3. **Run the simulator**:
   ```bash
   python main.py
   ```

---

## How to Use

- **Apply Gates**:
  1. Click on a gate button (H, X, or Measure).
  2. Click on a qubit to apply the gate or measure it.
- **Reset Qubits**:
  - Click the "Reset" button to set all qubits back to |0⟩.
- **See Probabilities**:
  - When qubits are in superposition, their probabilities are shown below them.

---
