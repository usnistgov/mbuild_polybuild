"""
Pyridinylthiopropanol (PTP) moiety.

This module defines the `PTP` class, representing a pyridinylthiopropanol functional group
for molecular simulations. The PTP group includes ports for molecular assembly.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups.ptp import PTP
>>> ptp = PTP()
>>> ptp.save("pyridinylthiopropanol.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class PTP(mb.Compound):
    """
    A pyridinylthiopropanol (PTP) group.

    This class initializes a pyridinylthiopropanol functional group by loading its structure
    from a PDB file and setting up its ports for molecular assembly.

    Ports
    -----
    - `port[0]`: Connection to the pyridinyl group.
    - `port[1]`: Connection to the thiopropanol group.

    Examples
    --------
    >>> from mbuild_polybuild.aa_functional_groups.ptp import PTP
    >>> ptp = PTP()
    """

    def __init__(self):
        """
        Initialize the pyridinylthiopropanol functional group.

        This method loads the PTP structure from the `pyridinylthiopropanol.pdb` file,
        centers it at the origin, and sets up its ports.

        Ports
        -----
        - `port[0]`: Connection to the pyridinyl group.
        - `port[1]`: Connection to the thiopropanol group.
        """
        super(PTP, self).__init__()

        mb.load(
            tb._import_pdb("pyridinylthiopropanol.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = PTP()
    m.save("pyridinylthiopropanol.mol2", overwrite=True)
