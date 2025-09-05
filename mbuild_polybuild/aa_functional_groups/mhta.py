"""Methylhydroxypropylthioacetate (MHTA) moiety.

This module defines the `MHTA` class, representing a methylhydroxypropylthioacetate functional group
for molecular simulations. The MHTA group includes ports for molecular assembly.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups.mhta import MHTA
>>> mhta = MHTA()
>>> mhta.save("methylhydroxypropylthioacetate.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class MHTA(mb.Compound):
    """
    A methylhydroxypropylthioacetate (MHTA) group.

    This class initializes a methylhydroxypropylthioacetate functional group by loading its structure
    from a PDB file and setting up its ports for molecular assembly.

    Ports
    -----
    - `port[0]`: Connection to the methyl group.
    - `port[1]`: Connection to the hydroxyl group.
    - `port[2]`: Connection to the thioacetate group.

    Examples
    --------
    >>> from mbuild_polybuild.aa_functional_groups.mhta import MHTA
    >>> mhta = MHTA()
    """

    def __init__(self):
        """
        Initialize the methylhydroxypropylthioacetate functional group.

        This method loads the MHTA structure from the `methylhydroxypropylthioacetate.pdb` file,
        centers it at the origin, and sets up its ports.

        Ports
        -----
        - `port[0]`: Connection to the methyl group.
        - `port[1]`: Connection to the hydroxyl group.
        - `port[2]`: Connection to the thioacetate group.
        """
        super(MHTA, self).__init__()

        mb.load(
            tb._import_pdb("methylhydroxypropylthioacetate.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = MHTA()
    m.save("methylhydroxypropylthioacetate.mol2", overwrite=True)
