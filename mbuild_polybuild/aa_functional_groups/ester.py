"""Ester moiety.

This module defines the `Ester` class, representing an ester functional group
(-C(=O)O-) for molecular simulations. The ester group includes ports for molecular assembly.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups.ester import Ester
>>> ester = Ester()
>>> ester.save("ester.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class Ester(mb.Compound):
    """
    An ester group (-C(=O)O-).

    This class initializes an ester functional group by loading its structure
    from a PDB file and setting up its ports for molecular assembly.

    Ports
    -----
    - `port[0]`: Connection to the carbon atom.
    - `port[1]`: Connection to the oxygen atom.

    Parameters
    ----------
    ion : bool, optional, default=False
        If True, removes the second port to represent an ionized ester group.

    Examples
    --------
    >>> from mbuild_polybuild.aa_functional_groups.ester import Ester
    >>> ester = Ester(ion=True)
    """

    def __init__(self, ion=False):
        """
        Initialize the ester functional group.

        This method loads the ester structure from the `ester.pdb` file,
        centers it at the origin, and sets up its ports. Optionally, it can
        remove the second port to represent an ionized ester group.

        Ports
        -----
        - `port[0]`: Connection to the carbon atom.
        - `port[1]`: Connection to the oxygen atom.

        Parameters
        ----------
        ion : bool, optional, default=False
            If True, removes the second port to represent an ionized ester group.
        """
        super(Ester, self).__init__()

        mb.load(
            tb._import_pdb("ester.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)

        if ion:
            self.remove(self["port[1]"], reset_labels=True)


if __name__ == "__main__":
    m = Ester()
    m.save("ester.mol2", overwrite=True)
