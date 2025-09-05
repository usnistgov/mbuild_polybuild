"""
Methoxyphenylthiobutanol (MPTB) moiety.

This module defines the `MPTB` class, representing a methoxyphenylthiobutanol functional group
for molecular simulations. The MPTB group includes ports for molecular assembly.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups.mptb import MPTB
>>> mptb = MPTB()
>>> mptb.save("methoxyphenylthiobutanol.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class MPTB(mb.Compound):
    """
    A methoxyphenylthiobutanol (MPTB) group.

    This class initializes a methoxyphenylthiobutanol functional group by loading its structure
    from a PDB file and setting up its ports for molecular assembly.

    Ports
    -----
    - `port[0]`: Connection to the methoxy group.
    - `port[1]`: Connection to the phenyl group.
    - `port[2]`: Connection to the butanol group.

    Examples
    --------
    >>> from mbuild_polybuild.aa_functional_groups.mptb import MPTB
    >>> mptb = MPTB()
    """

    def __init__(self):
        """
        Initialize the methoxyphenylthiobutanol functional group.

        This method loads the MPTB structure from the `methoxyphenylthiobutanol.pdb` file,
        centers it at the origin, and sets up its ports.

        Ports
        -----
        - `port[0]`: Connection to the methoxy group.
        - `port[1]`: Connection to the phenyl group.
        - `port[2]`: Connection to the butanol group.
        """
        super(MPTB, self).__init__()

        mb.load(
            tb._import_pdb("methoxyphenylthiobutanol.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = MPTB()
    m.save("methoxyphenylthiobutanol.mol2", overwrite=True)
