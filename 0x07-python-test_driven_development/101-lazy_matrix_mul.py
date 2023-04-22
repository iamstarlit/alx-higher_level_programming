#!/usr/bin/python3
"""
101-lazy_matrix_mul.py

This module has a function to multiply two matrices
using `numpy` module.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies tow matrices.

    Args:
        m_a: matrix `a` parameter
        m_b: matrix `b` parameter

    Returns:
        product of m_a and m_b matrix
    """

    # Perform matrix multiplication using np.matmul()
    return (np.matmul(m_a, m_b))
