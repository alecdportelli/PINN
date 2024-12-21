from Components.Object import *

from Utils.Constants import *
from Utils.Integration import *
from Utils.Physics import *
from Utils.Plotting import *

import numpy as np


if __name__ == "__main__":
    ''' Simulation Params '''
    SECONDS = 1000
    DT = (1/60)
    PLOT = True

    ''' Create object '''
    obj = Cube(length=1, mass=20)
    positions = []

    ''' Run the actual simulation '''
    for step in range(int(SECONDS / DT)):
        obj.SetThrust(10)  
        obj.UpdateDynamics(DT)
        positions.append((obj.x, obj.y))

    if PLOT:
        PlotPath(positions)

    