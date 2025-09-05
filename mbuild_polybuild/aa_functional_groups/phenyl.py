"""Phenyl moiety.

This module defines the `Phenyl` class, representing a phenyl functional group
for molecular simulations.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups.phenyl import Phenyl
>>> phenyl = Phenyl()
>>> phenyl.save("phenyl.mol2", overwrite=True)
"""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class Phenyl(mb.Compound):
    """
    A phenyl group.

    This class initializes a phenyl functional group by loading its structure
    from a PDB file and setting up its ports for molecular assembly.

    Examples
    --------
    >>> from mbuild_polybuild.aa_functional_groups.phenyl import Phenyl
    >>> phenyl = Phenyl()
    """

    def __init__(self):
        """
        Initialize the phenyl functional group.

        This method loads the phenyl structure from the `phenyl.pdb` file,
        centers it at the origin, and sets up its ports.
        """
        super(Phenyl, self).__init__()

        mb.load(
            tb._import_pdb("phenyl.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = Phenyl()
    m.save("phenyl.mol2", overwrite=True)
