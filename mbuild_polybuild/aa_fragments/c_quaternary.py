"""
This module defines the `C` class, representing a quaternary carbon moiety.

The `C` class is a specialized `mb.Compound` that loads a predefined quaternary
carbon structure from a PDB file and prepares it for further use in molecular
simulations.

Examples
--------
>>> from mbuild_polybuild.aa_fragments.c_quaternary import C
>>> c = C()
>>> c.save("c_quaternary.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class C(mb.Compound):
    """
    A quaternary carbon moiety.

    This class initializes a quaternary carbon structure by loading it from a
    PDB file and setting up its ports for molecular assembly.

    Examples
    --------
    >>> from mbuild_polybuild.aa_fragments.c_quaternary import C
    >>> c = C()
    """

    def __init__(self):
        """
        Initialize the quaternary carbon moiety.

        This method loads the quaternary carbon structure from the `c_quaternary.pdb`
        file, centers it at the origin, and sets up its ports.
        """
        super(C, self).__init__()

        mb.load(
            tb._import_pdb("c_quaternary.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = C()
    m.save("c_quaternary.mol2", overwrite=True)
