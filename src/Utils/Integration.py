import numpy as np
from .Physics import CalculateDrag


def RK4(obj, dt):
    """
    Perform one RK4 integration step for the object.

    Parameters:
        obj (Object): The object to simulate.
        dt (float): Time step for integration.

    Returns:
        None: Updates the object's state in place.
    """

    def Derivative(state, obj):
        """
        Compute the derivative of state (position and velocity).
        
        Parameters:
            state (np.array): Current state [x, y, vx, vy].
            obj (Object): The object to simulate.
            
        Returns:
            np.array: [vx, vy, ax, ay]
        """
        x, y, vx, vy = state

        # Compute drag force
        fx_drag, fy_drag = CalculateDrag(obj, vx, vy)

        # Total forces = drag + external force
        fx_total = fx_drag + obj.thrust[0]
        fy_total = fy_drag + obj.thrust[1]

        # Acceleration from total forces
        ax = fx_total / obj.mass
        ay = fy_total / obj.mass

        # Return the derivatives (dx/dt, dy/dt, dvx/dt, dvy/dt)
        return np.array([vx, vy, ax, ay])

    # Current state: [x, y, vx, vy]
    state = np.array([obj.x, obj.y, obj.xVelo, obj.yVelo])

    # RK4 steps
    k1 = Derivative(state, obj)
    k2 = Derivative(state + 0.5 * dt * k1, obj)
    k3 = Derivative(state + 0.5 * dt * k2, obj)
    k4 = Derivative(state + dt * k3, obj)

    # Update state
    new_state = state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    # Update object attributes
    obj.x, obj.y, obj.xVelo, obj.yVelo = new_state
