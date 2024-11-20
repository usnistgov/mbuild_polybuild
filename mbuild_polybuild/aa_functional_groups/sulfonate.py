"""Sulfonate moiety."""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class Sulfonate(mb.Compound):
    """An sulfonate group -S(=O)2O-"""

    def __init__(self):
        super(Sulfonate, self).__init__()

        mb.load(
            tb._import_pdb("sulfonate.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = Sulfonate()
    m.save("sulfonate.mol2", overwrite=True)
