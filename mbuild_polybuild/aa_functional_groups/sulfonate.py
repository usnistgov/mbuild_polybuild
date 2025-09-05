"""Sulfonate moiety.

This module defines the `Sulfonate` class, representing a sulfonate functional group
(-S(=O)2O-) for molecular simulations. The Sulfonate group includes ports for molecular assembly.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups.sulfonate import Sulfonate
>>> sulfonate = Sulfonate()
>>> sulfonate.save("sulfonate.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class Sulfonate(mb.Compound):
    """
    A sulfonate group (-S(=O)2O-).

    This class initializes a sulfonate functional group by loading its structure
    from a PDB file and setting up its ports for molecular assembly.

    Ports
    -----
    - `port[0]`: Connection to the sulfur atom.
    - `port[1]`: Connection to the oxygen atom.

    Examples
    --------
    >>> from mbuild_polybuild.aa_functional_groups.sulfonate import Sulfonate
    >>> sulfonate = Sulfonate()
    """

    def __init__(self):
        """
        Initialize the sulfonate functional group.

        This method loads the sulfonate structure from the `sulfonate.pdb` file,
        centers it at the origin, and sets up its ports.

        Ports
        -----
        - `port[0]`: Connection to the sulfur atom.
        - `port[1]`: Connection to the oxygen atom.
        """
        super(Sulfonate, self).__init__()

        mb.load(
            tb._import_pdb("sulfonate.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = Sulfonate()
    m.save("sulfonate.mol2", overwrite=True)
