from pytket.circuit import Circuit, OpType
from pytket.extensions.qiskit import tk_to_qiskit
from pytket.extensions.cirq import tk_to_cirq

c = Circuit(4, name="example")
c.add_gate(OpType.CU1, 0.5, [0,1])
c.H(1).X(1).Y(2).Z(3)
c.X(1).CX(1,2).Y(1).Z(2).H(3)
c.Y(1).Z(1)
c.add_gate(OpType.CU1, 0.5, [2,3])
c.H(2).X(3)
c.Z(1).H(1).X(2).Y(3).CX(3,0)

print('=== Information on the Circuit ===')
print('Name of the Circuit:',c.name)
print('Number of the Qubits in the Circuit:',c.n_qubits)
print('Depth of the Circuit:',c.depth())
print()
print('=== Visualization of the Circuit ===')
print('Via Qiskit')
print(tk_to_qiskit(c))
#print()
#print('Via Cirq')
#print(tk_to_cirq(c))
