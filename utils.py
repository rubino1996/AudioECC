'''
utils.py

This module provides utility functions used across the project, including mathematical operations
for elliptic curve computations. It contains a helper function for calculating the y-coordinate
on an elliptic curve given an x-coordinate and curve parameters.
'''

def compute_y_coordinate(x, a, b, p):
    '''
    Compute the y-coordinate on an elliptic curve for a given x-coordinate.

    Parameters:
    - x (int): The x-coordinate on the elliptic curve.
    - a (int): The coefficient of x in the elliptic curve equation.
    - b (int): The constant term in the elliptic curve equation.
    - p (int): The prime modulus defining the finite field of the curve.

    Returns:
    - int: The computed y-coordinate based on the elliptic curve equation.

    This function calculates y^2 = x^3 + ax + b (mod p) and returns y.
    '''
    y_square = (x ** 3 + a * x + b) % p
    return (pow(y_square, 2)) % p
