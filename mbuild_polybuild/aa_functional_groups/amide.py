"""Amide moiety."""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class Amide(mb.Compound):
    """An amide group -C(=O)N(H)-."""

    def __init__(self):
        super(Amide, self).__init__()

        mb.load(
            tb._import_pdb("amide.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = Amide()
    m.save("amide.mol2", overwrite=True)
