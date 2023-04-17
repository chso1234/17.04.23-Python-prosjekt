import math

def beregn_rektangel_areal(bredde, hoyde):
    """
    Beregn arealet av et rektangel med gitt bredde og høyde.
    """
    areal = bredde * hoyde
    return areal


def sirkelarealregning(radius):
    pi = math.pi
    areal = radius **2 * pi
    return areal