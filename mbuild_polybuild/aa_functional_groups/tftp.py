"""
Tridecafluorooctylthiopropanol (TFTP) moiety.

This module defines the `TFTP` class, representing a tridecafluorooctylthiopropanol functional group
for molecular simulations. The TFTP group includes ports for molecular assembly.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups.tftp import TFTP
>>> tftp = TFTP()
>>> tftp.save("tridecafluorooctylthiopropanol.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class TFTP(mb.Compound):
    """
    A tridecafluorooctylthiopropanol (TFTP) group.

    This class initializes a tridecafluorooctylthiopropanol functional group by loading its structure
    from a PDB file and setting up its ports for molecular assembly.

    Ports
    -----
    - `port[0]`: Connection to the tridecafluorooctyl group.
    - `port[1]`: Connection to the thiopropanol group.

    Examples
    --------
    >>> from mbuild_polybuild.aa_functional_groups.tftp import TFTP
    >>> tftp = TFTP()
    """

    def __init__(self):
        """
        Initialize the tridecafluorooctylthiopropanol functional group.

        This method loads the TFTP structure from the `tridecafluorooctylthiopropanol.pdb` file,
        centers it at the origin, and sets up its ports.

        Ports
        -----
        - `port[0]`: Connection to the tridecafluorooctyl group.
        - `port[1]`: Connection to the thiopropanol group.
        """
        super(TFTP, self).__init__()

        mb.load(
            tb._import_pdb("tridecafluorooctylthiopropanol.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = TFTP()
    m.save("tridecafluorooctylthiopropanol.mol2", overwrite=True)
