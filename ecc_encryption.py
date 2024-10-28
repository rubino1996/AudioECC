'''
ecc_encryption.py

This module provides functions for initializing an elliptic curve, generating keys,
computing shared secrets, and performing encryption and decryption on points using 
Elliptic Curve Cryptography (ECC).
'''

import secrets
import tinyec.ec as ec
import numpy as np


def initialize_curve(a, b, p, gx, gy, order, cofactor):
    return ec.Curve(a, b, field=ec.SubGroup(p, g=(gx, gy), n=order, h=cofactor))


def generate_keys(curve):
    private_key = secrets.randbelow(curve.field.p)
    public_key = private_key * curve.g
    return private_key, public_key


def compute_shared_secret(private_key, public_key):
    return private_key * public_key


def encrypt_points(curve, plaintext_points, shared_secret):
    P2 = ec.Point(curve, x=shared_secret.x, y=shared_secret.y)
    return [P1 + P2 for P1 in plaintext_points]


def decrypt_points(curve, encrypted_points, shared_secret_point):
    return [point - shared_secret_point for point in encrypted_points]
