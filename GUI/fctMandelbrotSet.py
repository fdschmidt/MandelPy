# fctMandelbrotSet.py
# =============================================================================
#
# AUTHOR:           Franziska Schmidt (www.astrofranzi.com)
# CREATION DATE:    26.12.2018
# PROJECT:          Outreach
# DESCRIPTION:      Collection of functions required for the calculation of
#                   a Mandelbrot Set
# NOTES:            -
# HISTORY:          26.12.2018: Source file creation (F.Schmidt)
# =============================================================================


# Import libraries ------------------------------------------------------------
import numpy as np
# -----------------------------------------------------------------------------


# CalculateIterations (function)
# =============================================================================
# Description: Calculates how many iterations are necessary to reach threshold
# Input:       cNumber: A complex number
# Output:      Number of iterations (0 if threshold is not reached)
# History:     26.12.2018: Function created (F.Schmidt)
# =============================================================================

def CalculateIterations(cNumber, threshold, itMax):
    # Set the initial value of z equal to the complex number
    z = cNumber

    # Iterate over itMax
    for ii in range(itMax):

        # Stop if threshold surpassed
        if abs(z) > threshold:
            # Return number of iterations necessary to reach threshold
            return ii

        # Update complex number
        z = z * z + cNumber

    # Return if threshold is never reached
    return 0




# CalculateMandelbrotSet (function)
# =============================================================================
# Description: Calculates Mandelbrot Set
# Input:       xDomain list, yDomain list, empty Mandelbrot Set
# Output:      Updated Mandelbrot Set
# History:     26.12.2018: Function created (F.Schmidt)
# =============================================================================
def CalculateMandelbrotSet(xDomain, yDomain, mandelbrot, threshold, itMax):
    # Loop over rows (y values)
    for iY in range(len(yDomain)):

        # Loop over all columns (x values)
        for iX in range(len(xDomain)):
            # Generate complex number
            cNumber = np.complex(xDomain[iX], yDomain[iY])

            # Update mandelbort set
            mandelbrot[iY][iX] = CalculateIterations(cNumber, threshold, itMax)

    return mandelbrot

# -----------------------------------------------------------------------------