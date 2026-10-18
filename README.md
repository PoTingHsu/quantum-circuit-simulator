

# Quantum Circuit Simulator

An interactive two-qubit quantum circuit simulator developed in Python for an undergraduate Computational Physics project (2023).

## Description

This project allows users to build quantum circuits by dragging and dropping quantum gates.

The simulator uses NumPy to calculate quantum state evolution and Matplotlib to display measurement probabilities.

The graphical interface is developed using Pygame, with additional 3D visualization using VPython.

Supported gates include H, X, Y, Z, S, T, RX, RY, RZ, and CNOT.

## Requirements

The code requires:

- Python
- NumPy
- Pygame
- Matplotlib
- Pillow
- VPython

## Usage

Run `quantum_circuit_simulator` to launch the simulator.

Drag quantum gates onto the circuit and click **Calculate** to display the measurement probabilities.

For the CNOT gate, place it on the first (upper) qubit line. The gate acts on both qubits, with the first qubit as the control and the second as the target.

## Limitations

- The simulator supports only two qubits.
- The Bloch sphere visualization is incomplete and does not accurately represent entangled states.
- Measurement probabilities are calculated without simulating state collapse.
- Some gate combinations have not been fully tested.
