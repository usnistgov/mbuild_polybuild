"""
Trifluoroethylthiobutanol (TFTB) moiety.

This module defines the `TFTB` class, representing a trifluoroethylthiobutanol functional group
for molecular simulations. The TFTB group includes ports for molecular assembly.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups.tftb import TFTB
>>> tftb = TFTB()
>>> tftb.save("trifluoroethylthiobutanol.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class TFTB(mb.Compound):
    """
    A trifluoroethylthiobutanol (TFTB) group.

    This class initializes a trifluoroethylthiobutanol functional group by loading its structure
    from a PDB file and setting up its ports for molecular assembly.

    Ports
    -----
    - `port[0]`: Connection to the trifluoroethyl group.
    - `port[1]`: Connection to the butanol group.

    Examples
    --------
    >>> from mbuild_polybuild.aa_functional_groups.tftb import TFTB
    >>> tftb = TFTB()
    """

    def __init__(self):
        """
        Initialize the trifluoroethylthiobutanol functional group.

        This method loads the TFTB structure from the `trifluoroethylthiobutanol.pdb` file,
        centers it at the origin, and sets up its ports.

        Ports
        -----
        - `port[0]`: Connection to the trifluoroethyl group.
        - `port[1]`: Connection to the butanol group.
        """
        super(TFTB, self).__init__()

        mb.load(
            tb._import_pdb("trifluoroethylthiobutanol.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = TFTB()
    m.save("trifluoroethylthiobutanol.mol2", overwrite=True)
