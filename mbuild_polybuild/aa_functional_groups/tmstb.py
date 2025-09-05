"""
Trimethylsilylpropylthiobutanol (TMSTB) moiety.

This module defines the `TMSTB` class, representing a trimethylsilylpropylthiobutanol functional group
for molecular simulations. The TMSTB group includes ports for molecular assembly.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups.tmstb import TMSTB
>>> tmstb = TMSTB()
>>> tmstb.save("trimethylsilylpropylthiobutanol.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class TMSTB(mb.Compound):
    """
    A trimethylsilylpropylthiobutanol (TMSTB) group.

    This class initializes a trimethylsilylpropylthiobutanol functional group by loading its structure
    from a PDB file and setting up its ports for molecular assembly.

    Ports
    -----
    - `port[0]`: Connection to the trimethylsilyl group.
    - `port[1]`: Connection to the propyl group.
    - `port[2]`: Connection to the butanol group.

    Examples
    --------
    >>> from mbuild_polybuild.aa_functional_groups.tmstb import TMSTB
    >>> tmstb = TMSTB()
    """

    def __init__(self):
        """
        Initialize the trimethylsilylpropylthiobutanol functional group.

        This method loads the TMSTB structure from the `trimethylsilylpropylthiobutanol.pdb` file,
        centers it at the origin, and sets up its ports.

        Ports
        -----
        - `port[0]`: Connection to the trimethylsilyl group.
        - `port[1]`: Connection to the propyl group.
        - `port[2]`: Connection to the butanol group.
        """
        super(TMSTB, self).__init__()

        mb.load(
            tb._import_pdb("trimethylsilylpropylthiobutanol.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = TMSTB()
    m.save("trimethylsilylpropylthiobutanol.mol2", overwrite=True)
