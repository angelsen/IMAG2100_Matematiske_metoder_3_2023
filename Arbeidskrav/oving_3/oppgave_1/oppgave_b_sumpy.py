# Jupyter Notebook: Analysis of Curves in Space

## Required Libraries
import sympy as sp
import matplotlib.pyplot as plt

## Functions for the Vectors
def position(t):
    # As we don't have an actual function for r(t), this is a placeholder
    return sp.Matrix([t, t**2, t**3])

def velocity(t):
    # Given from the problem
    return sp.Matrix([-3, 1, 0])

def acceleration(t):
    # Given from the problem
    return sp.Matrix([0, 1, -2])

def unit_tangent(t):
    v = velocity(t)
    mag = v.norm()
    return v / mag

def binormal(t):
    v = velocity(t)
    a = acceleration(t)
    
    v_cross_a = v.cross(a)
    mag = v_cross_a.norm()

    return v_cross_a/mag

def unit_normal(t):
    b = binormal(t)
    unit_t = unit_tangent(t)

    return b.cross(unit_t)

def binormal_unitTangent_cross_unitNormal(t):
    unit_t = unit_tangent(t)
    unit_n = unit_normal(t)

    return unit_t.cross(unit_n)
