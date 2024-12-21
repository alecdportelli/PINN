import numpy as np

from .Constants import *


def CalculateDrag(obj, vx, vy):
    """
    Compute the drag force on the object.

    Parameters:
        obj (Object): The object to simulate.
        vx, vy (float): Current position and velocity.

    Returns:
        (fx, fy): Drag force components.
    """
    
    speed = np.sqrt(vx**2 + vy**2)
    dragMagnitude = 0.5 * RHO_AIR * obj.cD * obj.cA * speed**2

    fx = -dragMagnitude * (vx / speed) if speed > 0 else 0
    fy = -dragMagnitude * (vy / speed) if speed > 0 else 0

    return fx, fy
