"""Phenyl moiety."""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class Phenyl(mb.Compound):
    """An phenyl"""

    def __init__(self):
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
