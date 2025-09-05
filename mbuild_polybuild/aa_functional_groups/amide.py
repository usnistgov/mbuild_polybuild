"""
Amide moiety.

This module defines the `Amide` class, representing an amide functional group
(-C(=O)N(H)-) for molecular simulations. The amide group includes ports for molecular assembly.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups.amide import Amide
>>> amide = Amide()
>>> amide.save("amide.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class Amide(mb.Compound):
    """
    An amide group (-C(=O)N(H)-).

    This class initializes an amide functional group by loading its structure
    from a PDB file and setting up its ports for molecular assembly.

    Ports
    -----
    - `port[0]`: Connection to the carbon atom.
    - `port[1]`: Connection to the nitrogen atom.

    Examples
    --------
    >>> from mbuild_polybuild.aa_functional_groups.amide import Amide
    >>> amide = Amide()
    """

    def __init__(self):
        """
        Initialize the amide functional group.

        This method loads the amide structure from the `amide.pdb` file,
        centers it at the origin, and sets up its ports.

        Ports
        -----
        - `port[0]`: Connection to the carbon atom.
        - `port[1]`: Connection to the nitrogen atom.
        """
        super(Amide, self).__init__()

        mb.load(
            tb._import_pdb("amide.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = Amide()
    m.save("amide.mol2", overwrite=True)
