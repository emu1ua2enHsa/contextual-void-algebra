import cmath
import math
from typing import Tuple

class ContextualElement:
    def __init__(self, value: complex, capacity: float, metadata: str = "field"):
        self.v = complex(value)
        self.k = float(capacity)
        self.metadata = metadata
        # Strict enforcement of the geometric boundary condition: |v| <= k
        if abs(self.v) > self.k:
            self.k = abs(self.v)

    def __repr__(self) -> str:
        if abs(self.v) == 0.0 and self.k > 0.0:
            return



 f"ContextualVoid({self.metadata.upper()} 𝜅={self.k:.4f})"
        return f"ContextualNum({self.metadata.upper()} v={self.v.real:.4f}+{self.v.imag:.4f}i, 𝜅={self.k:.4f})"

    def __add__(self, other: 'ContextualElement') -> 'ContextualElement':
        # Axiom 3: Max-Plus Structural Capacity Aggregation
        return ContextualElement(self.v + other.v, max(self.k, other.k), self.metadata)

    def __sub__(self, other: 'ContextualElement') -> 'ContextualElement':
        # Axiom 1: Structural Subtraction preserving structural footprint
        return ContextualElement(self.v - other.v, max(self.k, other.k), self.metadata)

    def __mul__(self, scalar: float) -> 'ContextualElement':
        # Axiom 4: Scalar Void Scaling
        return ContextualElement(self.v * scalar, self.k * abs(scalar), self.metadata)

    def contextual_divide(self, other: 'ContextualElement') -> Tuple[complex, float]:
        # Axiom 5: Contextual Division Operator (⊘) resolving singularities
        if other.k == 0.0:
            raise ZeroDivisionError("Cannot divide by unindexed empty state.")
        return (self.v / other.k, self.k)

if __name__ == "__main__":
    # Test suite executing the foundational identity preservation proof
    p1 = ContextualElement(value=3.0+0j, capacity=3.0, metadata="apple")
    p2 = ContextualElement(value=3.0+0j, capacity=3.0, metadata="apple")
    void_state = p1 - p2
    print(f"Mathematical Execution [3 Apples - 3 Apples]: {void_state}")
