import sympy as sp

def velocity():
    return sp.Matrix([-3, 1, 0])

def acceleration():
    return sp.Matric([0, 1, -2])

def unit_tangent(vector: sp.Matrix):
    return vector.normalized()
