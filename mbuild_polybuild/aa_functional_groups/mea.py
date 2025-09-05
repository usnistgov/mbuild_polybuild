"""
Monoethanolamine (MEA) moiety.

This module defines the `MEA` class, representing a monoethanolamine functional group
for molecular simulations. The MEA group includes ports for attaching to other molecules.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups.mea import MEA
>>> mea = MEA()
>>> mea.save("mea.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class MEA(mb.Compound):
    """
    A monoethanolamine (MEA) group.

    This class initializes a monoethanolamine functional group by loading its structure
    from a PDB file and setting up its ports for molecular assembly.

    Ports
    -----
    - `port[0]`: Connection to the nitrogen atom.
    - `port[1]`: Connection to the hydroxyl group.

    Examples
    --------
    >>> from mbuild_polybuild.aa_functional_groups.mea import MEA
    >>> mea = MEA()
    """

    def __init__(self):
        """
        Initialize the monoethanolamine functional group.

        This method loads the MEA structure from the `mea.pdb` file,
        centers it at the origin, and sets up its ports.

        Ports
        -----
        - `port[0]`: Connection to the nitrogen atom.
        - `port[1]`: Connection to the hydroxyl group.
        """
        super(MEA, self).__init__()

        mb.load(
            tb._import_pdb("mea.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = MEA()
    m.save("mea.mol2", overwrite=True)
