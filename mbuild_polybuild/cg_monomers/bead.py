"""Quaternary moiety."""

import numpy as np

import mbuild as mb


class Bead(mb.Compound):
    """
    General bead for coarse-graining with a variable number of ports placed for a coarse-grained scheme.

    Ports:
        "up" : First port, always present
        "down" : Second port, 180˚ from "up"
        "branch_up" : Third port are placed in a "T"
        "branch_down" : Fourth port placed in a cross

    Parameters
    ----------
    name : str
        Name of this bead type
    Nports : int, Optional, default=2
        Number of ports for this bead type placed for a coarse-grained scheme.
    compound_kwargs : dict, Optional, default={}
        Additional keyword arguements for the mb.Compound class (e.g. mass)
    """

    def __init__(self, name, Nports=2, bond_length=1.0):
        super(Bead, self).__init__()

        if Nports == 0:
            raise ValueError("A bead with zero ports is not available, use mb.Particle()")
        elif Nports > 4:
            raise ImportError("Bead with {} ports is not available".format(Nports))

        self.add(mb.Particle(name=name))

        self.add(mb.Port(anchor=self[0]), "up")
        self["up"].spin(np.pi, [0, 0, 1])
        self["up"].translate(np.array([0, bond_length / 2, 0]))

        if Nports > 1:
            self.add(mb.Port(anchor=self[0]), "down")
            self["down"].translate(np.array([0, -bond_length / 2, 0]))
        if Nports > 2:
            self.add(mb.Port(anchor=self[0]), "branch_up")
            self["branch_up"].spin(np.pi / 2, [0, 0, 1])
            self["branch_up"].translate(np.array([bond_length / 2, 0, 0]))
        if Nports > 3:
            self.add(mb.Port(anchor=self[0]), "branch_down")
            self["branch_down"].spin(-np.pi / 2, [0, 0, 1])
            self["branch_down"].translate(np.array([-bond_length / 2, 0, 0]))


if __name__ == "__main__":
    m = Bead()
    m.save("{}.mol2".format("bead"), overwrite=True)
