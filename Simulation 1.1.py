__author__ = 'Joshua Gore'
"""
CRITICAL MASS FOR A FISSION CHAIN REACTION
---------------------18/9/14---------------------
This program computes the survival fraction, F,
for a rectangular slab of fissionable material. F
is defined as the number of induced fissions per
spontaneous fission. For values of F greater than
1.0, a chain reaction occurs. The slab has
"critical mass" if it has F=1. We assume that two
neutrons are emitted per fission.
"""

#initialise

import math
import random


def rand9():
    r = []
    for k in range(0, 9):
        r.append(random.random())
    return r

#Input
y = 'y'
while y == 'y' or y == 'Y':
    print("INPUT VALUES FOR THE FOLLOWING: (PRESS RETURN TO ENTER)")
    M = float(input(" THE MASS OF THE RECTANGULAR SLAB (M): "))
    S = float(input(" THE RATIO OF LENGTH TO THICKNESS (S): "))
    N = float(input(" THE NUMBER OF RANDOMLY GENERATED FISSIONS (N): "))
    print("")

    # Calculate dimensions
    A = (M * S) ** (1 / 3)
    B = (M / S ** 2) ** (1 / 3)
    L1 = A / 2
    L2 = A / 2
    L3 = B / 2

    """
    --Set NIN, the number of cases in which an emmited
    neutron stops within the boundaries of the slab,
    thus producing an induced fission, equal to zero
    initially.
    """
    NIN = 0
    N = int(N)

    for i in range(0, N):
        """
        #For each spontaneous fission we need 9 random
        #numbers
        """

        R = rand9()  # generates 9 random numbers
        """
        -- Calculate the X, Y, and Z co-ordinates of the
        nucleus undergoing spontaneus emmision. They
        are random numbers inside the bondary of the
        block.
        Note: X,Y are in the interval (-A/2,+A/2)
                Z is in the interval (-B/2,+B/2)
        """
        X0 = A * (R[0] - 0.5)
        Y0 = A * (R[1] - 0.5)
        Z0 = B * (R[2] - 0.5)

        #begin loop over each of the two neutrons; 1 at a time
        K = 1
        for K in range(1, 3):
            #get two angles that define a random direction
            #in space for the neutron:
            PHI = 2 * math.pi * R[2 * K + 1]
            COSTH = 2 * (R[2 * K + 2] - 0.5)
            SINTH = math.sqrt(1 - COSTH ** 2)
            #get distance traveled by the neutron,
            #assumed to be a random number in the interval (0,1)
            D = R[K + 6]
            #calculate the coordinates of the end point
            #(interaction point) for the neutron
            X1 = X0 + D * SINTH * math.cos(PHI)
            Y1 = Y0 + D * SINTH * math.sin(PHI)
            Z1 = Z0 + D * COSTH
            #if the end point is inside the block,
            #the neutron produces an induced fission so add 1 to NIN:
            if abs(X1) <= L1 and abs(Y1) <= L2 and abs(Z1) <= L3:
                NIN += 1
            K += 1
    #output
    print("             MASS =", M)
    print(" LENGTH/THICKNESS =", S)
    print("# RANDOM FISSIONS =", N)

    #the survival fraction is NIN/N:
    F = NIN / N
    print("SURVIVAL FRACTION:", F)
    print()
    y = input("REPEAT? (y): ")